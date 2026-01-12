from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END
from agent.intent import detect_intent
from agent.rag import RAGEngine
from agent.tools import mock_lead_capture
from agent.memory import AgentState
from langchain_groq import ChatGroq
from config.settings import GROQ_MODEL, TEMPERATURE, GROQ_API_KEY

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL,
    temperature=TEMPERATURE
)

rag = RAGEngine()


def intent_node(state: AgentState):
    if state.get("in_lead_flow"):
        return state

    user_input = state["messages"][-1]
    intent = detect_intent(user_input)

    return {**state, "intent": intent}



def greeting_node(state):
    messages = list(state["messages"])
    messages.append("Hello!  How can I help you with AutoStream today?")
    return {**state, "messages": messages}



def rag_node(state):
    question = state["messages"][-1]
    answer = rag.query(question)
    response = f"Here is what I found:\n{answer}"

    messages = list(state["messages"])
    messages.append(response)

    return {**state, "messages": messages}



def lead_collection_node(state):
    messages = list(state["messages"])

    if not state.get("name"):
        messages.append("May I have your name?")
        return {**state, "in_lead_flow": True, "current_field": "name", "awaiting_input": True, "messages": messages}

    if not state.get("email"):
        messages.append("Please share your email address.")
        return {**state, "in_lead_flow": True, "current_field": "email", "awaiting_input": True, "messages": messages}

    if not state.get("platform"):
        messages.append("Which platform do you create content for? (YouTube, Instagram, etc.)")
        return {**state, "in_lead_flow": True, "current_field": "platform", "awaiting_input": True, "messages": messages}

    mock_lead_capture(state["name"], state["email"], state["platform"])

    messages.append("You are all set! Our team will contact you shortly.")

    return {
        **state,
        "completed": True,
        "current_field": "",
        "awaiting_input": False,
        "messages": messages
    }
def store_details_node(state: AgentState):
    # Only store when agent is waiting for user input
    if not state.get("awaiting_input"):
        return {**state}

    value = state.get("last_user_input", "").strip()
    field = state.get("current_field", "")

    if not value or not field:
        return {**state}

    new_state = dict(state)
    new_state[field] = value

    # stop storing until next question
    new_state["awaiting_input"] = False

    return new_state



def router(state):
    if state.get("completed"):
        return END

    if state.get("awaiting_input"):
        return "store"

    if state.get("in_lead_flow"):
        return "lead"

    intent = state["intent"]

    if intent == "greeting":
        return "greet"
    elif intent == "product_query":
        return "rag"
    elif intent == "high_intent":
        return "lead"
    else:
        return "lead"


      


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("intent", intent_node)
    builder.add_node("greet", greeting_node)
    builder.add_node("rag", rag_node)
    builder.add_node("lead", lead_collection_node)
    builder.add_node("store", store_details_node)

    builder.set_entry_point("intent")

    builder.add_conditional_edges("intent", router, {
    "greet": "greet",
    "rag": "rag",
    "lead": "lead",
    "store": "store",
    END: END
})

    builder.add_edge("store", "lead")
    builder.add_edge("greet", END)
    builder.add_edge("rag", END)


    return builder.compile()

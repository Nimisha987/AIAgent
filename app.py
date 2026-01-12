from agent.graph import build_graph

def main():
    graph = build_graph()

    state = {
    "messages": [],
    "intent": "",
    "name": "",
    "email": "",
    "platform": "",
    "completed": False,
    "in_lead_flow": False,
    "last_user_input": "",
    "current_field": "",
    "awaiting_input": False
}



    print("AutoStream AI Agent started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        # User message
        state["messages"].append(user_input)
        state["last_user_input"] = user_input   


        # Invoke graph
        result = graph.invoke(state)

        # Agent reply
        agent_reply = result["messages"][-1]
        print("Agent:", agent_reply)

        # Save agent reply
        state["messages"].append(agent_reply)

        # Merge state
        state = {**state, **result}

if __name__ == "__main__":
    main()

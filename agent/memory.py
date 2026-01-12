from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List[str]
    intent: str
    name: str
    email: str
    platform: str
    completed: bool
    in_lead_flow: bool
    last_user_input: str
    current_field: str  
    awaiting_input: bool  
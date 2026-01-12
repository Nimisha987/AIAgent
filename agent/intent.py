def detect_intent(user_input:str)->str:
    text=user_input.lower()

    greetings=['hi','hello','hey']
    buying=['buy','purchase','sign-up','subscribe','want to try','get pro']

    if any(word in text for word in greetings):
        return "greeting"
    
    if any(word in text for word in buying):
        return "high_intent"
    
    return "product_query"
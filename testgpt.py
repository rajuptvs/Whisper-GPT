from revChatGPT.revChatGPT import Chatbot

def chatme(msg="Byeee"):
    config = {
        "email": "your_email_goes_here",
        "password": "your_passowrd_here"
    }


    chatbot = Chatbot(config, conversation_id=None)

    print("Input given is .....",msg)
    message = chatbot.get_chat_response(msg)['message']
    print(message)
    return message

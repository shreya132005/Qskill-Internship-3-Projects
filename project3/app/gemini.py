from app.chat import chat_with_memory

print("RealTimeGemBot – Gemini AI with Memory & Live Search")
print("Type 'exit' to quit\n ")

while True:
    user_input = input("You: ")
    
    if user_input.lower()=="exit":
        print("Goodbye")
        break
    reply = chat_with_memory(user_input)
    print("AI:", reply)

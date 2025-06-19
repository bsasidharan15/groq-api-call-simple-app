#!/usr/bin/env python3
"""
Simple Groq Chat Assistant
Direct conversational AI using Groq API
"""

import os
from groq import Groq

# Your API key
GROQ_API_KEY = "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"

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def chat_with_ai(user_message, model="qwen/qwen3-32b"):
    """Send message to AI and get response"""
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Be conversational and helpful."},
                {"role": "user", "content": user_message}
            ],
            model=model,
            temperature=0.7,
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def main():
    """Main chat loop"""
    print("🤖 AI: Hey! How can I help you?")
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("🤖 AI: Goodbye! Have a great day!")
            break
        
        if not user_input:
            continue
        
        # Get AI response
        ai_response = chat_with_ai(user_input)
        print(f"🤖 AI: {ai_response}")

if __name__ == "__main__":
    main()

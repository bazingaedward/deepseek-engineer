from langchain_deepseek import ChatDeepSeek

if __name__ == "__main__":
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    messages = [
        ("human", "你好，上海幼儿园的平均学费多少, 请用中文回答"),
    ]
    
    ai_msg = llm.invoke(messages)
    print(ai_msg.content, 111)
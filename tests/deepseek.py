from langchain_deepseek import ChatDeepSeek



if __name__ == "__main__":
    llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    # DeepSeek-R1（通过 指定model="deepseek-reasoner"）不支持工具调用或结构化输出。这些功能由 DeepSeek-V3（通过 指定）支持model="deepseek-chat"。
    messages = [
        ("system", "You are a helpful translator. Translate the user sentence to French."),
        ("human", "I love programming."),
    ]
    
    llm.invoke(messages)
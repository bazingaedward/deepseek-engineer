from gpt_engineer.applications.cli.main import app
from langchain_openai import  ChatOpenAI
# 测试openai chat的能力
import os
import getpass 

if __name__ == "__main__":
    app()
    # ai = ChatOpenAI(
    #     model='gpt-4o',
    #     temperature=0.1,
    #     streaming=False,
    #     # callbacks=[StreamingStdOutCallbackHandler()],
    # )
  

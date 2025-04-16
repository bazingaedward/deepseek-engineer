from gpt_engineer.applications.cli.main import app
from langchain_openai import  ChatOpenAI
# 测试openai chat的能力
import os
import getpass 

if __name__ == "__main__":
    # app()
    # ai = ChatOpenAI(
    #     model='gpt-4o',
    #     temperature=0.1,
    #     streaming=False,
    #     # callbacks=[StreamingStdOutCallbackHandler()],
    # )
  

    if not os.environ.get("OPENAI_API_KEY"):
      os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    from langchain.chat_models import init_chat_model

    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    from langchain_core.messages import HumanMessage, SystemMessage

    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]

    model.invoke(messages)
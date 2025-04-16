import tiktoken

if __name__ == "__main__":
    # 通过模型名称加载编码
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    # encoding = tiktoken.encoding_for_model("gpt-4o")

    # 或者按编码名称加载
    # encoding = tiktoken.get_encoding("cl100k_base")

    # text = "This is an example sentence."
    text = "你好"

    # 编码文本为 token ID 列表
    tokens = encoding.encode(text)
    print(f"Tokens: {tokens}")

    # 获取 token 数量
    num_tokens = len(tokens)
    print(f"Number of tokens: {num_tokens}")

    # 将 token ID 列表解码回文本
    decoded_text = encoding.decode(tokens)
    print(f"Decoded text: {decoded_text}")
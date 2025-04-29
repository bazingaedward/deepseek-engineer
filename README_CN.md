# Deepseek engineer

借助deepseek和langchain的能力来尝试颠覆传统的软件开发模式，将大语言模型的能力快速转换成生产力，并不断学习进化。


## 项目背景
deepseek 在国内拥有广泛的使用和用户背景，得到了很多用户的认可和支持。同时价格也比openai等国外大模型便宜，具有很高的性价比。因此，如果将deepseek与代码生成的能力结合，相信可以进一步释放用户的生产力。这里的用户既包括开发者，也包括产品经理，UIUX等其他角色的用户。帮助他们做快速的项目落地和验证。

## 测试sse服务

```shell
# 启动服务
uvicorn tests/sse:app --reload
```

``` chrome dev中
const eventSource = new EventSource('/events');

eventSource.onmessage = (event) => {
  console.log('Received event:', event.data);
  document.getElementById('output').textContent += event.data + '\n';
};

eventSource.onerror = (error) => {
  console.error('EventSource failed:', error);
  eventSource.close();
};
```
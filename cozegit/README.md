# Coze Agent 本地调用示例

这是一个使用 Coze API 进行本地对话的示例项目。

## 环境要求

- Python 3.7+
- pip

## 安装步骤

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置环境变量：
- 复制 `.env` 文件并填写以下信息：
  - `COZE_API_TOKEN`：你的 Coze API 令牌
  - `BOT_ID`：你的 Bot ID（从 Coze 网页端 Bot 链接中获取）

## 使用方法

运行程序：
```bash
python chat_with_coze.py
```

- 程序启动后，可以直接输入问题进行对话
- 输入 'quit' 退出程序

## 注意事项

- 请确保你的 API 令牌和 Bot ID 配置正确
- 所有对话都会生成唯一的用户ID
- 使用了流式响应，可以实时看到 AI 的回复 
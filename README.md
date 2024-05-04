# Cloudflare AI 中文聊天

Cloudflare AI 聊天是一个基于 Python 和 Tkinter 的桌面应用程序，它允许用户与 Cloudflare AI 进行交互式对话，并提供实时翻译功能。

## 功能

- **AI 聊天**：与 Cloudflare AI 模型进行实时对话。
- **实时翻译**：将 AI 的回复从英语翻译成中文。
- **图形用户界面**：简洁的 GUI，方便用户输入消息和查看聊天历史(没有上下文记忆)。

## 如何使用

1. 克隆仓库到本地或下载 `CN-cloudflare-AI-GUI.py` 文件。
2. 确保您的系统已安装 Python 和相关库（Tkinter, requests）。
3. 运行程序，它将启动一个窗口。
4. 在文本框中输入您的消息，然后点击“发送”按钮。
5. 查看 AI 的回复，它将自动翻译成中文并显示在聊天历史中。

## 开发

该程序使用 Python 3、Tkinter 库以及 Cloudflare AI API 进行开发。您可以通过修改 `API_BASE_URL` 和 `headers` 来配置 API 访问。

## 提示

- 我在代码中公开您的 API 密钥,但我希望您不会散播或用于您自己的程序。
- 此程序在向Cloudflare发送和接受信息时会出现无响应,属于正常现象

## 贡献

欢迎贡献！如果您有任何建议或改进，请随时提交 pull request 或开 issue。

## 许可

该项目采用 MIT 许可证。有关详细信息，请查看 LICENSE 文件。

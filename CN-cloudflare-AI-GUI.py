import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/867520dfa43947e67f0416d72989a2af/ai/run/"
headers = {"Authorization": "Bearer DR4-UajY4Kkd5m5mqMF0TGJs-lITDZ19h6krTfGV"}

def chat_with_ai(model, message):
    input_data = [
        {"role": "user", "content": message}
    ]
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json={"messages": input_data})
    return response.json()

def translate_text(text):
    response = requests.get(url=f"https://t.ae3ee.xyz/?text={text}&source_language=en&target_language=zh&secret=Lcoavie")
    return response.json()

model_name = "@cf/meta/llama-2-7b-chat-int8"

def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"你: {user_message}\n")
    chat_history.config(state=tk.DISABLED)
    
    response = chat_with_ai(model_name, user_message)
    
    if 'result' in response and 'response' in response['result']:
        translated_response = translate_text(response['result']['response'])
        if 'text' in translated_response:
            chat_history.config(state=tk.NORMAL)
            chat_history.insert(tk.END, f"AI: {translated_response['text']}\n")
            chat_history.config(state=tk.DISABLED)
        else:
            chat_history.config(state=tk.NORMAL)
            chat_history.insert(tk.END, "AI: 回复翻译失败,请通知开发者.\n")
            chat_history.config(state=tk.DISABLED)
    else:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, "AI: 对不起，我没能理解你的意思。你能重新表达一下吗？\n")
        chat_history.config(state=tk.DISABLED)

    # 清空输入框
    user_input.delete('1.0', tk.END)

def exit_chat():
    if messagebox.askyesno("退出", "你确定要退出聊天吗？"):
        root.destroy()

root = tk.Tk()
root.title("Cloudflare AI 聊天 - BiliBili baicaizhale")

chat_history = scrolledtext.ScrolledText(root, width=50, height=20, state='disabled')  # 设置 state='disabled'
chat_history.pack(padx=10, pady=10)

user_input = tk.Text(root, height=3)
user_input.pack(padx=10)

send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack(pady=5)

exit_button = tk.Button(root, text="退出", command=exit_chat)
exit_button.pack(pady=5)

root.mainloop()

import os
import requests
import PyPDF2
import datetime
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

# 读取PDF文件的第200页内容
def extract_page_content(pdf_path, page_number):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        if page_number < len(reader.pages):
            page = reader.pages[page_number]
            return page.extract_text()
        else:
            raise ValueError("Page number exceeds the total number of pages in the PDF.")

# 使用DeepSeek API翻译文本
def translate_text(text):
    """
    使用DeepSeek API翻译文本
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate the following text from English to Chinese:\n{text}"},
        ],
        stream=True
    )

    # 处理流式响应
    translated_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        translated_content += content if content else ""

    return translated_content

# 保存翻译结果到Markdown文件
def save_to_markdown(content, original_content, page_number, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"# PDF的第{page_number + 1}页开始=======\n\n")
        # .write(f"**Original Content:**\n\n{original_content}\n\n")
        file.write(f"\n\n{content}\n\n")
        file.write(f"# PDF的第{page_number + 1}页结束=======\n\n")

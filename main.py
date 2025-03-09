import concurrent.futures
from deepseek_pdf_trans_lib import extract_page_content, translate_text, save_to_markdown
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 定义 translate_and_save 函数
def translate_and_save(pdf_path, start_page, end_page):
    for page_number in range(start_page, end_page + 1):
        # 提取当前页内容
        page_content = extract_page_content(pdf_path, page_number)
        
        # 翻译内容
        translated_content = translate_text(page_content)
        
        # 保存翻译结果
        save_to_markdown(translated_content, page_content, page_number, f"{pdf_path}_ZN-{start_page+1}-{end_page+1}.md")
        print(f"翻译结果已保存到{pdf_path}_ZN-{start_page}-{end_page}.md，页码: {page_number + 1}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_path = request.form['pdf_path']
        start_page = int(request.form['start_page'])
        end_page = int(request.form['end_page'])
        
        if not os.path.exists(pdf_path):
            flash('PDF文件不存在，请检查路径。')
            return redirect(url_for('index'))
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            executor.submit(translate_and_save, pdf_path, start_page, end_page)
        
        flash('翻译任务已提交。')
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
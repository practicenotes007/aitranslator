# 使用指南

1. 安装依赖库：
   ```
   pip install -r requirements.txt
   ```

2. 创建 `.env` 文件，并添加以下内容：
   ```
   API_KEY=your_openai_api_key_here
   BASE_URL=your_base_url_here
   ```

   你可以参考 `.env.example` 文件创建 `.env` 文件。

3. 配置需要翻译的页码范围：
   - 打开 `deepseek_pdf_trans.py` 文件。
   - 修改 `start_page` 和 `end_page` 变量，设置需要翻译的页码范围。例如，翻译第829页到第892页：
     ```python
     start_page = 829  # 起始页码
     end_page = 892    # 结束页码
     ```

4. 运行脚本：
   ```
   python deepseek_pdf_trans.py
   ```
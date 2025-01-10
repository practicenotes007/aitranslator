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
   - 打开 `main.py` 文件。
   - 修改 main函数中的`start_page` 和 `end_page` 变量，设置需要翻译的页码范围。例如，翻译第829页到第892页：
     ```python
     start_page = 829  # 起始页码（注意：从0开始，即PDF文档的第1页在这里是0。）
     end_page = 892    # 结束页码
     ```

4. 运行脚本：（多线程版本，根据页数最多启动10个线程访问DeepSeek LLM）
   ```
   python main.py
   ```

5. 翻译结果会根据启动的线程个数保存到当前目录下的文件中。
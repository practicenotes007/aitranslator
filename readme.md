# PDF 智能翻译工具

基于 Flask 的 PDF 多线程翻译工具，支持指定页码范围翻译并保存为 Markdown 格式。

## 功能特性
- 多线程 PDF 页面内容提取
- DeepSeek 翻译接口集成
- 翻译结果自动保存为双语对照格式
- Web 界面交互式操作

## 快速开始

### 环境要求
- Python 3.7+
- 以下依赖库：
```
pip install requests PyPDF2 python-dotenv flask
```
### 配置步骤
在项目根目录创建 .env 文件：
```
API_KEY=your_deepseek_api_key
BASE_URL=https://api.deepseek.com/v1
```
### 启动 Flask 应用：
```
python main.py
```

访问 Web 界面： http://localhost:5000

### 使用说明

在网页表单中输入：
PDF 文件绝对路径（例如：D:/documents/sample.pdf）
起始页码和结束页码
点击提交开始后台翻译任务
翻译结果保存在同目录下，命名格式：原文件名_ZN-起始页-结束页.md

### 常见问题

Q1: 提示 "PDF 文件不存在" 

➔ 请检查文件路径是否正确，Windows 系统建议使用绝对路径

Q2: 翻译接口报错 

➔ 请确认 .env 文件中的 API 密钥和接口地址配置正确

Q3: 如何查看实时翻译进度？ 

➔ 查看控制台输出的保存日志
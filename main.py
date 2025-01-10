import concurrent.futures
from deepseek_pdf_trans_lib import extract_page_content, translate_text, save_to_markdown

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

# 主函数
def main():
    pdf_path = 'UEFI_Spec_2_9_2021_03-18.pdf'  # 替换为你的PDF文件路径   ACPI_Spec_6_5_Aug29
    start_page = 0  # 起始页码（从0开始）
    end_page = 3    # 结束页码

    # 计算页码数量
    page_count = end_page - start_page + 1

    # 根据页码数量确定线程数量
    if page_count < 10:
        num_threads = 1
    elif page_count < 50:
        num_threads = 5
    else:
        num_threads = 10

    # 计算每个线程处理的页码范围
    pages_per_thread = (page_count + num_threads - 1) // num_threads
    threads = []

    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start = start_page + i * pages_per_thread
            end = min(start + pages_per_thread - 1, end_page)
            future = executor.submit(translate_and_save, pdf_path, start, end)
            threads.append(future)

        # 等待所有线程完成
        for future in concurrent.futures.as_completed(threads):
            future.result()

if __name__ == "__main__":
    main()

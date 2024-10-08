import opencc

# 創建轉換器
converter = opencc.OpenCC('t2s')  # 繁體轉簡體

# 讀取文件
with open('2023.08.15 (1).srt', 'r', encoding='utf-8') as file:
    content = file.read()

# 進行繁體到簡體的轉換
simplified_content = converter.convert(content)

# 將轉換後的內容寫回新文件
with open('your_file_simplified.srt', 'w', encoding='utf-8') as file:
    file.write(simplified_content)

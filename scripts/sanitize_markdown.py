import re
import os
import glob
import sys

def remove_tooltips(text):
    # ツールチップのタグ自体を削除（中身は残さないといけないが、中身が壊れている場合もあるので注意）
    # 単純なタグ削除
    text = re.sub(r'{{< tooltip[^>]* >}}', '', text)
    text = re.sub(r'{{< /tooltip >}}', '', text)
    return text

def find_balanced_close(text, start_index, open_char, close_char):
    count = 0
    for i in range(start_index, len(text)):
        if text[i] == open_char:
            count += 1
        elif text[i] == close_char:
            count -= 1
            if count == 0:
                return i
    return -1

def strip_links(text):
    # リンク [text](url) を text に置換する
    # 入れ子になっている場合も、外側から順に（あるいは見つかった順に）剥がしていくことで最終的にテキストのみにする
    # ループして、これ以上 [text](url) のパターンが見つからなくなるまで繰り返す
    
    while True:
        original_text = text
        found_change = False
        
        i = 0
        while i < len(text):
            if text[i] == '[':
                # リンク開始の可能性
                # 対応する ] を探す
                close_bracket = find_balanced_close(text, i, '[', ']')
                if close_bracket != -1:
                    # 次が ( か確認
                    if close_bracket + 1 < len(text) and text[close_bracket + 1] == '(':
                        # 対応する ) を探す
                        close_paren = find_balanced_close(text, close_bracket + 1, '(', ')')
                        if close_paren != -1:
                            # リンク確定: [text](url)
                            # text部分を取り出す
                            link_text = text[i+1:close_bracket]
                            
                            # 置換実行
                            prefix = text[:i]
                            suffix = text[close_paren+1:]
                            text = prefix + link_text + suffix
                            
                            found_change = True
                            break # テキスト長が変わったのでループを抜けて最初から再スキャン
                
            i += 1
            
        if not found_change:
            break
            
    return text

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Front matterと本文を分離
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            body = parts[2]
            
            # 1. まずツールチップタグを削除
            cleaned_body = remove_tooltips(body)
            
            # 2. 次にリンクを剥がす（再帰的に全てテキスト化）
            cleaned_body = strip_links(cleaned_body)
            
            # 再結合
            new_content = f'---{front_matter}---{cleaned_body}'
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Sanitized: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⚠️ Skipped (No front matter): {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/sanitize_markdown.py <directory_or_file>")
        sys.exit(1)
        
    target = sys.argv[1]
    
    if os.path.isfile(target):
        process_file(target)
    elif os.path.isdir(target):
        files = glob.glob(os.path.join(target, "**/*.md"), recursive=True)
        for f in files:
            process_file(f)

if __name__ == "__main__":
    main()

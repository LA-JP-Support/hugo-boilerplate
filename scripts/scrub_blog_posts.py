import re
import os
import glob
import sys

def clean_nested_content(text):
    # 1. Tooltips: 内側から順に解除
    # 最も内側のツールチップ（中に他のツールチップを含まないもの）を探して置換
    # {{< tooltip ... >}}Content{{< /tooltip >}}
    tooltip_pattern = re.compile(r'{{< tooltip[^>]* >}}((?:(?!{{< tooltip).)*?){{< /tooltip >}}', re.DOTALL)
    
    while True:
        match = tooltip_pattern.search(text)
        if not match:
            break
        # 置換: タグを削除し、中身だけ残す
        text = text[:match.start()] + match.group(1) + text[match.end():]
    
    # 2. Links: 内側から順に解除
    # 最も内側のリンク（中に他のリンクを含まないもの）を探して置換
    # [Text](URL "Title") or [Text](URL)
    # [^\[\]] は [ や ] を含まない文字
    link_pattern = re.compile(r'\[([^\[\]]*)\]\([^\)]+\)', re.DOTALL)
    
    while True:
        match = link_pattern.search(text)
        if not match:
            break
        # 置換: リンク記法を削除し、テキストだけ残す
        text = text[:match.start()] + match.group(1) + text[match.end():]

    # 3. 残ったゴミの掃除
    # ツールチップの閉じタグの残りなど
    text = re.sub(r'{{< /tooltip >}}', '', text)
    # ツールチップの開始タグの残り（閉じタグがなくてマッチしなかったものなど）
    text = re.sub(r'{{< tooltip[^>]* >}}', '', text)
    
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
            
            # 本文のみをクリーニング
            cleaned_body = clean_nested_content(body)
            
            # 再結合
            new_content = f'---{front_matter}---{cleaned_body}'
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Cleaned: {os.path.basename(file_path)}")
            return True
        else:
            print(f"⚠️ Skipped (No front matter): {os.path.basename(file_path)}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/scrub_blog_posts.py <directory_or_file>")
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

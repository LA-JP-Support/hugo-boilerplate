import json
from pathlib import Path

def cleanup_duplicates():
    json_path = Path('data/linkbuilding/ja_automatic.json')
    
    # 削除対象のキーワード（手動設定 ja.yaml と重複しているもの）
    target_keywords = ['Google DeepMind', 'DeepMind', 'Gemini', 'AlphaGo', 'AlphaZero', 'AI']
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict) and 'keywords' in data:
        items = data['keywords']
        is_dict_wrapper = True
    else:
        items = data
        is_dict_wrapper = False

    initial_count = len(items)
    
    # 手動設定と重複する、または不適切なエントリーを削除
    new_items = [
        item for item in items 
        if item.get('Keyword') not in target_keywords
    ]
    
    final_count = len(new_items)
    
    if initial_count != final_count:
        print(f"Removed {initial_count - final_count} duplicate/incorrect entries from ja_automatic.json")
        if is_dict_wrapper:
            data['keywords'] = new_items
            output_data = data
        else:
            output_data = new_items
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print("Successfully cleaned ja_automatic.json")
    else:
        print("No duplicates found in ja_automatic.json")

if __name__ == '__main__':
    cleanup_duplicates()

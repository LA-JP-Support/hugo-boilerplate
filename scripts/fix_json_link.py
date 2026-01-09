import json
from pathlib import Path

def fix_json():
    json_path = Path('data/linkbuilding/ja_automatic.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # data is expected to be {'keywords': [...]} based on file inspection
    if isinstance(data, dict) and 'keywords' in data:
        items = data['keywords']
        is_dict_wrapper = True
    elif isinstance(data, list):
        items = data
        is_dict_wrapper = False
    else:
        print("Unknown JSON structure")
        return

    initial_count = len(items)
    
    # Filter out the incorrect entry
    # Entry to remove: Keyword="AI", URL="/ja/glossary/Precision/"
    new_items = [
        item for item in items 
        if not (item.get('Keyword') == 'AI' and '/glossary/Precision/' in item.get('URL', ''))
    ]
    
    final_count = len(new_items)
    
    if initial_count != final_count:
        print(f"Removed {initial_count - final_count} incorrect entries.")
        
        if is_dict_wrapper:
            data['keywords'] = new_items
            output_data = data
        else:
            output_data = new_items
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print("Successfully updated ja_automatic.json")
    else:
        print("No matching entry found to remove.")

if __name__ == '__main__':
    fix_json()

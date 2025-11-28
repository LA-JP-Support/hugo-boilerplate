# Hugo-Boilerplate スクリプト詳細仕様書

## 📋 目次

1. [概要](#1-概要)
2. [ビルドプロセススクリプト](#2-ビルドプロセススクリプト)
3. [コンテンツ処理スクリプト](#3-コンテンツ処理スクリプト)
4. [翻訳関連スクリプト](#4-翻訳関連スクリプト)
5. [リンクビルディングスクリプト](#5-リンクビルディングスクリプト)
6. [画像処理スクリプト](#6-画像処理スクリプト)
7. [ユーティリティスクリプト](#7-ユーティリティスクリプト)

---

## 1. 概要

### スクリプトディレクトリ構造

```
scripts/
├── build_content.sh              # メインビルドスクリプト
├── convert_tooltip_syntax.py     # ツールチップ構文変換
├── extract_automatic_links.py    # 自動リンク抽出
├── find_duplicate_images.py      # 重複画像検出
├── generate_amplify_redirects_file.py # Amplifyリダイレクト生成
├── generate_content.py           # コンテンツ生成
├── generate_linkbuilding_keywords.py # キーワード生成
├── generate_related_content.py   # 関連コンテンツ生成
├── linkbuilding.py              # リンクビルディング（基本）
├── linkbuilding_parallel.py     # リンクビルディング（並列）
├── linkbuilding_config.json     # リンクビルディング設定
├── offload_replicate_images.py  # 画像オフロード
├── precompute_linkbuilding.py   # リンクビルディング最適化
├── preprocess-images.sh         # 画像前処理
├── requirements.txt             # Python依存関係
├── sync_content_attributes.py   # コンテンツ属性同期
├── sync_translation_urls.py     # 翻訳URL同期
├── sync_translations.py         # 翻訳同期
├── translate_with_flowhunt.py   # FlowHunt翻訳
├── translation-urls.py          # 翻訳URLマッピング
└── validate_tables.py          # テーブル検証
```

### Python依存関係 (requirements.txt)

```
beautifulsoup4==4.12.2
flowhunt==0.1.0
lxml==4.9.3
Pillow==10.0.0
python-dotenv==1.0.0
pyyaml==6.0.1
requests==2.31.0
tqdm==4.66.1
```

---

## 2. ビルドプロセススクリプト

### 2.1 build_content.sh

**目的**: コンテンツビルドプロセス全体を管理するマスタースクリプト

**主要機能:**
```bash
#!/bin/bash
set -e  # エラー時に即座に終了

# ディレクトリ設定
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
THEME_DIR="$(dirname "$SCRIPT_DIR")"
HUGO_ROOT="$(dirname "$(dirname "$THEME_DIR")")"

# Python仮想環境セットアップ
VENV_DIR="${SCRIPT_DIR}/.venv"
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    NEED_INSTALL=true
fi
source "${VENV_DIR}/bin/activate"
```

**実行可能ステップ:**

| ステップ名 | 説明 | 依存関係 |
|---------|------|---------|
| sync_translations | 翻訳キー同期 | なし |
| build_hugo | Hugoビルド | sync_translations |
| offload_images | 画像ダウンロード | なし |
| find_duplicate_images | 重複画像検出 | offload_images |
| translate | FlowHunt翻訳 | なし |
| sync_content_attributes | 属性同期 | translate |
| sync_translation_urls | URL同期 | sync_content_attributes |
| generate_amplify_redirects | リダイレクト生成 | sync_translation_urls |
| generate_linkbuilding_keywords | キーワード生成 | build_hugo |
| generate_related_content | 関連コンテンツ生成 | build_hugo |
| extract_automatic_links | リンク抽出 | なし |
| precompute_linkbuilding | リンク最適化 | build_hugo |
| apply_linkbuilding | リンク適用 | precompute_linkbuilding |
| preprocess_images | 画像最適化 | なし |

**実行例:**
```bash
# フルビルド
./scripts/build_content.sh

# 特定ステップのみ
./scripts/build_content.sh --step translate
./scripts/build_content.sh --step build_hugo,apply_linkbuilding

# 並列実行（言語ごと）
./scripts/build_content.sh --step generate_linkbuilding_keywords
```

---

## 3. コンテンツ処理スクリプト

### 3.1 convert_tooltip_syntax.py

**目的**: 旧形式のツールチップ構文を新しいHugoショートコード形式に変換

**クラス構造:**
```python
class TooltipConverter:
    def __init__(self, create_backup=True, verbose=True):
        self.create_backup = create_backup
        self.verbose = verbose
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'tooltips_converted': 0,
            'errors': 0
        }
    
    def convert_text(self, text):
        """テキスト内のツールチップパターンをショートコードに変換"""
        # パターン: **用語**（説明：詳細）
        PATTERN_BOLD = r'\*\*([^*]+)\*\*[（(]説明[：:]\s*([^)）]+)[)）]'
        # パターン: 用語（説明：詳細）
        PATTERN_NORMAL = r'([^\s（(]+)[（(]説明[：:]\s*([^)）]+)[)）]'
        
        # ショートコードに変換
        # {{< tooltip text="詳細" >}}用語{{< /tooltip >}}
```

**処理フロー:**
1. ファイル読み込み（UTF-8）
2. パターンマッチング（正規表現）
3. エスケープ処理（`"` → `&quot;`）
4. バックアップ作成（.bak）
5. 変換後ファイル保存

### 3.2 validate_tables.py

**目的**: Markdownテーブルの構文エラーを検出・修正

**検出する問題:**
```python
def check_table_headers(content):
    """テーブルヘッダーの問題を検出"""
    problems = []
    
    # パターン1: ヘッダー行の後に区切り線がない
    # | ヘッダー1 | ヘッダー2 |
    # （区切り線なし）
    
    # パターン2: セル内の改行
    # | 複数行\nテキスト |
    
    return problems

def fix_table_headers(content):
    """テーブルヘッダーを修正"""
    # 区切り線の自動生成
    # | col1 | col2 | col3 |
    # |------|------|------|  ← 自動生成
```

### 3.3 generate_related_content.py

**目的**: コンテンツの関連性を分析し、関連記事のリンクを生成

**アルゴリズム:**
```python
def calculate_similarity(content1, content2):
    """コンテンツの類似度を計算"""
    # 1. TF-IDF ベクトル化
    # 2. コサイン類似度計算
    # 3. キーワードマッチング
    # 4. カテゴリ・タグ重み付け
    
def find_related_content(target_file, all_files, max_related=5):
    """関連コンテンツを検索"""
    similarities = []
    for file in all_files:
        if file != target_file:
            score = calculate_similarity(target_file, file)
            similarities.append((file, score))
    
    # スコア順にソートして上位を返す
    return sorted(similarities, key=lambda x: x[1], reverse=True)[:max_related]
```

---

## 4. 翻訳関連スクリプト

### 4.1 translate_with_flowhunt.py

**目的**: FlowHunt APIを使用した自動多言語翻訳

**API統合:**
```python
import flowhunt
from dotenv import load_dotenv

class FlowHuntTranslator:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('FLOWHUNT_API_KEY')
        self.flow_id = "flowhunt-flow-translate"
        self.client = flowhunt.Client(api_key=self.api_key)
    
    def translate_content(self, content, source_lang='en', target_lang='ja'):
        """コンテンツを翻訳"""
        # フロントマターとコンテンツを分離
        frontmatter, body = self.split_content(content)
        
        # フロントマターの選択的翻訳
        translated_frontmatter = self.translate_frontmatter(
            frontmatter, target_lang
        )
        
        # 本文の翻訳（ショートコード保護）
        translated_body = self.translate_body_safe(body, target_lang)
        
        return self.merge_content(translated_frontmatter, translated_body)
```

**サポート言語:**
```python
SUPPORTED_LANGUAGES = {
    'ja': 'Japanese',
    'zh': 'Chinese',
    'ko': 'Korean',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ar': 'Arabic',
    # ... 20+ languages
}
```

### 4.2 sync_translations.py

**目的**: 翻訳ファイル間でキーの一貫性を保証

```python
def sync_translation_keys():
    """すべての言語ファイルで翻訳キーを同期"""
    languages = ['ja', 'en', 'zh', 'ko', ...]
    
    # マスターキーセットを作成
    all_keys = set()
    for lang in languages:
        keys = extract_keys(f'i18n/{lang}.yaml')
        all_keys.update(keys)
    
    # 各言語ファイルに欠落キーを追加
    for lang in languages:
        add_missing_keys(f'i18n/{lang}.yaml', all_keys)
```

### 4.3 sync_translation_urls.py

**目的**: 多言語サイトのURL構造を同期

```python
def generate_translation_urls(hugo_root):
    """翻訳URL マッピングを生成"""
    url_mapping = {}
    
    for content_file in find_content_files(hugo_root):
        translation_key = extract_translation_key(content_file)
        if translation_key:
            lang = extract_language(content_file)
            url = generate_url(content_file, lang)
            
            if translation_key not in url_mapping:
                url_mapping[translation_key] = {}
            url_mapping[translation_key][lang] = url
    
    return url_mapping
```

---

## 5. リンクビルディングスクリプト

### 5.1 linkbuilding.py

**目的**: コンテンツ内に自動的に内部リンクを挿入

**データ構造:**
```python
@dataclass
class Keyword:
    """リンク化するキーワード"""
    keyword: str
    url: str
    title: str = ""
    priority: int = 0
    exact_match: bool = False

@dataclass
class LinkConfig:
    """リンクビルディング設定"""
    max_replacements_per_keyword: int = 2
    max_replacements_per_url: int = 2
    max_links_on_page: int = 50
    max_replacements_per_page: int = 30
    min_chars_between_links: int = 1
    skip_existing_links: bool = True
```

**リンク挿入アルゴリズム:**
```python
def process_html_content(html, keywords, config):
    """HTMLコンテンツにリンクを挿入"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # テキストノードを処理
    for text_node in find_text_nodes(soup):
        if should_process_node(text_node):
            modified_text = apply_keywords(
                text_node.string, 
                keywords, 
                config
            )
            if modified_text != text_node.string:
                replace_node(text_node, modified_text)
    
    return str(soup)
```

### 5.2 linkbuilding_parallel.py

**目的**: 並列処理による高速リンクビルディング

```python
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def process_language(lang_code, config):
    """単一言語を処理"""
    html_files = find_html_files(f'public/{lang_code}')
    keywords = load_keywords(f'data/linkbuilding/{lang_code}.yaml')
    
    for html_file in html_files:
        process_file(html_file, keywords, config)

def main():
    """並列処理メイン"""
    max_workers = min(8, multiprocessing.cpu_count())
    languages = detect_languages('public')
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for lang in languages:
            future = executor.submit(process_language, lang, config)
            futures.append(future)
        
        # 結果を待機
        for future in futures:
            future.result()
```

### 5.3 precompute_linkbuilding.py

**目的**: 実際のコンテンツに基づいてキーワードを最適化

```python
def optimize_keywords(keywords, html_files):
    """使用されないキーワードを除外"""
    optimized = []
    
    for keyword in keywords:
        found = False
        for html_file in html_files:
            if keyword_exists_in_file(keyword, html_file):
                found = True
                break
        
        if found:
            optimized.append(keyword)
    
    return optimized

def generate_optimized_files(linkbuilding_dir, public_dir, output_dir):
    """最適化されたキーワードファイルを生成"""
    languages = detect_languages(linkbuilding_dir)
    
    for lang in languages:
        # スキップ条件（既存ファイルチェック）
        if should_skip_language(lang, output_dir):
            continue
        
        keywords = load_keywords(f'{linkbuilding_dir}/{lang}.yaml')
        html_files = find_html_files(f'{public_dir}/{lang}')
        
        optimized = optimize_keywords(keywords, html_files)
        save_optimized(optimized, f'{output_dir}/{lang}_optimized.json')
```

---

## 6. 画像処理スクリプト

### 6.1 preprocess-images.sh

**目的**: 画像の最適化とWebP変換

```bash
#!/bin/bash

process_image() {
    local input_file=$1
    local output_dir=$2
    
    # WebP変換
    cwebp -q 85 "$input_file" -o "${output_dir}/$(basename ${input_file%.*}).webp"
    
    # レスポンシブサイズ生成
    for size in 320 640 1024 1920; do
        convert "$input_file" -resize "${size}x>" \
            "${output_dir}/$(basename ${input_file%.*})-${size}w.jpg"
    done
}

process_all_images() {
    find static/images -type f \( -name "*.jpg" -o -name "*.png" \) | \
    while read image; do
        process_image "$image" "static/images/optimized"
    done
}
```

### 6.2 find_duplicate_images.py

**目的**: 重複画像を検出して報告

```python
import hashlib
from PIL import Image

def calculate_image_hash(image_path):
    """画像のハッシュ値を計算"""
    with Image.open(image_path) as img:
        # 画像を正規化（サイズ統一）
        img_resized = img.resize((128, 128))
        # ハッシュ計算
        return hashlib.md5(img_resized.tobytes()).hexdigest()

def find_duplicates(image_dir):
    """重複画像を検出"""
    hash_to_files = defaultdict(list)
    
    for image_file in find_image_files(image_dir):
        file_hash = calculate_image_hash(image_file)
        hash_to_files[file_hash].append(image_file)
    
    # 重複を抽出
    duplicates = {
        hash: files 
        for hash, files in hash_to_files.items() 
        if len(files) > 1
    }
    
    return duplicates
```

### 6.3 offload_replicate_images.py

**目的**: 外部サービスから画像をダウンロードしてローカル保存

```python
import requests
from urllib.parse import urlparse

def download_image(url, save_path):
    """画像をダウンロード"""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(8192):
            f.write(chunk)

def offload_replicate_images(content_dir, image_dir):
    """コンテンツ内の外部画像をローカル化"""
    for md_file in find_markdown_files(content_dir):
        content = read_file(md_file)
        
        # 外部画像URLを検出
        external_images = find_external_images(content)
        
        for image_url in external_images:
            # ローカルパスを生成
            local_path = generate_local_path(image_url, image_dir)
            
            # ダウンロード
            download_image(image_url, local_path)
            
            # コンテンツ内のURLを更新
            content = content.replace(image_url, local_path)
        
        # ファイルを更新
        write_file(md_file, content)
```

---

## 7. ユーティリティスクリプト

### 7.1 extract_automatic_links.py

**目的**: フロントマターのキーワードから自動リンクを抽出

```python
def extract_keywords_from_frontmatter(content):
    """フロントマターからキーワードを抽出"""
    frontmatter = parse_frontmatter(content)
    
    # 最初の2つのキーワードを使用
    keywords = frontmatter.get('keywords', [])[:2]
    
    return keywords

def generate_automatic_links(content_dir):
    """自動リンクデータを生成"""
    links = []
    
    for md_file in find_markdown_files(content_dir):
        keywords = extract_keywords_from_frontmatter(md_file)
        url = generate_url_from_file(md_file)
        
        for keyword in keywords:
            links.append({
                'keyword': keyword,
                'url': url,
                'priority': 1,
                'exact_match': False
            })
    
    return links
```

### 7.2 generate_amplify_redirects_file.py

**目的**: AWS Amplify用のリダイレクトルールを生成

```python
def generate_redirects(hugo_root):
    """リダイレクトルールを生成"""
    redirects = []
    
    # 言語リダイレクト
    redirects.append({
        "source": "/ja",
        "target": "/",
        "status": "301"
    })
    
    # 古いURLから新しいURLへ
    url_mappings = load_url_mappings('data/redirects.yaml')
    for old_url, new_url in url_mappings.items():
        redirects.append({
            "source": old_url,
            "target": new_url,
            "status": "301"
        })
    
    # 404ページ
    redirects.append({
        "source": "/<*>",
        "target": "/404.html",
        "status": "404"
    })
    
    return redirects

def save_redirects_json(redirects, output_path):
    """JSON形式で保存"""
    with open(output_path, 'w') as f:
        json.dump(redirects, f, indent=2)
```

### 7.3 generate_linkbuilding_keywords.py

**目的**: コンテンツからリンクビルディング用キーワードを自動生成

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

def extract_keywords_from_content(content_files, top_k=10):
    """TF-IDFを使用してキーワードを抽出"""
    
    # 全コンテンツを収集
    documents = []
    for file in content_files:
        content = read_markdown_content(file)
        documents.append(content)
    
    # TF-IDF計算
    vectorizer = TfidfVectorizer(
        max_features=100,
        ngram_range=(1, 3),
        stop_words=load_stop_words()
    )
    
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    
    # スコアでランク付け
    scores = tfidf_matrix.sum(axis=0).A1
    keyword_scores = list(zip(feature_names, scores))
    keyword_scores.sort(key=lambda x: x[1], reverse=True)
    
    return keyword_scores[:top_k]
```

---

## パフォーマンス最適化

### 並列処理戦略

```python
# CPU数に応じてワーカー数を調整
max_workers = min(
    8,  # 最大8ワーカー
    multiprocessing.cpu_count(),  # CPU数
    len(languages)  # 言語数
)

# メモリ使用量の監視
def monitor_memory():
    import psutil
    process = psutil.Process()
    memory_mb = process.memory_info().rss / 1024 / 1024
    if memory_mb > 2048:  # 2GB制限
        logger.warning(f"High memory usage: {memory_mb:.0f}MB")
```

### キャッシング戦略

```python
# ファイルベースキャッシュ
class FileCache:
    def __init__(self, cache_dir='.cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def get(self, key):
        cache_file = self.cache_dir / f"{key}.cache"
        if cache_file.exists():
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        return None
    
    def set(self, key, value):
        cache_file = self.cache_dir / f"{key}.cache"
        with open(cache_file, 'wb') as f:
            pickle.dump(value, f)
```

---

## エラーハンドリング

### 共通エラーハンドラー

```python
class ScriptError(Exception):
    """スクリプト実行エラー"""
    pass

def safe_execute(func):
    """デコレーターによる安全実行"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            if DEBUG:
                raise
            return None
    return wrapper
```

### ロギング設定

```python
import logging

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scripts.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

---

## 実行環境要件

### システム要件

- **OS**: macOS, Linux, WSL
- **Python**: 3.6以上
- **Node.js**: 14以上
- **Hugo**: 0.80以上
- **メモリ**: 4GB以上推奨
- **ディスク**: 10GB以上の空き容量

### 必須ツール

```bash
# インストール確認
python3 --version
node --version
hugo version
git --version

# 画像処理ツール
convert --version  # ImageMagick
cwebp -version     # WebP
```

---

## 更新履歴

- **2025-11-22**: 初版作成
- **2025-11-20**: 並列処理最適化
- **2025-11-19**: キャッシング機能追加

---

## 著作権・ライセンス

© 2025 SmartWeb/Interwork Corporation
License: GPL v2 or later

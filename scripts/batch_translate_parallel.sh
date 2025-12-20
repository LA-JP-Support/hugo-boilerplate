#!/bin/bash
# Parallel Translation Script for Glossary Articles (macOS互換版)
# 複数ファイルを並列翻訳

set -e

cd "$(dirname "$0")/.."

# APIキー確認
if [ -z "$ANTHROPIC_API_KEY" ]; then
    # export ANTHROPIC_API_KEY="your-api-key-here"  # Set this in your environment instead
fi

# 引数チェック
if [ $# -eq 0 ]; then
    echo "使用方法: $0 <file1.md> <file2.md> ... [max_workers]"
    echo ""
    echo "例："
    echo "  $0 HealthTech-Diagnosis.md HR-Talent-Acquisition.md"
    echo "  $0 *.md 8  # 全ファイル8並列"
    exit 1
fi

# 並列数を取得（最後の引数が数字なら並列数）
MAX_WORKERS=4
FILES=()

for arg in "$@"; do
    if [[ "$arg" =~ ^[0-9]+$ ]]; then
        MAX_WORKERS="$arg"
    else
        FILES+=("$arg")
    fi
done

if [ ${#FILES[@]} -eq 0 ]; then
    echo "❌ エラー: ファイルが指定されていません"
    exit 1
fi

echo "=========================================="
echo "🚀 並列翻訳開始"
echo "=========================================="
echo "ファイル数: ${#FILES[@]}"
echo "並列数: $MAX_WORKERS"
echo "=========================================="

# 並列処理（シンプルな方法）
count=0
pids=()

for file in "${FILES[@]}"; do
    echo "[開始] $file"
    
    # バックグラウンドで実行
    python3 scripts/translate_glossary_en_to_ja.py --one-file "$file" &
    pids+=($!)
    
    ((count++))
    
    # 並列数に達したら全完了を待つ
    if [ $count -ge $MAX_WORKERS ]; then
        echo "⏳ バッチ完了待ち..."
        for pid in "${pids[@]}"; do
            wait "$pid" 2>/dev/null || true
        done
        pids=()
        count=0
    fi
done

# 残りのプロセスを待つ
if [ ${#pids[@]} -gt 0 ]; then
    echo "⏳ 最終バッチ完了待ち..."
    for pid in "${pids[@]}"; do
        wait "$pid" 2>/dev/null || true
    done
fi

echo ""
echo "=========================================="
echo "✅ 全ファイル翻訳完了"
echo "=========================================="

#!/bin/bash
#
# Setup and test the enrichment system
#

echo "🔧 Setting up enrichment system..."

# Give execute permission to batch script
chmod +x scripts/batch_enrich.sh

echo "✅ Execute permissions set"
echo ""

# Test 1: Analyze tooltips
echo "📊 Test 1: Analyzing tooltips..."
python3 scripts/analyze_tooltips_vs_glossary.py --lang en

echo ""
echo "✅ Analysis complete! Check docs/tooltip_analysis_en.json"
echo ""

# Test 2: Dry run on single blog file
echo "🔍 Test 2: Dry run on single blog file..."
SAMPLE_BLOG="content/en/blog/ai-chatbot-types-guide.md"

if [ -f "$SAMPLE_BLOG" ]; then
    python3 scripts/enrich_glossary_blog.py "$SAMPLE_BLOG" --dry-run
    echo ""
    echo "✅ Dry run complete!"
else
    echo "⚠️  Sample blog file not found: $SAMPLE_BLOG"
fi

echo ""
echo "🎉 Setup and testing complete!"
echo ""
echo "📋 Next steps:"
echo "1. Review tooltip analysis: cat docs/tooltip_analysis_en.json | python3 -m json.tool"
echo "2. Run batch dry-run: ./scripts/batch_enrich.sh en --dry-run"
echo "3. If satisfied, run for real: ./scripts/batch_enrich.sh en"
echo ""

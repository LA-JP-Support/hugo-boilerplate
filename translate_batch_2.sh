#!/bin/bash
# 翻訳バッチ2 - 105件
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ANTHROPIC_API_KEY が設定されていません"
    exit 1
fi

echo "========================================"
echo "翻訳バッチ2 - 105件"
echo "========================================"
echo ""

TOTAL=105
COUNT=0

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Operational-Metrics.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Operational-Metrics.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Quality-Monitoring.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Quality-Monitoring.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Quality-Score.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Quality-Score.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Repeat-Contact-Rate.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Repeat-Contact-Rate.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Service-Recovery.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Service-Recovery.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Shrinkage.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Shrinkage.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Support-Capacity-Planning.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Support-Capacity-Planning.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Support-Metrics.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Support-Metrics.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Support-Optimization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Support-Optimization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Support-Team-Structure.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Support-Team-Structure.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Tiered-Support.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Tiered-Support.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Workforce-Optimization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Workforce-Optimization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Workload-Distribution.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Workload-Distribution.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Accessibility--Web-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Accessibility--Web-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Above-the-Fold.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Above-the-Fold.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Behavioral-Trigger.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Behavioral-Trigger.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Breadcrumb.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Breadcrumb.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Browser-Caching.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Browser-Caching.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] CLS--Cumulative-Layout-Shift-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "CLS--Cumulative-Layout-Shift-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Conversion-Path.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Conversion-Path.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Customer-Friction.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Customer-Friction.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Exit-Page.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Exit-Page.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Exit-Rate.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Exit-Rate.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] FCP--First-Contentful-Paint-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "FCP--First-Contentful-Paint-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Funnel-Visualization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Funnel-Visualization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Heatmap.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Heatmap.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Heatmap-Analysis.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Heatmap-Analysis.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Image-Compression.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Image-Compression.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Landing-Page.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Landing-Page.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Landing-Page-Optimization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Landing-Page-Optimization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Lazy-Loading.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Lazy-Loading.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] LCP--Largest-Contentful-Paint-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "LCP--Largest-Contentful-Paint-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Minification.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Minification.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Mobile-Optimization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Mobile-Optimization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Multivariate-Testing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Multivariate-Testing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Page-Load-Time.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Page-Load-Time.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Page-Value.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Page-Value.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Path-Analysis.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Path-Analysis.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Performance-Budget.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Performance-Budget.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Progressive-Web-App--PWA-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Progressive-Web-App--PWA-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Responsive-Design.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Responsive-Design.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Scroll-Depth.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Scroll-Depth.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Scroll-Map.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Scroll-Map.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Session-Recording.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Session-Recording.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Time-to-Interactive--TTI-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Time-to-Interactive--TTI-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] TTFB--Time-to-First-Byte-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "TTFB--Time-to-First-Byte-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] User-Engagement.md"
python scripts/translate_glossary_en_to_ja.py --one-file "User-Engagement.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] User-Experience--UX-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "User-Experience--UX-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] User-Flow.md"
python scripts/translate_glossary_en_to_ja.py --one-file "User-Flow.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] User-Path.md"
python scripts/translate_glossary_en_to_ja.py --one-file "User-Path.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] UX-Audit.md"
python scripts/translate_glossary_en_to_ja.py --one-file "UX-Audit.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Web-Accessibility-Standards.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Web-Accessibility-Standards.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Web-Performance.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Web-Performance.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Blogging-Best-Practices.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Blogging-Best-Practices.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Blogging-Frequency.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Blogging-Frequency.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Blogging-Platform.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Blogging-Platform.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Blogging-Strategy.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Blogging-Strategy.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Business-Blog.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Business-Blog.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Call-to-Action--CTA-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Call-to-Action--CTA-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Curation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Curation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Decay.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Decay.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Refresh.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Refresh.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Update-Strategy.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Update-Strategy.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Corporate-Blog.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Corporate-Blog.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Expert-Roundup.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Expert-Roundup.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Guest-Blogging.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Guest-Blogging.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Headline-Writing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Headline-Writing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hook.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hook.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Industry-Analysis.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Industry-Analysis.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Listicle.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Listicle.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Opinion-Piece.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Opinion-Piece.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Original-Research.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Original-Research.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Personal-Branding.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Personal-Branding.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] POV--Point-of-View-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "POV--Point-of-View-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Professional-Blogging.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Professional-Blogging.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Storytelling.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Storytelling.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Technical-Blog.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Technical-Blog.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Thought-Leadership-Content.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Thought-Leadership-Content.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Trending-Topics.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Trending-Topics.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Tutorial-Content.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Tutorial-Content.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Meta.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Meta.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] TikTok.md"
python scripts/translate_glossary_en_to_ja.py --one-file "TikTok.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] ByteDance.md"
python scripts/translate_glossary_en_to_ja.py --one-file "ByteDance.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] LinkedIn.md"
python scripts/translate_glossary_en_to_ja.py --one-file "LinkedIn.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Twitter-X.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Twitter-X.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] YouTube.md"
python scripts/translate_glossary_en_to_ja.py --one-file "YouTube.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] WhatsApp.md"
python scripts/translate_glossary_en_to_ja.py --one-file "WhatsApp.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Slack.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Slack.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Microsoft-Teams.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Microsoft-Teams.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Zoom.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Zoom.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Notion.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Notion.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Asana.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Asana.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Microsoft.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Microsoft.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Midjourney.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Midjourney.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Stability-AI.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Stability-AI.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Stable-Diffusion.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Stable-Diffusion.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Perplexity.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Perplexity.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] DALL-E.md"
python scripts/translate_glossary_en_to_ja.py --one-file "DALL-E.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] GitHub-Copilot.md"
python scripts/translate_glossary_en_to_ja.py --one-file "GitHub-Copilot.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Baidu.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Baidu.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Ernie-Bot.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Ernie-Bot.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Alibaba.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Alibaba.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Tongyi-Qianwen.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Tongyi-Qianwen.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Tencent.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Tencent.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] WeChat.md"
python scripts/translate_glossary_en_to_ja.py --one-file "WeChat.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

echo "========================================"
echo "✅ バッチ2完了"
echo "========================================"

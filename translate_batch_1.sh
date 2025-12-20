#!/bin/bash
# 翻訳バッチ1 - 104件
cd /Users/TM-MBP1/Documents/GitHub/hugo-boilerplate

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ANTHROPIC_API_KEY が設定されていません"
    exit 1
fi

echo "========================================"
echo "翻訳バッチ1 - 104件"
echo "========================================"
echo ""

TOTAL=104
COUNT=0

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Managed-Services.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Managed-Services.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Operational-Efficiency.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Operational-Efficiency.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Outsourcing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Outsourcing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Per-Seat-Pricing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Per-Seat-Pricing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Process-Automation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Process-Automation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Quick-Deployment.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Quick-Deployment.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Quick-Wins.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Quick-Wins.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Remote-Support.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Remote-Support.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] SaaS--Software-as-a-Service-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "SaaS--Software-as-a-Service-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Scalable-Pricing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Scalable-Pricing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Self-Service-Setup.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Self-Service-Setup.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] SMB--Small-and-Medium-Business-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "SMB--Small-and-Medium-Business-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] SMB-Digital-Transformation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "SMB-Digital-Transformation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] SMB-Technology-Stack.md"
python scripts/translate_glossary_en_to_ja.py --one-file "SMB-Technology-Stack.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Startup-Pricing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Startup-Pricing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Subscription-Model.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Subscription-Model.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Technology-Adoption.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Technology-Adoption.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Technology-Evaluation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Technology-Evaluation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Technology-Partner.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Technology-Partner.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Time-to-Implement.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Time-to-Implement.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Total-Cost-of-Ownership--TCO-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Total-Cost-of-Ownership--TCO-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Training-Resources.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Training-Resources.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Usage-Based-Pricing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Usage-Based-Pricing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] User-Friendly-Interface.md"
python scripts/translate_glossary_en_to_ja.py --one-file "User-Friendly-Interface.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Vendor-Comparison.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Vendor-Comparison.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Vendor-Selection.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Vendor-Selection.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Audience-Engagement.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Audience-Engagement.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Brand-Monitoring.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Brand-Monitoring.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Conversion-Tracking.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Conversion-Tracking.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Influencer-Marketing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Influencer-Marketing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Instagram-Shopping.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Instagram-Shopping.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Live-Commerce.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Live-Commerce.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Meta-Business-Suite.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Meta-Business-Suite.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Product-Catalog.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Product-Catalog.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Shoppable-Content.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Shoppable-Content.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Shoppable-Posts.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Shoppable-Posts.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Analytics.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Analytics.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Calendar.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Calendar.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Commerce.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Commerce.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-CRM.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-CRM.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Engagement-Rate.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Engagement-Rate.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Advertising.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Advertising.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-API.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-API.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Automation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Automation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Dashboard.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Dashboard.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Management.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Management.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Metrics.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Metrics.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Monitoring.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Monitoring.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Publishing.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Publishing.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-ROI.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-ROI.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Scheduling.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Scheduling.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Media-Strategy.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Media-Strategy.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Proof.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Proof.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Social-Selling.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Social-Selling.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] User-Review-Management.md"
python scripts/translate_glossary_en_to_ja.py --one-file "User-Review-Management.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Base-Template.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Base-Template.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Build-Automation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Build-Automation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Build-Performance.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Build-Performance.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] CI-CD-for-Static-Sites.md"
python scripts/translate_glossary_en_to_ja.py --one-file "CI-CD-for-Static-Sites.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Collection.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Collection.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Front-Matter.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Front-Matter.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Content-Type.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Content-Type.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Data-Files.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Data-Files.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Deploy-Preview.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Deploy-Preview.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Edge-Function.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Edge-Function.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Git-Based-CMS.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Git-Based-CMS.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Go-Templates.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Go-Templates.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo-Configuration.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo-Configuration.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo-Module.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo-Module.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo-Pipes.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo-Pipes.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo-Shortcode.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo-Shortcode.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo-Taxonomy.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo-Taxonomy.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Hugo-Theme.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Hugo-Theme.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] i18n.md"
python scripts/translate_glossary_en_to_ja.py --one-file "i18n.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Incremental-Build.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Incremental-Build.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] List-Template.md"
python scripts/translate_glossary_en_to_ja.py --one-file "List-Template.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Multilingual-Site.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Multilingual-Site.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Page-Bundle.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Page-Bundle.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Pagination.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Pagination.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Partial-Template.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Partial-Template.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Section.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Section.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Single-Template.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Single-Template.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Static-Site-Generation.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Static-Site-Generation.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Static-Site-Generator.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Static-Site-Generator.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Template-Hierarchy.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Template-Hierarchy.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Template-Variable.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Template-Variable.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] TOML-YAML-JSON-Config.md"
python scripts/translate_glossary_en_to_ja.py --one-file "TOML-YAML-JSON-Config.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Burnout.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Burnout.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Efficiency.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Efficiency.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Performance.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Performance.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Productivity.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Productivity.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Schedule-Adherence.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Schedule-Adherence.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Training.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Training.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Agent-Utilization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Agent-Utilization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Automation-Rate.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Automation-Rate.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Average-Resolution-Time.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Average-Resolution-Time.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Contact-Deflection.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Contact-Deflection.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Cost-per-Contact.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Cost-per-Contact.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Escalation-Management.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Escalation-Management.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Escalation-Rate.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Escalation-Rate.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] First-Contact-Resolution--FCR-.md"
python scripts/translate_glossary_en_to_ja.py --one-file "First-Contact-Resolution--FCR-.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Knowledge-Utilization.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Knowledge-Utilization.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

COUNT=$((COUNT + 1))
echo "[$COUNT/$TOTAL] Macro.md"
python scripts/translate_glossary_en_to_ja.py --one-file "Macro.md"
if [ $? -eq 0 ]; then
    echo "✅ 完了"
else
    echo "❌ エラー"
fi
sleep 2
echo ""

echo "========================================"
echo "✅ バッチ1完了"
echo "========================================"

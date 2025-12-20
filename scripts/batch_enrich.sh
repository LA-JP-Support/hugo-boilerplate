#!/bin/bash
#
# Batch process glossary and blog enrichment
# 
# This script:
# 1. Analyzes tooltips vs glossary
# 2. Processes glossary files (adds internal links)
# 3. Processes blog files (converts tooltips + adds internal links)
#
# Usage:
#   ./scripts/batch_enrich.sh en          # English only
#   ./scripts/batch_enrich.sh ja          # Japanese only
#   ./scripts/batch_enrich.sh all         # Both languages
#   ./scripts/batch_enrich.sh en --dry-run  # Dry run

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Default language
LANG="${1:-en}"
shift || true

# Check for dry-run flag
DRY_RUN=""
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN="--dry-run"
    echo -e "${YELLOW}🔍 DRY RUN MODE${NC}"
fi

# Function to process a single language
process_language() {
    local lang=$1
    
    echo -e "\n${BLUE}${'='*60}${NC}"
    echo -e "${BLUE}Processing Language: ${lang^^}${NC}"
    echo -e "${BLUE}${'='*60}${NC}\n"
    
    # Step 1: Analyze tooltips
    echo -e "${GREEN}📊 Step 1: Analyzing tooltips vs glossary...${NC}"
    python3 scripts/analyze_tooltips_vs_glossary.py --lang "$lang"
    
    # Step 2: Enrich glossary
    echo -e "\n${GREEN}📚 Step 2: Enriching glossary files...${NC}"
    python3 scripts/enrich_glossary_blog.py "content/${lang}/glossary/" $DRY_RUN
    
    # Step 3: Enrich blog (with tooltip conversion)
    echo -e "\n${GREEN}📝 Step 3: Enriching blog files (converting tooltips)...${NC}"
    python3 scripts/enrich_glossary_blog.py "content/${lang}/blog/" --convert-tooltips $DRY_RUN
    
    echo -e "\n${GREEN}✅ Completed processing ${lang^^}${NC}\n"
}

# Main execution
case "$LANG" in
    "en")
        process_language "en"
        ;;
    "ja")
        process_language "ja"
        ;;
    "all")
        process_language "en"
        process_language "ja"
        ;;
    *)
        echo -e "${RED}❌ Unknown language: $LANG${NC}"
        echo "Usage: $0 [en|ja|all] [--dry-run]"
        exit 1
        ;;
esac

echo -e "${GREEN}${'='*60}${NC}"
echo -e "${GREEN}🎉 All processing complete!${NC}"
echo -e "${GREEN}${'='*60}${NC}"

# Show next steps
echo -e "\n${BLUE}📋 Next Steps:${NC}"
echo "1. Review the tooltip analysis reports in docs/"
echo "2. Check git diff to verify changes"
echo "3. Test the site locally with 'hugo server'"
echo "4. Commit and push if everything looks good"
echo ""

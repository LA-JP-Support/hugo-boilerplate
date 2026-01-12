#!/bin/bash

# Generate placeholder images for pillars section
# Requires ImageMagick to be installed

OUTPUT_DIR="/Users/TM-MBP1/Documents/GitHub/hugo-boilerplate/static/images/pillars"

# Image dimensions (matches 60% aspect ratio used in CSS)
WIDTH=1200
HEIGHT=720

echo "Generating placeholder images..."

# 1. email-automation.jpg - Blue/Purple gradient (communication theme)
magick -size ${WIDTH}x${HEIGHT} \
  gradient:'#4F46E5-#7C3AED' \
  -blur 0x20 \
  -gravity center \
  -font Helvetica -pointsize 48 -fill 'rgba(255,255,255,0.3)' \
  -annotate 0 'Email Automation' \
  -quality 85 \
  "${OUTPUT_DIR}/email-automation.jpg"
echo "✓ Created email-automation.jpg"

# 2. ai-answer-assistant.jpg - Teal/Cyan gradient (AI assistant theme)
magick -size ${WIDTH}x${HEIGHT} \
  gradient:'#0D9488-#06B6D4' \
  -blur 0x20 \
  -gravity center \
  -font Helvetica -pointsize 48 -fill 'rgba(255,255,255,0.3)' \
  -annotate 0 'AI Answer Assistant' \
  -quality 85 \
  "${OUTPUT_DIR}/ai-answer-assistant.jpg"
echo "✓ Created ai-answer-assistant.jpg"

# 3. ai-content.jpg - Green/Emerald gradient (content creation theme)
magick -size ${WIDTH}x${HEIGHT} \
  gradient:'#059669-#10B981' \
  -blur 0x20 \
  -gravity center \
  -font Helvetica -pointsize 48 -fill 'rgba(255,255,255,0.3)' \
  -annotate 0 'AI Content Creation' \
  -quality 85 \
  "${OUTPUT_DIR}/ai-content.jpg"
echo "✓ Created ai-content.jpg"

# 4. hugo-web.jpg - Pink/Rose gradient (web/Hugo theme)
magick -size ${WIDTH}x${HEIGHT} \
  gradient:'#DB2777-#F472B6' \
  -blur 0x20 \
  -gravity center \
  -font Helvetica -pointsize 48 -fill 'rgba(255,255,255,0.3)' \
  -annotate 0 'Hugo Web Development' \
  -quality 85 \
  "${OUTPUT_DIR}/hugo-web.jpg"
echo "✓ Created hugo-web.jpg"

echo ""
echo "Done! All placeholder images created in ${OUTPUT_DIR}"
ls -la "${OUTPUT_DIR}"

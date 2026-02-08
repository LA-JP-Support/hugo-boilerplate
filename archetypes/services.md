---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
description: ""
type: "services"
draft: true
translationKey: "{{ .File.ContentBaseName }}"

# Hero Section
badge: ""
hero_heading: ""
hero_description: ""

# CTAs
cta_primary:
  text: "無料相談を予約"
  url: "/ja/contact/"

# Introduction
introduction: ""

# Features (alternating layout sections)
features:
  - label: "機能1"
    title: "機能タイトル"
    description: "機能の説明文"
    image: "/images/services/{{ .File.ContentBaseName }}/feature-1.jpg"

  - label: "機能2"
    title: "機能タイトル"
    description: "機能の説明文"
    image: "/images/services/{{ .File.ContentBaseName }}/feature-2.jpg"

# Stats Section
stats_heading: "導入企業の実績"
stats_description: ""
stats:
  - value: ""
    label: ""
    description: ""

# CTA Section
cta_section:
  heading: "今すぐ始めませんか？"
  description: ""
  button_text: "無料相談を予約"
  button_url: "/ja/contact/"

# Related Services
related_services_heading: "その他のAIカスタマーサポート機能"
related_services_description: ""
---

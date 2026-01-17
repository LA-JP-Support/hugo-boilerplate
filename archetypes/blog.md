---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date.Format "2006-01-02" }}
lastmod: {{ .Date.Format "2006-01-02" }}
draft: true
translationKey: "{{ .File.ContentBaseName }}"
description: ""
keywords: []
image: ""
tags: []
categories: []
url: "blog/{{ .File.ContentBaseName }}/"
---

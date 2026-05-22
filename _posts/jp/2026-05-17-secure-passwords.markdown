---
layout: minimal-post
title: "ターミナルでローカルに安全なランダムパスワードを生成する"
summary: "手早く安全なパスワードが必要なときに"
icon: "/images/favicons/apps.png"
lang: jp
categories:
  - jp
---


# `/dev/random` のデータを `tr`（transliterate）コマンドで安全な文字セットに絞って生成する

記号なしの英数字24文字：
```
echo $(LC_ALL=C  tr -dc 'A-Za-z0-9' < /dev/random | head -c 24)
```

記号ありの英数字24文字：
```
echo $(LC_ALL=C  tr -dc 'A-Za-z0-9.!@^*_/' < /dev/random | head -c 24)
```

# OpenSSL の出力を base64 として生成する

```
openssl rand -base64 32
```



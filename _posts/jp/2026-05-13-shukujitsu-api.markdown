---
layout: minimal-post
title: "日本祝日API"
summary: "簡単なJSON形式を提供します"
icon: "/images/favicons/apps.png"
lang: jp
categories:
  - jp
---

# 祝日 API

**祝日API**を使えば、過去から未来までの日本の国民の祝日・休日に、1回のHTTPリクエストで即座にアクセスできます。認証不要・初期設定不要・無料。スケジュール管理アプリ、給与計算システム、カレンダー連携など、祝日リストを手動で管理する手間をなくして、このAPIにお任せください。

ベースURL: `https://shukujitsu.kaylee.jp`

---

## エンドポイント

### 全祝日の取得

```
GET /holidays/all
```

データセット内のすべての祝日を返します。日付範囲での絞り込みも可能です。

| クエリパラメータ | フォーマット | 説明 |
|---|---|---|
| `from` | `YYYY-MM-DD` | 指定日以降の祝日のみ取得 |
| `to` | `YYYY-MM-DD` | 指定日以前の祝日のみ取得 |

**例**

```bash
# すべての祝日を取得
curl https://shukujitsu.kaylee.jp/holidays/all

# 2025年上半期の祝日を取得
curl "https://shukujitsu.kaylee.jp/holidays/all?from=2025-01-01&to=2025-06-30"
```

---

### 年別祝日の取得

```
GET /holidays/year/:year
```

指定した年のすべての祝日を返します。

**例**

```bash
curl https://shukujitsu.kaylee.jp/holidays/year/2025
```

---

## レスポンス形式

すべてのエンドポイントは、祝日オブジェクトのJSON配列を返します。

```json
[
  {
    "date": "2025年1月1日",
    "date_en": "2025-01-01",
    "name": "元日",
    "name_en": "New Year's Day"
  },
  {
    "date": "2025年1月13日",
    "date_en": "2025-01-13",
    "name": "成人の日",
    "name_en": "Coming-of-Age Day"
  }
]
```

| フィールド | 説明 |
|---|---|
| `date` | 日本語形式の日付（`YYYY年M月D日`） |
| `date_en` | ISO 8601形式の日付（`YYYY-MM-DD`） |
| `name` | 祝日名（日本語） |
| `name_en` | 祝日名（英語、政府公式の日本法令外国語訳に準拠） |

---

## 使用例

**今日が祝日かどうか確認する（JavaScript）**

```js
const today = new Date().toISOString().slice(0, 10);
const res = await fetch(`https://shukujitsu.kaylee.jp/holidays/all?from=${today}&to=${today}`);
const holidays = await res.json();
if (holidays.length > 0) {
  console.log(`今日は${holidays[0].name}です！`);
}
```

**ある年の祝日を一覧取得する（Python）**

```python
import requests

holidays = requests.get("https://shukujitsu.kaylee.jp/holidays/year/2025").json()
for h in holidays:
    print(h["date"], h["name"])
```

---

## データについて

祝日データは内閣府が公開する公式データセットを直接参照しているため、法令の改正があっても常に正確で最新の情報をお届けします。

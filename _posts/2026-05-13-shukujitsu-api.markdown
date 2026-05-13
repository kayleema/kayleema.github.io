---
layout: minimal-post
title: "Japanese Holiday API"
summary: "Get Japanese Holiday Information in Nice Json Format"
icon: "/images/favicons/apps.png"
---

# Shukujitsu API

**Shukujitsu** gives you instant access to every Japanese national holiday, past and future, in a single HTTP request — no authentication, no setup, no fees. Whether you're building a scheduling app, a payroll system, or a calendar integration, stop hand-maintaining holiday lists and let this API do the work.

Base URL: `https://shukujitsu.kaylee.jp`

---

## Endpoints

### All holidays

```
GET /holidays/all
```

Returns every holiday in the dataset. Optionally filter by date range.

| Query param | Format | Description |
|---|---|---|
| `from` | `YYYY-MM-DD` | Only include holidays on or after this date |
| `to` | `YYYY-MM-DD` | Only include holidays on or before this date |

**Examples**

```bash
# All holidays ever
curl https://shukujitsu.kaylee.jp/holidays/all

# Holidays in the first half of 2025
curl "https://shukujitsu.kaylee.jp/holidays/all?from=2025-01-01&to=2025-06-30"
```

---

### Holidays by year

```
GET /holidays/year/:year
```

Returns all holidays for a specific year.

**Example**

```bash
curl https://shukujitsu.kaylee.jp/holidays/year/2025
```

---

## Response format

Every endpoint returns a JSON array of holiday objects:

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

| Field | Description |
|---|---|
| `date` | Date in Japanese format (`YYYY年M月D日`) |
| `date_en` | Date in ISO 8601 format (`YYYY-MM-DD`) |
| `name` | Holiday name in Japanese |
| `name_en` | Holiday name in English (per the official Japanese Law Translation) |

---

## Usage examples

**Check if today is a holiday (JavaScript)**

```js
const today = new Date().toISOString().slice(0, 10);
const res = await fetch(`https://shukujitsu.kaylee.jp/holidays/all?from=${today}&to=${today}`);
const holidays = await res.json();
if (holidays.length > 0) {
  console.log(`Today is ${holidays[0].name_en}!`);
}
```

**Get all holidays for a year (Python)**

```python
import requests

holidays = requests.get("https://shukujitsu.kaylee.jp/holidays/year/2025").json()
for h in holidays:
    print(h["date_en"], h["name_en"])
```

---

## Data source

Holiday data is sourced directly from the Japanese government's official public dataset, so it's always authoritative and up to date with any legislative changes.

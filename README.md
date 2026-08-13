# Up Garage Japan Used Car & Bike Parts Scraper

Scrape used car & motorcycle parts from **upgarage.com** (アップガレージ), Japan's largest used parts marketplace with 800,000+ items across 280+ nationwide stores. Extract part name, price, category hierarchy, condition, shop location and image — perfect for reseller arbitrage, market research, and cross-border parts sourcing.

> 🇯🇵 **Japanese used parts market data** — tires, wheels, car AV, tuning parts, bike gear, and more. Ideal for exporters and price comparison across JDM parts dealers.

## Output Sample

```json
{
  "itemId": "24545776",
  "title": "KYOHO(共豊) SMACK(スマック) VALKYRIE + KENDA(ケンダ) KR203",
  "shop": "アップガレージ 東近江店",
  "price": 65890,
  "imageUrl": "https://static.upgcf.com/img.php?w=&file_path=...",
  "detailUrl": "https://www.upgarage.com/ec/item/24545776/",
  "year": "2026",
  "category": "タイヤホイール",
  "subCategory": "17インチタイヤホイールセット",
  "vehicleType": "四輪",
  "condition": "20",
  "source": "upgarage"
}
```

## Input

| Field | Type | Description |
|-------|------|-------------|
| `searchKeyword` | string | Part or vehicle name (e.g. `ホイール`, `マフラー`). Empty = scan all |
| `maxItems` | integer | Max items to fetch (default 100) |
| `maxPages` | integer | Max pages to crawl, 20 items/page (default 5) |
| `statsMode` | boolean | Return price statistics instead of raw listings |
| `statsKeyword` | string | Part name to aggregate price stats for |
| `proxyConfiguration` | object | Apify proxy (auto by default) |

## Use Cases

- **Parts exporters** — source JDM used wheels, tires, tuning parts for overseas resale
- **Reseller arbitrage** — compare JDM parts prices across dealers
- **Market research** — track model/part-specific price trends (use `statsMode`)
- **Price monitoring** — watch for deals on specific parts (e.g. `レカロ` seats)

## Pricing

Pay-per-event: small fee per result. Use `statsMode` to get aggregated price stats (min/max/avg/median) for a specific part in a single call.

## Limitations

- Requires Apify proxy (auto) — upgarage may block overseas datacenter IPs
- Default fetch is 100 items / 5 pages; raise `maxItems`/`maxPages` for more
- Japanese-language output (title/category/shop are in Japanese)

## FAQ

**Q: How do I search wheels?** Pass `searchKeyword: "ホイール"` (or any part/vehicle name).

**Q: How do I get price statistics?** Set `statsMode: true` and `statsKeyword: "ホイール"` to get count/min/max/avg/median.

## Changelog

- **0.1** — Initial release: keyword search, full part fields, stats mode.

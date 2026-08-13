import asyncio
import httpx

API_BASE_URL = "https://www.upgarage.com/service/api/v1/items"
DEFAULT_LIMIT = 20

async def fetch_page(client: httpx.AsyncClient, url: str):
    for attempt in range(3):
        try:
            resp = await client.get(url, follow_redirects=True)
            if resp.status_code == 200:
                resp.encoding = "utf-8"
                return resp.json()
            if resp.status_code == 429 or resp.status_code >= 500:
                await asyncio.sleep(2 ** attempt)
                continue
            return None
        except (httpx.HTTPError, OSError, ValueError):
            await asyncio.sleep(2 ** attempt)
            continue
    return None

def parse_page(data: dict):
    resources = data.get("resources", []) if isinstance(data, dict) else []
    results = []
    for r in resources:
        item_id = str(r.get("id")) if r.get("id") is not None else None
        name = r.get("name") or ""
        price = r.get("tax_included_price") or r.get("price")
        shop = r.get("shop_name") or ""
        detail_url = f"https://www.upgarage.com/ec/item/{item_id}/" if item_id else None
        results.append({
            "itemId": item_id,
            "title": name,
            "shop": shop,
            "price": price,
            "imageUrl": r.get("image_url"),
            "detailUrl": detail_url,
            "year": r.get("manufacture_year"),
            "category": r.get("d_bunrui_name"),
            "subCategory": r.get("s_bunrui_name"),
            "vehicleType": r.get("dd_bunrui_name"),
            "condition": r.get("condition"),
            "source": "upgarage",
        })
    return results

def list_page(base: str, page: int) -> str:
    limit = DEFAULT_LIMIT
    offset = (page - 1) * limit
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}limit={limit}&offset={offset}"

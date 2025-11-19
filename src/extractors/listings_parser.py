thonfrom bs4 import BeautifulSoup
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class ListingsParser:
 def __init__(self, selector_item: str, selector_detail: str):
 self.selector_item = selector_item
 self.selector_detail = selector_detail

 def parse(self, html: str) -> List[Dict]:
 soup = BeautifulSoup(html, "html.parser")
 elements = soup.select(self.selector_item)
 parsed = []

 for el in elements:
 title = el.get_text(strip=True)
 detail_el = el.select_one(self.selector_detail)
 detail_url = detail_el["href"] if detail_el else None

 parsed.append({
 "title": title,
 "detail_url": detail_url
 })

 logger.info(f"Parsed {len(parsed)} listings.")
 return parsed
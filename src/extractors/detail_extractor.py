thonimport requests
from bs4 import BeautifulSoup
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class DetailExtractor:
 def extract(self, url: str) -> Dict:
 try:
 response = requests.get(url, timeout=10)
 response.raise_for_status()
 except Exception as e:
 logger.error(f"Failed to fetch detail page: {url} | {e}")
 return {}

 soup = BeautifulSoup(response.text, "html.parser")

 # Example extraction logic; real selectors vary by site
 data = {
 "reference_id": soup.select_one("#ref") and soup.select_one("#ref").get_text(strip=True),
 "category": soup.select_one(".category") and soup.select_one(".category").get_text(strip=True),
 "agency": soup.select_one(".agency") and soup.select_one(".agency").get_text(strip=True),
 "description": soup.select_one(".description") and soup.select_one(".description").get_text(strip=True),
 "published_date": soup.select_one(".published") and soup.select_one(".published").get_text(strip=True),
 "status": soup.select_one(".status") and soup.select_one(".status").get_text(strip=True)
 }

 logger.info(f"Extracted details from: {url}")
 return data
thonimport logging
from typing import Generator
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PaginationHandler:
 def __init__(self, base_url: str, start_page: int = 1, max_pages: int = 1, page_param: str = "page"):
 self.base_url = base_url.rstrip("/")
 self.start_page = start_page
 self.max_pages = max_pages
 self.page_param = page_param

 def fetch_pages(self) -> Generator[str, None, None]:
 for page in range(self.start_page, self.start_page + self.max_pages):
 url = f"{self.base_url}?{self.page_param}={page}"
 logger.info(f"Fetching page: {url}")
 try:
 response = requests.get(url, timeout=10)
 response.raise_for_status()
 yield response.text
 except Exception as e:
 logger.error(f"Failed to fetch page {page}: {e}")
 continue
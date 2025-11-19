thonimport csv
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class CSVExporter:
 def export(self, records: List[Dict], output_path: str) -> None:
 if not records:
 logger.warning("No records to export.")
 return

 keys = records[0].keys()

 try:
 with open(output_path, "w", newline="", encoding="utf-8") as f:
 writer = csv.DictWriter(f, fieldnames=keys)
 writer.writeheader()
 writer.writerows(records)
 logger.info(f"Exported {len(records)} records to {output_path}")
 except Exception as e:
 logger.error(f"Failed to export CSV: {e}")
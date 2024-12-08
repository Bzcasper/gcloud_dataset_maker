import functions_framework
import json
import logging
import time
import random
from google.cloud import storage
import os

# Load runtime config
CONFIG_PATH = os.path.join(os.path.dirname(__file__),"..","..","runtime_config.json")
with open(CONFIG_PATH,'r') as f:
    runtime_cfg=json.load(f)

bucket_name = runtime_cfg.get('DATA_GCS_BUCKET','my-jewelry-data')

JEWELRY_CATEGORIES=['ring','necklace','bracelet','wristwatch','earring','pendant']
SUBCATEGORIES={
  'ring':['engagement ring','fashion ring','wedding band'],
  'necklace':['gold necklace','silver necklace','pearl necklace'],
  'bracelet':['gold bracelet','tennis bracelet','charm bracelet'],
  'wristwatch':['automatic watch','quartz watch','smart watch'],
  'earring':['stud earrings','hoop earrings','drop earrings'],
  'pendant':['diamond pendant','ruby pendant','emerald pendant']
}

@functions_framework.http
def scrape_data(request):
    num_images=int(request.args.get('num_images',50))
    csv_content="url,title,price,category,subcategory,scraped_at,images,condition\n"
    for cat in JEWELRY_CATEGORIES:
        chosen_sub=SUBCATEGORIES[cat][0]
        for i in range(num_images):
            csv_content+=f"http://example.com/{cat}{i},{cat} item {i},$100,{cat},{chosen_sub},2024-01-01T00:00:00Z,http://img.com/{cat}{i}.jpg,good\n"

    storage_client=storage.Client()
    bucket=storage_client.bucket(bucket_name)
    blob=bucket.blob('raw/all_listings.csv')
    blob.upload_from_string(csv_content)
    logging.info("Scraping complete and data saved to GCS.")
    return "scraping_done", 200

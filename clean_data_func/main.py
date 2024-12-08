import functions_framework
import json
import logging
from google.cloud import storage
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__),"..","..","runtime_config.json")
with open(CONFIG_PATH,'r') as f:
    runtime_cfg=json.load(f)

bucket_name=runtime_cfg.get('DATA_GCS_BUCKET','my-jewelry-data')

@functions_framework.http
def clean_data(request):
    storage_client=storage.Client()
    bucket=storage_client.bucket(bucket_name)
    raw_blob=bucket.blob('raw/all_listings.csv')
    raw_data=raw_blob.download_as_text()

    # Mock cleaning: same data as cleaned
    cleaned_data=raw_data

    # Save cleaned data
    cleaned_blob=bucket.blob('cleaned/cleaned_listings.csv')
    cleaned_blob.upload_from_string(cleaned_data)

    final_blob=bucket.blob('cleaned/final_listings_with_images.csv')
    final_blob.upload_from_string(cleaned_data)
    logging.info("Data cleaning complete and uploaded to GCS.")
    return "cleaning_done",200

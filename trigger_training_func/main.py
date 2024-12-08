import functions_framework
import json
import logging
import os
from google.cloud import aiplatform

CONFIG_PATH = os.path.join(os.path.dirname(__file__),"..","..","runtime_config.json")
with open(CONFIG_PATH,'r') as f:
    runtime_cfg=json.load(f)

@functions_framework.http
def trigger_training(request):
    project="YOUR_GCP_PROJECT"
    location="us-central1"
    aiplatform.init(project=project, location=location)

    job = aiplatform.CustomJob.from_local_script(
        display_name="jewelry-training-job",
        script_path="train_resnet50.py",
        container_uri="gcr.io/YOUR_GCP_PROJECT/jewelry-training:latest",
        requirements=["torch","transformers","deepspeed","peft","colorlog","requests","pillow","numpy"]
    )
    job.run()
    logging.info("Training triggered on Vertex AI.")
    return "training_started", 200

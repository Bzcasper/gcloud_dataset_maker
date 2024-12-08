import logging
import colorlog
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Default fallback configs
SCRAPING_CONFIG_DEFAULT = {
    'max_pages_per_category': 2,
    'delay_between_requests': 2.0,
    'timeout': 10,
    'max_retries': 3
}

RESNET_CONFIG_DEFAULT = {
    'batch_size': 4,
    'epochs': 1,
    'learning_rate': 0.001,
    'weight_decay': 0.01,
    'momentum': 0.9,
    'early_stopping_patience': 1
}

GPT2_CONFIG_DEFAULT = {
    'model_name': 'gpt2',
    'batch_size': 1,
    'epochs': 1,
    'learning_rate': 2e-5,
    'warmup_steps': 20,
    'max_length': 128,
    'temperature': 0.7,
    'top_p': 0.9,
    'lora_rank': 4
}

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = (
    "%(asctime)s "
    "%(log_color)s%(levelname)-8s%(reset)s "
    "%(cyan)s[%(name)s]%(reset)s "
    "%(message_log_color)s%(message)s%(reset)s"
)
LOG_COLORS = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white'
}
MESSAGE_COLORS = {
    'DEBUG': 'white',
    'INFO': 'white',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red'
}
formatter = colorlog.ColoredFormatter(
    LOG_FORMAT,
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors=LOG_COLORS,
    secondary_log_colors={'message': MESSAGE_COLORS}
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.root.setLevel(LOG_LEVEL)
logging.root.handlers = [handler]

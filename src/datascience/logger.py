import logging
import os
from datetime import datetime

# Create logs directory if not exists
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Timestamped log file
LOG_FILE = os.path.join(LOGS_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Logger config
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s : %(levelname)s : %(module)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # So logs show in terminal as well
    ]
)

logger = logging.getLogger("mlops-logger")

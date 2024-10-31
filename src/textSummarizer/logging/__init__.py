import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s : %(message)s]"
logging_dir = "logs"
logging_file = os.path.join(logging_dir, "running_logs.log")

# Ensure directory exists
try:
    os.makedirs(logging_dir, exist_ok=True)
except PermissionError as e:
    print(f"PermissionError while creating directory: {e}")
    sys.exit(1)

# Configure logging
try:
    logging.basicConfig(
        level=logging.INFO,
        format=logging_str,
        handlers=[
            logging.FileHandler(logging_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
except PermissionError as e:
    print(f"PermissionError while setting up logging: {e}")
    sys.exit(1)

logger = logging.getLogger("textSummarizerLogger")
logger.info("Logging setup complete.")

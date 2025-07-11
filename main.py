import logging
from google.cloud import logging as gcp_logging
import time

# Initialize Google Cloud Logging
client = gcp_logging.Client()
client.setup_logging()

# Python logger
logger = logging.getLogger("my-app")

def main():
    logger.info("Starting the script...")

    try:
        for i in range(5):
            logger.info(f"Processing iteration {i}")
            if i == 3:
                raise ValueError("Simulated error at i=3")
            time.sleep(1)
    except Exception as e:
        logger.exception("An error occurred")

    logger.info("Script finished")

if __name__ == "__main__":
    main()

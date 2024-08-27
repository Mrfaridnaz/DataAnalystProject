import logging

# Configure the logging
logging.basicConfig(
    filename='app.log',  # Log output will be saved to this file
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Date format for the log messages
)

# Create a logger object
logger = logging.getLogger(__name__)

# Log messages of various severity levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

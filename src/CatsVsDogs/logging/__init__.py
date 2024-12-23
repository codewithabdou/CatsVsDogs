import os
import sys
import logging
from pathlib import Path

# Get project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

# Set up logging configuration
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"
log_dir = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(log_dir, exist_ok=True)

# Create separate log files for all levels with absolute paths
info_filepath = os.path.join(log_dir, 'info.log')
error_filepath = os.path.join(log_dir, 'error.log')
debug_filepath = os.path.join(log_dir, 'debug.log')
warning_filepath = os.path.join(log_dir, 'warning.log')
critical_filepath = os.path.join(log_dir, 'critical.log')


# Create logger instance
logger = logging.getLogger("CatsVsDogsLogger")
logger.setLevel(logging.DEBUG)  # Set to lowest level to catch all logs

# Remove any existing handlers
if logger.handlers:
    logger.handlers.clear()

# Create formatters
formatter = logging.Formatter(logging_str)

# Create handlers for all logging levels
info_handler = logging.FileHandler(info_filepath, mode='a', encoding='utf-8')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

error_handler = logging.FileHandler(error_filepath, mode='a', encoding='utf-8')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

debug_handler = logging.FileHandler(debug_filepath, mode='a', encoding='utf-8')
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

warning_handler = logging.FileHandler(warning_filepath, mode='a', encoding='utf-8')
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)

critical_handler = logging.FileHandler(critical_filepath, mode='a', encoding='utf-8')
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(formatter)

# Create console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add all handlers to logger
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(debug_handler)
logger.addHandler(warning_handler)
logger.addHandler(critical_handler)
logger.addHandler(console_handler)

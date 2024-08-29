import logging

logging.basicConfig(filename='network_performance.log', level=logging.INFO)

def log_info(message):
    """Log an info message."""
    logging.info(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)

if __name__ == "__main__":
    # Example usage
    log_info('Network performance tool started.')
    log_error('An error occurred.')
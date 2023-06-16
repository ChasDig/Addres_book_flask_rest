import logging
from python_logging_rabbitmq import RabbitMQHandler
from pythonjsonlogger import jsonlogger

HOST, PORT = "localhost", 5672


def rabbitmq_logging(func):
    def start_logging(*args, **kwargs):
        logger = logging.getLogger()
        log_handler = RabbitMQHandler(host=HOST, port=PORT, exchange="logs")
        formatter = jsonlogger.JsonFormatter(
            "%(asctime) %(levelname) %(module) %(funcName) %(lineno) %(message)s",
            json_indent=4,
            json_ensure_ascii=False,
            json_default=str,
        )
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)
        result = func(*args, **kwargs)
        logger.removeHandler(log_handler)
        return result
    return start_logging

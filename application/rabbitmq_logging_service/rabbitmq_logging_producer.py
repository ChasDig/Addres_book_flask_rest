import logging
from python_logging_rabbitmq import RabbitMQHandler
from pythonjsonlogger import jsonlogger


def rabbitmq_logging(func):
    def start_logging(*args, **kwargs):
        result = func(*args, **kwargs)
        logger = logging.getLogger()
        log_handler = RabbitMQHandler(host='localhost', exchange="logs")
        formatter = jsonlogger.JsonFormatter(
            "%(asctime) %(levelname) %(module) %(funcName) %(lineno) %(message)s",
            json_indent=4,
            json_ensure_ascii=False,
            json_default=str,
        )
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)
        return result
    return start_logging

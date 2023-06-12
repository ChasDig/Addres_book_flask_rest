def start_logging():
    import logging
    from pythonjsonlogger import jsonlogger

    logger = logging.getLogger()
    log_handler = logging.FileHandler("app_logger.json")
    formatter = jsonlogger.JsonFormatter(
        "%(asctime) %(levelname) %(module) %(funcName) %(lineno) %(message)s",
        json_indent=4,
        json_ensure_ascii=False,
        json_default=str,
    )
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

from application.config import config
from application.service import create_application


app = create_application(config)

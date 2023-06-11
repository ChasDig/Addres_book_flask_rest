from application.dao import UsersDAO, PhonesDAO, EmailsDAO
from application.services import UsersServices, PhonesService, EmailServices
from application.setup.db import db

users_dao = UsersDAO(db_session=db.session)
phone_dao = PhonesDAO(db_session=db.session)
email_dao = EmailsDAO(db_session=db.session)

users_service = UsersServices(dao=users_dao)
phone_service = PhonesService(dao=phone_dao)
email_service = EmailServices(dao=email_dao)

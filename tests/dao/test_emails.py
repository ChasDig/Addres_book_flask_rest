import pytest

from application.dao.models import Emails
from application.dao import EmailsDAO

DATA_EMAIL = [
    {
        "user_id": 1,
        "name_email": "test_email_3@gmail.com",
        "view": "Личная",
    },
]


class TestEmailsDAO:

    @pytest.fixture()
    def emails_dao(self, db):
        return EmailsDAO(db_session=db.session)

    @pytest.fixture()
    def email_1(self, db):
        email = Emails(user_id=1, name_email="test_email_1@gmail.com", view="Рабочая")
        db.session.add(email)
        db.session.commit()
        return email

    @pytest.fixture()
    def email_2(self, db):
        email = Emails(user_id=2, name_email="test_email_2@gmail.com", view="Личная")
        db.session.add(email)
        db.session.commit()
        return email

    def test_get_email_by_id(self, emails_dao, email_1):
        assert emails_dao.get_email_by_id(email_id=1) == email_1

    def test_get_all_emails(self, emails_dao, email_1, email_2):
        assert emails_dao.get_all_emails() == [email_1, email_2]

    def test_delete_email(self, emails_dao, email_1):
        assert emails_dao.delete_email(email_id=email_1.id) == f"Delete object with id={email_1.id}"

    @pytest.mark.parametrize("data_json_create", DATA_EMAIL)
    def test_create_email(self, emails_dao, data_json_create):
        new_email = emails_dao.create_email(data_json=data_json_create)
        assert type(new_email) == Emails
        assert emails_dao.get_email_by_id(1) == new_email
        assert new_email.id == 1
        assert new_email.user_id == 1
        assert new_email.name_email == "test_email_3@gmail.com"
        assert new_email.view == "Личная"

    @pytest.mark.parametrize("data_json_update", DATA_EMAIL)
    def test_update_email(self, emails_dao, email_1, data_json_update):
        update_email = emails_dao.update_email(email_id=email_1.id, data_json=data_json_update)
        assert type(update_email) == Emails
        assert emails_dao.get_email_by_id(email_id=email_1.id) == update_email
        assert update_email.id == 1
        assert update_email.user_id == 1
        assert update_email.name_email == "test_email_3@gmail.com"
        assert update_email.view == "Личная"

    def test_order_emails(self, emails_dao, email_1, email_2):
        assert emails_dao.order_emails(sort_values="user_id", reverse=False) == [email_1, email_2]
        assert emails_dao.order_emails(sort_values="user_id", reverse=True) == [email_2, email_1]
        assert emails_dao.order_emails(sort_values="name_email", reverse=False) == [email_1, email_2]
        assert emails_dao.order_emails(sort_values="name_email", reverse=True) == [email_2, email_1]
        assert emails_dao.order_emails(sort_values="view", reverse=False) == [email_2, email_1]
        assert emails_dao.order_emails(sort_values="view", reverse=True) == [email_1, email_2]

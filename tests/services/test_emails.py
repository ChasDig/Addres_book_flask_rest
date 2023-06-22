import pytest
from unittest.mock import patch

from application.dao.models import Emails
from application.services import EmailServices


class TestEmailServices:

    @pytest.fixture()
    @patch("application.dao.EmailsDAO")
    def dao_emails_mock(self, dao_mock):
        dao = dao_mock
        dao.get_email_by_id.return_value = Emails(user_id=1, name_email="test_email_1@gmail.com", view="Рабочая")
        dao.get_all_emails.return_value = [
            Emails(user_id=1, name_email="test_email_1@gmail.com", view="Рабочая"),
            Emails(user_id=2, name_email="test_email_2@gmail.com", view="Личная"),
        ]
        dao.delete_email.return_value = f"Delete object with id=1"
        return dao

    @pytest.fixture()
    def emails_services(self, dao_emails_mock):
        return EmailServices(dao=dao_emails_mock)

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

    def test_get_email_by_id(self, emails_services, dao_emails_mock, email_1):
        assert emails_services.get_email_by_id(email_id=1) == dao_emails_mock.get_email_by_id.return_value

    def test_get_all_emails(self, emails_services, dao_emails_mock, email_1, email_2):
        assert emails_services.get_all_emails() == dao_emails_mock.get_all_emails.return_value

    def test_delete_email(self, emails_services, dao_emails_mock, email_1):
        assert emails_services.delete_email(email_id=email_1.id) == dao_emails_mock.delete_email.return_value

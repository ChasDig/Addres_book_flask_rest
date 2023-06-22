import pytest

from application.dao.models import Emails

DATA_EMAIL = [
    {
        "id": 1,
        "user_id": 1,
        "name_email": "test_email_1@gmail.com",
        "view": "Рабочая",
    },
]

DATA_EMAIL_ALL = [
    [
        {
            "id": 1,
            "user_id": 1,
            "name_email": "test_email_1@gmail.com",
            "view": "Рабочая",
        },
        {
            "id": 2,
            "user_id": 2,
            "name_email": "test_email_2@gmail.com",
            "view": "Личная",
        },
    ],
]


class TestEmailsViews:

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

    @pytest.mark.parametrize("data_json_response", DATA_EMAIL)
    def test_get_email_by_id(self, client, email_1, data_json_response):
        response = client.post("/emails/1/")
        assert response.status_code == 200
        assert response.json == data_json_response

    @pytest.mark.parametrize("data_json_response", DATA_EMAIL_ALL)
    def test_get_all_emails(self, client, email_1, email_2, data_json_response):
        response = client.post("/emails/")
        assert response.status_code == 200
        assert response.json == data_json_response

    def test_delete_email(self, client, email_1):
        response = client.delete("/emails/1/")
        assert response.status_code == 200

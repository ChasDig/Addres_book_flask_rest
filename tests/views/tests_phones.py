import pytest

from application.dao.models import Phones

DATA_PHONES = [
    {
        "id": 1,
        "user_id": 1,
        "view": "Мобильный",
        "number": 88005553536,
    },
]

DATA_PHONES_ALL = [
    [
        {
            "id": 1,
            "user_id": 1,
            "view": "Мобильный",
            "number": 88005553536,
        },
        {
            "id": 2,
            "user_id": 2,
            "view": "Городской",
            "number": 88005553537,
        },
    ],
]


class TestPhonesViews:

    @pytest.fixture()
    def phone_1(self, db):
        phone = Phones(user_id=1, view="Мобильный", number="88005553536")
        db.session.add(phone)
        db.session.commit()
        return phone

    @pytest.fixture()
    def phone_2(self, db):
        phone = Phones(user_id=2, view="Городской", number="88005553537")
        db.session.add(phone)
        db.session.commit()
        return phone

    @pytest.mark.parametrize("data_json_response", DATA_PHONES)
    def test_get_phone_by_id(self, client, phone_1, data_json_response):
        response = client.post("/phones/1/")
        assert response.status_code == 200
        assert response.json == data_json_response

    @pytest.mark.parametrize("data_json_response", DATA_PHONES_ALL)
    def test_get_all_phones(self, client, phone_1, phone_2, data_json_response):
        response = client.post("/phones/")
        assert response.status_code == 200
        assert response.json == data_json_response

    def test_delete_phone(self, client, phone_1):
        response = client.delete("/phones/1/")
        assert response.status_code == 200

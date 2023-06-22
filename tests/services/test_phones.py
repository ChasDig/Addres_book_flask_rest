import pytest
from unittest.mock import patch

from application.dao.models import Phones
from application.services import PhonesService


class TestPhonesService:

    @pytest.fixture()
    @patch("application.dao.PhonesDAO")
    def dao_phones_mock(self, dao_mock):
        dao = dao_mock
        dao.get_phone_by_id.return_value = Phones(user_id=1, view="Мобильный", number="88005553536")
        dao.get_all_phones.return_value = [
            Phones(user_id=1, view="Мобильный", number="88005553536"),
            Phones(user_id=2, view="Городской", number="88005553537"),
        ]
        dao.delete_phone.return_value = f"Delete object with id=1"
        return dao

    @pytest.fixture()
    def phone_services(self, dao_phones_mock):
        return PhonesService(dao=dao_phones_mock)

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

    def test_get_phone_by_id(self, phone_services, dao_phones_mock, phone_1):
        assert phone_services.get_phone_by_id(phone_id=1) == dao_phones_mock.get_phone_by_id.return_value

    def test_get_all_phones(self, phone_services, dao_phones_mock, phone_1, phone_2):
        assert phone_services.get_all_phones() == dao_phones_mock.get_all_phones.return_value

    def test_delete_phone(self, phone_services, dao_phones_mock, phone_1):
        assert phone_services.delete_phone(phone_id=phone_1.id) == dao_phones_mock.delete_phone.return_value

import pytest

from application.dao.models import Phones
from application.dao import PhonesDAO

DATA_PHONE = [
    {
        "user_id": 1,
        "view": "Городской",
        "number": 88005553538,
    }
]


class TestPhonesDAO:

    @pytest.fixture()
    def phones_dao(self, db):
        return PhonesDAO(db_session=db.session)

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

    def test_get_phone_by_id(self, phones_dao, phone_1):
        assert phones_dao.get_phone_by_id(phone_id=1) == phone_1

    def test_get_all_phones(self, phones_dao, phone_1, phone_2):
        assert phones_dao.get_all_phones() == [phone_1, phone_2]

    def test_delete_phone(self, phones_dao, phone_1):
        assert phones_dao.delete_phone(phone_id=phone_1.id) == f"Delete object with id={phone_1.id}"

    @pytest.mark.parametrize("data_json_create", DATA_PHONE)
    def test_create_phone(self, phones_dao, data_json_create):
        new_phone = phones_dao.create_phone(data_json=data_json_create)
        assert type(new_phone) == Phones
        assert phones_dao.get_phone_by_id(phone_id=1) == new_phone
        assert new_phone.id == 1
        assert new_phone.user_id == 1
        assert new_phone.view == "Городской"
        assert new_phone.number == "88005553538"

    @pytest.mark.parametrize("data_json_update", DATA_PHONE)
    def test_update_phone(self, phones_dao, phone_1, data_json_update):
        update_phone = phones_dao.update_phone(phone_id=phone_1.id, data_json=data_json_update)
        assert type(update_phone) == Phones
        assert phones_dao.get_phone_by_id(phone_id=phone_1.id) == update_phone
        assert update_phone.id == 1
        assert update_phone.user_id == 1
        assert update_phone.view == "Городской"
        assert update_phone.number == "88005553538"

    def test_order_phones(self, phones_dao, phone_1, phone_2):
        assert phones_dao.order_phones(sort_values="user_id", reverse=False) == [phone_1, phone_2]
        assert phones_dao.order_phones(sort_values="user_id", reverse=True) == [phone_2, phone_1]
        assert phones_dao.order_phones(sort_values="view", reverse=False) == [phone_2, phone_1]
        assert phones_dao.order_phones(sort_values="view", reverse=True) == [phone_1, phone_2]
        assert phones_dao.order_phones(sort_values="number", reverse=False) == [phone_1, phone_2]
        assert phones_dao.order_phones(sort_values="number", reverse=True) == [phone_2, phone_1]
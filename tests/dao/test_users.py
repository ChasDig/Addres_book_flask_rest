import pytest
import datetime

from application.dao.models import Users
from application.dao import UsersDAO

DATA_USER = [
    {
        "username": "test_username_3",
        "user_images": "test_images_3.png",
        "sex": "female",
        "data_birth": "2003-03-03",
        "address": "test_address_3",
    },
]


class TestUsersDAO:

    @pytest.fixture()
    def users_dao(self, db):
        return UsersDAO(db_session=db.session)

    @pytest.fixture()
    def user_1(self, db):
        user = Users(
            username="test_username_1",
            user_images="test_images_1.png",
            sex="male",
            data_birth=datetime.date(year=2001, month=1, day=1),
            address="test_address_1",
        )
        db.session.add(user)
        db.session.commit()
        return user

    @pytest.fixture()
    def user_2(self, db):
        user = Users(
            username="test_username_2",
            user_images="test_images_2.png",
            sex="female",
            data_birth=datetime.date(year=2002, month=2, day=2),
            address="test_address_2",
        )
        db.session.add(user)
        db.session.commit()
        return user

    def test_get_user_by_id(self, users_dao, user_1):
        assert users_dao.get_user_by_id(user_id=1) == user_1

    def test_get_all_users(self, users_dao, user_1, user_2):
        assert users_dao.get_all_users() == [user_1, user_2]

    def test_delete_user(self, users_dao, user_1):
        assert users_dao.delete_user(user_id=user_1.id) == f"Delete object with id={user_1.id}"

    @pytest.mark.parametrize("data_json_create", DATA_USER)
    def test_create_user(self, users_dao, data_json_create):
        new_user = users_dao.create_user(data_json=data_json_create)
        assert type(new_user) == Users
        assert users_dao.get_user_by_id(user_id=new_user.id) == new_user
        assert new_user.id == 1
        assert new_user.username == "test_username_3"
        assert new_user.user_images == "test_images_3.png"
        assert new_user.sex == "female"
        assert new_user.data_birth == datetime.date(year=2003, month=3, day=3)
        assert new_user.address == "test_address_3"

    @pytest.mark.parametrize("data_json_update", DATA_USER)
    def test_update_user(self, users_dao, user_1, data_json_update):
        update_user = users_dao.update_user(user_id=user_1.id, data_json=data_json_update)
        assert type(update_user) == Users
        assert users_dao.get_user_by_id(user_id=update_user.id) == update_user
        assert update_user.id == 1
        assert update_user.username == "test_username_3"
        # assert update_user.user_images == "test_images_3.png"
        assert update_user.sex == "female"
        assert update_user.data_birth == datetime.date(year=2003, month=3, day=3)
        assert update_user.address == "test_address_3"

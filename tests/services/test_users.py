import pytest
import datetime
from unittest.mock import patch

from application.dao.models import Users
from application.services import UsersServices


class TestUsersServices:

    @pytest.fixture()
    @patch("application.dao.UsersDAO")
    def dao_users_mock(self, dao_mock):
        dao = dao_mock
        dao.get_user_by_id.return_value = Users(
            username="test_username_1",
            user_images="test_images_1.png",
            sex="male",
            data_birth=datetime.date(year=2001, month=1, day=1),
            address="test_address_1",
        )
        dao.get_all_users.return_value = [
            Users(
                username="test_username_1",
                user_images="test_images_1.png",
                sex="male",
                data_birth=datetime.date(year=2001, month=1, day=1),
                address="test_address_1",
            ),
            Users(
                username="test_username_2",
                user_images="test_images_2.png",
                sex="female",
                data_birth=datetime.date(year=2002, month=2, day=2),
                address="test_address_2",
            ),
        ]
        dao.delete_user.return_value = f"Delete object with id=1"
        return dao

    @pytest.fixture()
    def user_services(self, dao_users_mock):
        return UsersServices(dao=dao_users_mock)

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

    def test_get_user_by_id(self, user_services, dao_users_mock, user_1):
        assert user_services.get_user_by_id(user_id=1) == dao_users_mock.get_user_by_id.return_value

    def test_get_all_users(self, user_services, dao_users_mock, user_1, user_2):
        assert user_services.get_all_users() == dao_users_mock.get_all_users.return_value

    def test_delete_user(self, user_services, dao_users_mock, user_1):
        assert user_services.delete_user(user_id=user_1.id) == dao_users_mock.delete_user.return_value

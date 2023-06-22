import pytest
import datetime

from application.dao.models import Users

DATA_USERS = [
    {
        "id": 1,
        "username": "test_username_1",
        "user_images": "test_images_1.png",
        "sex": "male",
        "data_birth": "2001-01-01",
        "address": "test_address_1",
    },
]

DATA_USERS_ALL = [
    [
        {
            "id": 1,
            "username": "test_username_1",
            "user_images": "test_images_1.png",
            "sex": "male",
            "data_birth": "2001-01-01",
            "address": "test_address_1",
        },
        {
            "id": 2,
            "username": "test_username_2",
            "user_images": "test_images_2.png",
            "sex": "female",
            "data_birth": "2002-02-02",
            "address": "test_address_2",
        },
    ],
]


class TestUsersViews:

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

    @pytest.mark.parametrize("data_json_response", DATA_USERS)
    def test_get_user_by_id(self, client, user_1, data_json_response):
        response = client.post("/users/1/")
        assert response.status_code == 200
        assert response.json == data_json_response

    @pytest.mark.parametrize("data_json_response", DATA_USERS_ALL)
    def test_get_all_users(self, client, user_1, user_2, data_json_response):
        response = client.post("/users/")
        assert response.status_code == 200
        assert response.json == data_json_response

    def test_delete_user(self, client, user_1):
        response = client.delete("/users/1/")
        assert response.status_code == 200

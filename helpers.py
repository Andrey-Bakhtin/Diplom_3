import requests
from faker import Faker

from urls import URL


DEFAULT_TIMEOUT = 20
faker = Faker('ru_RU')

def generate_user_body():
    return {
        "email": f"{faker.user_name()}@yandex.ru",
        "password": faker.password(),
        "name": faker.user_name()
    }

class Users:

    @staticmethod
    def register():
        body = generate_user_body()
        response = requests.post(URL.CREATE_USER, json=body, timeout=DEFAULT_TIMEOUT)
        return response
    
    @staticmethod
    def delete(token):
        return requests.delete(URL.DELETE_USER, headers={"Authorization": token}, timeout=DEFAULT_TIMEOUT)

class Orders:

    @staticmethod
    def create_order(body, token):
        return requests.post(url=URL.CREATE_ORDER, json=body, headers={'Authorization': token}, timeout=DEFAULT_TIMEOUT)

    @classmethod
    def create_for_user(cls, response):
        token = response.json()["accessToken"]
        body = DataForOrder.VALID_INGREDIENTS
        return cls.create_order(body, token)


class DataForOrder:
    
    VALID_INGREDIENTS = { 
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", 
                    "61c0c5a71d1f82001bdaaa6f"] 
    }

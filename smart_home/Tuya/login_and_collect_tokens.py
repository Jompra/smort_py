from dotenv import load_dotenv
import requests as r
import os

load_dotenv()

USER_NAME = os.getenv("TUYA_USERNAME")
PASSWORD = os.getenv("TUYA_PASSWORD")
COUNTRY = os.getenv("TUYA_COUNTRYCODE")
BASE_URL = "https://px1.tuyaeu.com/homeassistant/auth.do"

FORM_DATA = {
    "userName": USER_NAME,
    "password": PASSWORD,
    "countryCode": COUNTRY,
    "bizType": "smart_life",
    "from": "tuya",
}


def get_initial_login_token():
    return r.post(BASE_URL, FORM_DATA)


print(get_initial_login_token().json())

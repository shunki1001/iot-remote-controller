# %%
import base64
import hashlib
import hmac
import os
import time
import uuid

import requests
from dotenv import load_dotenv

load_dotenv()


def request_switchbot(endpoint: str, method: str, data: dict):
    # Declare empty header dictionary
    apiHeader = {}
    # open token
    token = os.environ["TOKEN"]  # copy and paste from the SwitchBot app V6.14 or later
    # secret key
    secret = os.environ[
        "SECRET"
    ]  # copy and paste from the SwitchBot app V6.14 or later
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")

    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )

    # Build api header JSON
    apiHeader["Authorization"] = token
    apiHeader["Content-Type"] = "application/json"
    apiHeader["charset"] = "utf8"
    apiHeader["t"] = str(t)
    apiHeader["sign"] = str(sign, "utf-8")
    apiHeader["nonce"] = str(nonce)

    host_domain = "https://api.switch-bot.com/v1.1/"
    if method == "GET":
        response = requests.get(url=f"{host_domain}{endpoint}", headers=apiHeader)
    elif method == "POST":
        response = requests.post(
            url=f"{host_domain}{endpoint}", json=data, headers=apiHeader
        )
    if response.status_code == 200:
        print(response.json())
        return " succeed"
    else:
        return "failed"

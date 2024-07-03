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


# %%
test = {
    "statusCode": 100,
    "body": {
        "deviceList": [
            {
                "deviceId": "6055F9412FEE",
                "deviceName": "プラグミニ",
                "deviceType": "Plug Mini (US)",
                "enableCloudService": True,
                "hubDeviceId": "",
            },
            {
                "deviceId": "CE5847B6B192",
                "deviceName": "カーテン 92",
                "deviceType": "Curtain3",
                "enableCloudService": True,
                "hubDeviceId": "FE67FD64F492",
                "calibrate": True,
                "master": True,
                "openDirection": "left",
            },
            {
                "deviceId": "DC0200CBED5E",
                "deviceName": "ボット 5E",
                "deviceType": "Bot",
                "enableCloudService": True,
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "F25F643BA816",
                "deviceName": "ハブミニ 16",
                "deviceType": "Hub Mini",
                "enableCloudService": True,
                "hubDeviceId": "000000000000",
            },
            {
                "deviceId": "F79A30E4B409",
                "deviceName": "温湿度計",
                "deviceType": "Meter",
                "enableCloudService": True,
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "FE67FD64F492",
                "deviceName": "Hub Mini 92",
                "deviceType": "Hub Mini",
                "enableCloudService": False,
                "hubDeviceId": "000000000000",
            },
        ],
        "infraredRemoteList": [
            {
                "deviceId": "01-202104122317-60784120",
                "deviceName": "テレビ",
                "remoteType": "DIY TV",
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "01-202209251043-23752078",
                "deviceName": "太陽",
                "remoteType": "Light",
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "02-202403312053-55169345",
                "deviceName": "ライト",
                "remoteType": "DIY Light",
                "hubDeviceId": "F25F643BA816",
            },
            {
                "deviceId": "02-202406211242-11769332",
                "deviceName": "扇風機",
                "remoteType": "DIY Fan",
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "02-202407022156-75534835",
                "deviceName": "エアコン",
                "remoteType": "Air Conditioner",
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "02-202407031551-15155646",
                "deviceName": "エアコンです",
                "remoteType": "DIY Air Conditioner",
                "hubDeviceId": "F25F643BA816",
            },
        ],
    },
    "message": "success",
}

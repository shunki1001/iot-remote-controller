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
        if response.status_code == 200:
            return response.json()
        else:
            return "failed"
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
                "deviceId": "C3323435656A",
                "deviceName": "リビング温度計",
                "deviceType": "Meter",
                "hubDeviceId": "000000000000",
            },
            {
                "deviceId": "CB3234354979",
                "deviceName": "温湿度計 79",
                "deviceType": "Meter",
                "hubDeviceId": "000000000000",
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
                "deviceId": "DDCC4E0C9819",
                "deviceName": "窓側",
                "deviceType": "Ceiling Light",
                "enableCloudService": True,
                "hubDeviceId": "000000000000",
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
                "deviceId": "FA9F0DC40257",
                "deviceName": "リモートボタン 57",
                "deviceType": "Remote",
                "enableCloudService": False,
                "hubDeviceId": "000000000000",
            },
            {
                "deviceId": "FE67FD64F492",
                "deviceName": "Hub Mini 92",
                "deviceType": "Hub Mini",
                "enableCloudService": False,
                "hubDeviceId": "000000000000",
            },
            {
                "deviceId": "FE8CB7E0D4C6",
                "deviceName": "キッチン側",
                "deviceType": "Ceiling Light",
                "enableCloudService": True,
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
                "deviceId": "02-202407290954-67648624",
                "deviceName": "エアコン寝室",
                "remoteType": "Others",
                "hubDeviceId": "F25F643BA816",
            },
            {
                "deviceId": "02-202407291012-25226595",
                "deviceName": "ハイセンス",
                "remoteType": "Others",
                "hubDeviceId": "FE67FD64F492",
            },
            {
                "deviceId": "02-202407310814-88239725",
                "deviceName": "ライト",
                "remoteType": "DIY Light",
                "hubDeviceId": "FE67FD64F492",
            },
        ],
    },
    "message": "success",
}

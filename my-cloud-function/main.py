import os
import time

from flask import Flask, jsonify
from flask_cors import CORS
from functions_wrapper import entrypoint

from functions import request_switchbot

app = Flask(__name__)
# CORSの追加
cors = CORS(app, resources={r"/*": {"origins": os.environ["CORS_URL"]}})


@app.route("/tv/on", methods=["GET"])
def tv_on():
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/01-202104122317-60784120/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "turnOn",
                        "commandType": "command",
                    },
                ),
                "action": "tv on",
            }
        ),
        200,
    )


@app.route("/living-ac/on", methods=["GET"])
def living_ac_on():
    # IoT デバイスを操作するコードをここに記述
    # return jsonify({"status": "success", "action": "light off"})
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/02-202407022156-75534835/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "turnOn",
                        "commandType": "command",
                    },
                ),
                "action": "living-ac/on",
            }
        ),
        200,
    )


@app.route("/living-ac/off", methods=["GET"])
def living_ac_off():
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/02-202407022156-75534835/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "turnOff",
                        "commandType": "command",
                    },
                ),
                "action": "living-ac/off",
            }
        ),
        200,
    )


@app.route("/desk-ac/on", methods=["GET"])
def desk_ac_on():
    # IoT デバイスを操作するコードをここに記述
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/02-202407291012-25226595/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "冷房25℃",
                        "commandType": "customize",
                    },
                ),
                "action": "desc-ac/on",
            }
        ),
        200,
    )


@app.route("/desk-ac/off", methods=["GET"])
def desk_ac_off():
    # IoT デバイスを操作するコードをここに記述
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/02-202407291012-25226595/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "OFF",
                        "commandType": "customize",
                    },
                ),
                "action": "desc-ac/off",
            }
        ),
        200,
    )


@app.route("/light/on", methods=["GET"])
def light_on():
    # IoT デバイスを操作するコードをここに記述
    request_switchbot(
        "devices/FE8CB7E0D4C6/commands",
        "POST",
        {
            "parameter": "default",
            "command": "turnOn",
            "commandType": "command",
        },
    )
    time.sleep(1)
    request_switchbot(
        "devices/02-202407310814-88239725/commands",
        "POST",
        {
            "parameter": "default",
            "command": "turnOn",
            "commandType": "command",
        },
    )
    time.sleep(1)
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/DDCC4E0C9819/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "turnOn",
                        "commandType": "command",
                    },
                ),
                "action": "light/on",
            }
        ),
        200,
    )


@app.route("/light/off", methods=["GET"])
def light_off():
    request_switchbot(
        "devices/FE8CB7E0D4C6/commands",
        "POST",
        {
            "parameter": "default",
            "command": "turnOff",
            "commandType": "command",
        },
    )
    time.sleep(1)
    request_switchbot(
        "devices/02-202407310814-88239725/commands",
        "POST",
        {
            "parameter": "default",
            "command": "turnOff",
            "commandType": "command",
        },
    )
    time.sleep(1)
    return (
        jsonify(
            {
                "status": request_switchbot(
                    "devices/DDCC4E0C9819/commands",
                    "POST",
                    {
                        "parameter": "default",
                        "command": "turnOff",
                        "commandType": "command",
                    },
                ),
                "action": "light/off",
            }
        ),
        200,
    )


@app.route("/thermo-sensor", methods=["GET"])
def thermo_sensor():
    # IoT デバイスを操作するコードをここに記述
    response_living = request_switchbot(
        "devices/C3323435656A/status",
        "GET",
        {},
    )
    response_desk = request_switchbot(
        "devices/CB3234354979/status",
        "GET",
        {},
    )
    response_bedroom = request_switchbot(
        "devices/F79A30E4B409/status",
        "GET",
        {},
    )
    state_response = [
        {
            "place": "living",
            "temperature": response_living["body"]["temperature"],
            "humidity": response_living["body"]["humidity"],
        },
        {
            "place": "desk",
            "temperature": response_desk["body"]["temperature"],
            "humidity": response_desk["body"]["humidity"],
        },
        {
            "place": "bedroom",
            "temperature": response_bedroom["body"]["temperature"],
            "humidity": response_bedroom["body"]["humidity"],
        },
    ]
    return (
        jsonify(
            {
                "status": state_response,
                "action": "thermo-sensor",
            }
        ),
        200,
    )


app_wrap = lambda request: entrypoint(app, request)

if __name__ == "__main__":
    app.run(debug=True)

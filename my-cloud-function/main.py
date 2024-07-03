import time

from flask import Flask, jsonify

from functions import request_switchbot

app = Flask(__name__)


@app.route("/tv/on", methods=["GET"])
def tv_on():
    return jsonify(
        {
            "status": request_switchbot(
                "devices/01-202104122317-60784120/commands",
                "POST",
                {"parameter": "default", "command": "turnOn", "commandType": "command"},
            ),
            "action": "light on",
        }
    )


@app.route("/living-ac/on", methods=["GET"])
def living_ac_on():
    # IoT デバイスを操作するコードをここに記述
    # return jsonify({"status": "success", "action": "light off"})
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202407022156-75534835/commands",
                "POST",
                {"parameter": "default", "command": "turnOn", "commandType": "command"},
            ),
            "action": "living-ac/on",
        }
    )


@app.route("/living-ac/off", methods=["GET"])
def living_ac_off():
    return jsonify(
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
    )


@app.route("/desk-ac/on", methods=["GET"])
def desk_ac_on():
    # IoT デバイスを操作するコードをここに記述
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202407031551-15155646/commands",
                "POST",
                {"parameter": "default", "command": "turnOn", "commandType": "command"},
            ),
            "action": "desc-ac/on",
        }
    )


@app.route("/desk-ac/off", methods=["GET"])
def desk_ac_off():
    # IoT デバイスを操作するコードをここに記述
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202407031551-15155646/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "turnOff",
                    "commandType": "command",
                },
            ),
            "action": "desc-ac/on",
        }
    )


@app.route("/living-light/on", methods=["GET"])
def living_light_on():
    # IoT デバイスを操作するコードをここに記述
    return jsonify(
        {
            "status": request_switchbot(
                "devices/01-202209251043-23752078/commands",
                "POST",
                {"parameter": "default", "command": "turnOn", "commandType": "command"},
            ),
            "action": "living-light/on",
        }
    )


@app.route("/living-light/off", methods=["GET"])
def living_light_off():
    return jsonify(
        {
            "status": request_switchbot(
                "devices/01-202209251043-23752078/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "turnOff",
                    "commandType": "command",
                },
            ),
            "action": "living-light/off",
        }
    )


@app.route("/living-light/dinner", methods=["GET"])
def living_light_dinner():
    return jsonify(
        {
            "status": request_switchbot(
                "devices/01-202209251043-23752078/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "dinner",
                    "commandType": "customize",
                },
            ),
            "action": "living-light/dinner",
        }
    )


@app.route("/living-light/lunch", methods=["GET"])
def living_light_lunch():
    return jsonify(
        {
            "status": request_switchbot(
                "devices/01-202209251043-23752078/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "lunch",
                    "commandType": "customize",
                },
            ),
            "action": "living-light/lunch",
        }
    )


@app.route("/desk-light/on", methods=["GET"])
def desk_light_on():
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202403312053-55169345/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "turnOn",
                    "commandType": "command",
                },
            ),
            "action": "desk-light/on",
        }
    )


@app.route("/desk-light/off", methods=["GET"])
def desk_light_off():
    request_switchbot(
        "devices/02-202403312053-55169345/commands",
        "POST",
        {
            "parameter": "default",
            "command": "turnOn",
            "commandType": "command",
        },
    )
    time.sleep(1)
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202403312053-55169345/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "turnOn",
                    "commandType": "command",
                },
            ),
            "action": "desk-light/off",
        }
    )


@app.route("/desk-light/brighten", methods=["GET"])
def desk_light_brighten():
    for _ in range(10):
        request_switchbot(
            "devices/02-202403312053-55169345/commands",
            "POST",
            {
                "parameter": "default",
                "command": "brightnessUp",
                "commandType": "command",
            },
        )
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202403312053-55169345/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "brightnessUp",
                    "commandType": "command",
                },
            ),
            "action": "desk-light/brighten",
        }
    )


@app.route("/desk-light/darken", methods=["GET"])
def desk_light_darken():
    for _ in range(10):
        request_switchbot(
            "devices/02-202403312053-55169345/commands",
            "POST",
            {
                "parameter": "default",
                "command": "brightnessDown",
                "commandType": "command",
            },
        )
    return jsonify(
        {
            "status": request_switchbot(
                "devices/02-202403312053-55169345/commands",
                "POST",
                {
                    "parameter": "default",
                    "command": "brightnessDown",
                    "commandType": "command",
                },
            ),
            "action": "desk-light/darken",
        }
    )


# 他のエンドポイントも同様に定義

if __name__ == "__main__":
    app.run(debug=True)

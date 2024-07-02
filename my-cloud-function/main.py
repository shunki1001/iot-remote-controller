from flask import Flask, jsonify

from functions import request_switchbot

app = Flask(__name__)


@app.route("/tv/on", methods=["GET"])
def tv_on():
    # IoT デバイスを操作するコードをここに記述
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
    return jsonify({"status": "success", "action": "light off"})


@app.route("/desk-ac/on", methods=["GET"])
def desk_ac_on():
    # IoT デバイスを操作するコードをここに記述
    return jsonify({"status": "success", "action": "door locked"})


@app.route("/living-light/on", methods=["GET"])
def living_light_on():
    # IoT デバイスを操作するコードをここに記述
    return jsonify({"status": "success", "action": "/living-light/on"})


@app.route("/living-light/off", methods=["GET"])
def living_light_off():
    # IoT デバイスを操作するコードをここに記述
    return jsonify({"status": "success", "action": "/living-light/off"})


# 他のエンドポイントも同様に定義

if __name__ == "__main__":
    app.run(debug=True)

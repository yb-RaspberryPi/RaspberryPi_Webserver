from model.led_db import LedDB   
from flask import Flask, render_template
import RPi.GPIO as GPIO                     # 추가
import config

app = Flask(__name__)
led_db = LedDB()
LED = config.LED_PIN                        # 추가

# LED 핀 준비 (test_led.py 와 같음)         # 추가
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

LED = {
        "red" = config.LED_RED,
        "blue" = config.LED_BLUE,
        "green" = config.LED_GREEN
 }

@app.route("/")
def home():
    return render_template("index.html")


# ───── 아래 두 라우트 추가 ─────
@app.route("/on", methods=["POST"])
def led_on():
    # LED를 켜고 "ok" 를 돌려줌. 실패하면 "fail"
    try:
        GPIO.output(config.LED_PIN, GPIO.HIGH)
        led_db.add(LED, 1)
        return "ok", 200
    except:
        return "fail", 500


@app.route("/off", methods=["POST"])
def led_off():
    # LED를 끄고 "ok" 를 돌려줌. 실패하면 "fail"
    try:
        GPIO.output(config.LED_PIN, GPIO.LOW)
        led_db.add(LED, 0)
        return "ok", 200
    except:
        return "fail", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)

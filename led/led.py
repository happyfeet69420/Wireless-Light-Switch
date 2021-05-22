from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
servo = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo,GPIO.OUT)

# {{url}}/led?status=on
@app.route('/', methods=['GET'])
def led():
    p=GPIO.PWM(servo,50)
    p.start(2.5)
    status = request.args.get('status')
    if status == "off":
        p.ChangeDutyCycle(2)
        time.sleep(0.5)
        p.ChangeDutyCycle(0)
        return jsonify({"message": "Lights succssfully turned off"})
    elif status == "on":
        p.ChangeDutyCycle(7)
        time.sleep(0.5)
        return jsonify({"message": "Lights succssfully turned off"})
    else:
        p.stop()
        GPIO.cleanup()
        return jsonify({"message": "Led succssfully turned off"})

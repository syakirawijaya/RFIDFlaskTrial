from flask import Flask, render_template, redirect, url_for
import serial

app = Flask(__name__)

# Set the correct serial port for your Arduino
ser = serial.Serial('COM16', 9600, timeout=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listen')
def listen_rfid():
    while True:
        if ser.in_waiting > 0:
            rfid_output = ser.readline().decode('utf-8').strip()
            if rfid_output == "RFID1_SUCCESS":
                return redirect(url_for('rfid1'))
            elif rfid_output == "RFID2_SUCCESS":
                return redirect(url_for('rfid2'))
            elif rfid_output == "RFID3_SUCCESS":
                return redirect(url_for('rfid3'))
            else:
                return "Scan Unsuccessful", 400

@app.route('/rfid1')
def rfid1():
    return render_template('rfid1.html')

@app.route('/rfid2')
def rfid2():
    return render_template('rfid2.html')

@app.route('/rfid3')
def rfid3():
    return render_template('rfid3.html')

if __name__ == '__main__':
    app.run(debug=True)

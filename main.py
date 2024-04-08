import serial
import time

SERIAL_PORT = 'COM20'  # veya COMx (Windows'ta)
BAUD_RATE = 9600

def servokontrol(command):
    try:
        serial_port = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Serial port '{SERIAL_PORT}' connected.")

        serial_port.write(command.encode())
        time.sleep(0.1)  # Opsiyonel bekleme süresi

        serial_port.close()
        print("Serial port closed.")
    except Exception as e:
        print(f"Error: {e}")

# Servo 1 için açı değeri gönder
servo1_aci = input("Servo 1 açı değerini girin (0-180): ")
servokontrol(f"S1:{servo1_aci}")

# Servo 2 için açı değeri gönder
servo2_aci = input("Servo 2 açı değerini girin (0-180): ")
servokontrol(f"S2:{servo2_aci}")

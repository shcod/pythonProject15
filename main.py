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



def servo_ayarla2(servo1_aci: int, servo2_aci: int):
    try:
        # Serial bağlantısını başlat
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as serial_port:
            print(f"Serial port '{SERIAL_PORT}' connected.")

            # Servo 1 için açı değerini gönder
            serial_port.write(f"S1:{servo1_aci}".encode())
            time.sleep(0.1)  # Opsiyonel bekleme süresi

            # Servo 2 için açı değerini gönder
            serial_port.write(f"S2:{servo2_aci}".encode())
            time.sleep(0.1)  # Opsiyonel bekleme süresi

        print("Servo angles set successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Örnek kullanım
servo_ayarla2(90, 45)  # Servo 1 için 90 derece, Servo 2 için 45 derece açı gönder

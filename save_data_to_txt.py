import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

with open("dane.txt", "a") as plik:
    while True:
        if ser.in_waiting > 0:
            linia = ser.readline().decode('utf-8').strip()
            print(linia)
            plik.write(linia + '\n')

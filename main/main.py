import serial

arduino = serial.Serial("COM3", 9600)

while True:
    message = arduino.readline().decode().strip()
    if message.startswith("+"):
        print(f"Button {message[1:]} pressed")
    else:
        print(f"Button {message[1:]} released")
    if "+7" in message: break

print("bye!")



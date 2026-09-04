import serial
import mido
from sys import exit

is_connected = False
for port_name in mido.get_output_names():
    if "arduino" in port_name:
        outport = mido.open_output(port_name)
        print(f"Connected to MIDI output port: {port_name}")
        is_connected = True
        break

if not is_connected:
    print("No MIDI output port found. Create a loopMIDI port named 'arduino'.")
    exit()

arduino = serial.Serial("COM3", 9600)

def send_pad_trigger(note_number, velocity=127):
    msg_on = mido.Message("note_on", note=note_number, velocity=velocity)
    outport.send(msg_on)

    msg_off = mido.Message("note_off", note=note_number, velocity=0)
    outport.send(msg_off)

    print(f"Note {midi_note_number} sent")

while True:
    message = arduino.readline().decode().strip()
    if message.startswith("+"):
        button_id = int(message[1:])
        midi_note_number = 36 + button_id
        send_pad_trigger(midi_note_number, 110)
        
    if "+7" in message: break

print("bye!")



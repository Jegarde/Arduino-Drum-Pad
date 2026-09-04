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

def trigger_button(note, is_pressed, velocity=127):
    msg = mido.Message("note_on" if is_pressed else "note_off", note=note, velocity=velocity)
    outport.send(msg)
    print(f"Note {midi_note_number} {'pressed' if is_pressed else 'released'}")

while True:
    message = arduino.readline().decode().strip()
    if message.startswith("+"):
        button_id = int(message[1:])
        midi_note_number = 36 + button_id
        trigger_button(midi_note_number, is_pressed=True, velocity=110)
    elif message.startswith("-"):
        button_id = int(message[1:])
        midi_note_number = 36 + button_id
        trigger_button(midi_note_number, is_pressed=False, velocity=0)


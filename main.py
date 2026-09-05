import serial
import mido
import tkinter as tk
import rtmidi
from sys import exit
from tkinter.messagebox import showinfo

# Change if the serial port doesn't match yours :)
ARDUINO_SERIAL_PORT = "COM3"

def connect_to_loop_midi():
    outport = None
    for port_name in mido.get_output_names():
        if "arduino" in port_name:
            outport = mido.open_output(port_name)
            print(f"Connected to MIDI output port: {port_name}")
            break

    return outport


def trigger_button(note, is_pressed, velocity=127):
    msg = mido.Message("note_on" if is_pressed else "note_off", note=note, velocity=velocity)
    try:
        outport.send(msg)
    except rtmidi.SystemError as e:
        showinfo("Oof!", "Failed to send MIDI message! Make sure the loopMIDI port is open and named 'arduino' and try again.")
        exit()
    print(f"Note {note} {'pressed' if is_pressed else 'released'}")


def set_button_state(button_id, is_pressed):
    if 0 <= button_id < len(buttons):
        buttons[button_id].configure(
            relief=tk.SUNKEN if is_pressed else tk.RAISED,
            bg="light blue" if is_pressed else "SystemButtonFace",
        )


def poll_arduino():
    # Arduino prints pressed notes in (+/-)[button_id] format. + means pressed, - means released.
    message = arduino.readline().decode(errors="replace").strip()

    is_pressed = None
    if message.startswith("+"):
        is_pressed = True
    elif message.startswith("-"):
        is_pressed = False

    if is_pressed is None:
        root.after(1, poll_arduino)
        return
    
    button_id = int(message[1:])
    midi_note_number = 36 + button_id
    set_button_state(button_id, is_pressed)
    trigger_button(midi_note_number, is_pressed)

    root.after(1, poll_arduino)


def close_application():
    arduino.close()
    root.destroy()

try:
    arduino = serial.Serial(ARDUINO_SERIAL_PORT, 9600, timeout=0.1)
except serial.SerialException:
    err_msg = f"Could not connect to Arduino on {ARDUINO_SERIAL_PORT}. Make sure the Arduino is connected and try again. Or change the serial port in the code to match yours!"
    showinfo("Oof!", err_msg)
    print(err_msg)
    exit()

outport = connect_to_loop_midi()
if not outport:
    err_msg = "No MIDI output port found. Create a loopMIDI port named 'arduino' and try again."
    showinfo("Oof!", err_msg)
    print(err_msg)
    exit()

root = tk.Tk()
root.title("Arduino Drum Pad")
buttons = []

for button_id in range(8):
    button = tk.Button(
        root,
        width=10,
        height=4,
        relief=tk.RAISED,
        bg="SystemButtonFace",
        state=tk.DISABLED
    )
    row = 8 - (button_id // 4) # Invert the row so it matches the drum rack layout
    button.grid(row=row, column=button_id % 4, padx=5, pady=5)
    buttons.append(button)


root.protocol("WM_DELETE_WINDOW", close_application)
root.after(1, poll_arduino)
root.resizable(False, False)
root.mainloop()
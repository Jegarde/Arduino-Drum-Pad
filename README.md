# Arduino Drum Pad
This is a simple 2x4 drum pad made using Arduino's starter pack parts! Made with Ableton Live in mind, hard coded for my needs. :)

## How
When a button is pressed or released, the Arduino communicates it to serial. The Python script listens to the serial, and sends the correct MIDI message to loopMIDI.
From www.tobias-erichsen.de/software/loopmidi.html: 
> This software can be used to create virtual loopback MIDI-ports to interconnect applications on Windows that want to open hardware-MIDI-ports for communication.

Essentially it allows me to create a virtual MIDI port in which I can send MIDI messages to, which a DAW like Ableton Live can listen to. This project was made with Ableton Live in mind, I don't know if it works with other DAWs.

## Why
I'm a broke SWE student who wants to get started in music production with a minimal budget. I had an Arduino starter pack lying around and this idea popped up after window shopping for a MIDI drum pad. 

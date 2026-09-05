# Arduino Drum Pad
This is a simple 2x4 drum pad made using Arduino's starter pack parts! Made with Ableton Live in mind, hard coded for my needs. :p

<img width="2100" height="907" alt="Illustration of the Arduino drum pad interacting with Ableton Live drum rack" src="https://github.com/user-attachments/assets/b83f5585-d5f2-49f6-9b6b-dcdece079876" />

Demo showcase: https://youtu.be/F0KimtX4SsA

## How
When a button is pressed or released, the Arduino communicates it to serial. The Python script listens to the serial, and sends the correct MIDI message to loopMIDI.
From www.tobias-erichsen.de/software/loopmidi.html: 
> This software can be used to create virtual loopback MIDI-ports to interconnect applications on Windows that want to open hardware-MIDI-ports for communication.

Essentially it allows me to create a virtual MIDI port in which I can send MIDI messages to, which a DAW like Ableton Live can listen to. This project was made with Ableton Live in mind, I don't know if it works with other DAWs. 

## Why
I'm a broke SWE student who wants to get started in music production with a minimal budget. I had an Arduino starter pack lying around and this idea popped up after window shopping for a MIDI drum pad. 

This project is made fully for my use and I won't provide instructions on how to set it up. I uploaded it here because I like sharing my projects. But if you're interested in building this yourself, I'd say it's easy enough to figure out on your own even as a beginner. I'm a beginner with electronics too! If anything, I hope this project inspires you to mess around with electronics too.

## AI Disclosure
This project was coded with organic vibes. No artificial vibes here! (as evident by the code.. :P)


<img width="307" height="284" alt="kuva" src="https://github.com/user-attachments/assets/7f6dec8a-e0e0-4e7a-b6bd-e336b42de374" />


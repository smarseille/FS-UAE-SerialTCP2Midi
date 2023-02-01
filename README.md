# FS-UAE-SerialTCP2Midi
SerialTCP2Midi interface for FS-UAE Serial

I created this to fill up a small gap for FS-UAE, as some games like Sierra games prefers Roland MT32 MIDI synthesizer.
FS-UAE before 4 can send raw MIDI commands via Serial. However, a lack of a program to process this and forward it to the synthersizer caused me to create this script.

## Binary
If you are looking for a binary as you do not use python or have python installed and want something that just works?
https://drive.google.com/file/d/1a-MKelnRg1cdS1xY5L1OYecFIgUuFyo0/view?usp=sharing

Go to Additional information for more information.

## Requirements:
mido
rtmidi

## Installation:

git clone this repo and install mido:
pip install mido 

install rtmidi:
pip install rtmidi

if this causes problem, try: 
pip install python-rtmidi

This may not work for everyone, in that case get a whl version corresponding to your python version here:
https://pypi.org/project/python-rtmidi/#files

Install it using:
pip install (filename).whl

Launch the script SerialTCP2Midi.py

## Additional information:
I am using loopmidi and munt to emulate the Roland MT32 under windows.

Download LoopMIDI: https://www.tobias-erichsen.de/software/loopmidi.html
After installing the application, open the application and add a new port. Once the new port is created, keep the application running.

Download munt: 
Windows: https://sourceforge.net/projects/munt/ (Github: https://github.com/munt/munt)
For linux there is also an ALSA version available.

After installing you will need ROMS, I cannot give you the mt32 roms unfortunately. Once you have gotten them by grabbing the roms of a real MT32, you can then setup the roms in rom selection under Options.

Make sure to take the correct version for CONTROL as well as PCM. (you cannot mix CM32L with MT32 roms).

After the roms is setup, go to Tools and click on New MIDI Port. There should be one that is called "loopMIDI Port" when you kept the default naming of LoopMIDI.

Now you can start launching SerialTCP2Midi, there will be a list of options presented, select the loopMIDI Port. It will then attempt connecting to 127.0.0.1 on 5004. 

Before launching a game that supports the MT32, set the following option in the fs-uae file:
serial_port = tcp://127.0.0.1:5004/

Once the emulator starts, SerialTCP2Midi will connect and start accepting all midi commands and forwards them.

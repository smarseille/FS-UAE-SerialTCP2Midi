"""
SerialTCP2Midi for FS-UAE
Copyright (c) 2022 SMarseille.
Github: @virtualmirai
Twitter: hug_marseille


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import socket
import mido
import re
import rtmidi

class Midi:
    def __init__(self):
        print("Initializing midi module...")
        self.device = False
        self.midiport = ""
        self.list = mido.get_output_names()
        self.parse = mido.Parser()
        print("Module ready.")

    def startup(self):
        for a,b in enumerate(self.list):
            print ("%i - %s" % (a,b))
        while self.device == False:
            sel = input("Enter number of device:")
            try:
                x = int(sel)
                try:
                    self.device = self.list[x]
                except:
                    print("Device out of range")
            except:
                print("Invalid value")
        self.midiport = mido.open_output(self.device)


class Listener:
    def __init__(self):
        print("FS-UAE SerialTCP2MIDI by SMarseille, 2022.")
        print("==========================================")
        self.port = 5004
        self.running = True


    def __client(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', self.port))
        print("Connected!")
        cnt = 0
        while True:
            cnt += 1
            if cnt == 100:
                for i in range(1,6,1):
                    msg = mido.Message('note_off', channel=i, note=0, velocity=0, time=0)
                    midi.midiport.send(msg)
                break
            try:
                data = self.sock.recv(2048)
            except ConnectionResetError:
                print("Connection reset error")
                break
            except Exception as e:
                print(e)
                break
            if data:
                cnt = 0
                bytearr = re.findall('..',data.hex())
                for i in bytearr:
                    y = int(i,16)
                    try:
                        midi.parse.feed_byte(y)
                        for message in midi.parse:
                            print(message)
                            midi.midiport.send(message)
                    except:
                        print(data.hex())
                        print(y)
                        print("Failed to feed, value to big?")

    def start_client(self):
        while True:
            try:
                self.__client()
            except Exception:
                for i in range(0,16,1):
                    msg = mido.Message('control_change', channel=i, control=123, value=0, time=0)
                    midi.midiport.send(msg)
                print("Unable to connect. Check if the FS-UAE instance is running and you have the following configured in the fs-uae config file of the game: \r\n"
                      "serial_port = tcp://127.0.0.1:5004/")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listener = Listener()
    midi = Midi()
    midi.startup()

    listener.start_client()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

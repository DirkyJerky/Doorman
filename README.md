# The Doorman

Using a Pi Pico to remotely unlock my front door.

## Requirements

- A Raspberry Pi Pico W
- Micropython (installed on the Pico)
- An interface to the wired door buzzer.  I used a relay, connected to the Pi's GPIO pins
- Some LEDs, to show status.  Connect to GPIO pins + ground through resistors.

## Installation

1. Copy the provided files under `./install/` to the Pi Pico W
2. Adjust the SSID + Password in `main.py` to connect to your prefered Wifi network
3. Adjust the pins in pins.py to match your connected peripherals.


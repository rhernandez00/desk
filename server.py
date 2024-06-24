# Raspberry Pi server that listens for POST requests to be used with a stream deck and AZ lights
# Possible commands: 
# up, down : brightness (l), red (r), green (g), blue (b) 
# Example commands: up_l (up brigthness), down_r (down red), up_g (up green), down_b (down blue)
# Author: Raul Hernandez, 16/06/2024

# Imports
from flask import Flask, request
import signal
import sys
import neopixel
import board

pixel_pin = board.D18 # The pin the NeoPixels are connected to
num_pixels = 24 # I'm using two 12 pixel strips
ORDER = neopixel.RGB

# Create a NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
# Define brightness, red, green and blue variables
brightness, red, green, blue = 0.2, 0, 0, 0
color_step = 5
brightness_step = 0.05

# Create a Flask app
app = Flask(__name__)

# Define a route for the /command endpoint
@app.route('/command', methods=['POST'])
def command():
    data = request.json
    print(f"Received command: {data['command']}")
    # Split command using _ as separator
    command_received = data['command'].split('_')
    # Make sure that the command has two parts
    if len(command_received) != 2:
        return 'Invalid command', 400
    else:
        apply_command(command_received)

    return 'Command received', 200

def signal_handler(sig, frame): # function to handle shutdown
    print("quit received, closing down app")
    # turn off the pixels
    pixels.fill((0, 0, 0))
    pixels.brightness = 0
    pixels.show()

    sys.exit(0)

def apply_command(command_received):
    global brightness, red, green, blue
    # Get the command and the var
    direction = command_received[0]
    var = command_received[1]
    print(f"direction: {direction}, var: {var}")

    if var == 'l': #brightness
        if direction == 'up':
            brightness += brightness_step
        elif direction == 'down':
            brightness -= brightness_step
        elif direction == 'max':
            print('hit max')
            if brightness < 0.5:
                brightness = 0.0
            else:
                brightness = 1
        # Make sure that the values are between 0 and 1
        brightness = max(0, min(1, brightness))
    else: #color
        if direction == 'up':
            if var == 'r':
                red += color_step
            elif var == 'g':
                green += color_step
            elif var == 'b':
                blue += color_step
        elif direction == 'down':
            if var == 'r':
                red -= color_step
            elif var == 'g':
                green -= color_step
            elif var == 'b':
                blue -= color_step
        elif direction == 'max':
            if var == 'r':
                if red < 128:
                    red = 255
                else:
                    red = 0
            elif var == 'g':
                if green < 128:
                    green = 255
                else:
                    green = 0
            elif var == 'b':
                if blue < 128:
                    blue = 255
                else:
                    blue = 0

        # Make sure that the values are between 0 and 255
        red = max(0, min(255, red))
        green = max(0, min(255, green))
        blue = max(0, min(255, blue))
    # update the pixels    
    print(f"brightness: {brightness}, red: {red}, green: {green}, blue: {blue}")
    print("command_received: ", command_received)
    pixels.fill((green, red, blue)) # for some reason the order is green, red, blue
    pixels.brightness = brightness
    pixels.show()

# Run the app
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    app.run(host='0.0.0.0', port=5000)

# Raspberry Pi server that listens for POST requests to be used with a stream deck and AZ lights
# Possible commands: 
# up, down : brightness (l), red (r), green (g), blue (b) 
# Example commands: up_l (up brigthness), down_r (down red), up_g (up green), down_b (down blue)
# Author: Raul Hernandez, 16/06/2024

# Imports
from flask import Flask, request
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

def apply_command(command_received):
    global brightness, red, green, blue
    # Get the command and the var
    direction = command_received[0]
    var = command_received[1]
    if var == 'l': #brightness
        if direction == 'up':
            brightness += 0.1
        elif direction == 'down':
            brightness -= 0.1
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
        # Make sure that the values are between 0 and 255
        red = max(0, min(255, red))
        green = max(0, min(255, green))
        blue = max(0, min(255, blue))
    # update the pixels
    pixels.fill((red, green, blue))
    pixels.brightness = brightness
    pixels.show()

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

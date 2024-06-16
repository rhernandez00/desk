# Raspberry Pi server that listens for POST requests to be used with a stream deck and AZ lights
# Author: Raul Hernandez

# Imports
from flask import Flask, request

# Create a Flask app
app = Flask(__name__)

# Define a route for the /command endpoint
@app.route('/command', methods=['POST'])
def command():
    data = request.json
    print(f"Received command: {data['command']}")
    # Check if the command is 'on'
    if data['command'] == 'on':
        # Add code to turn on the lights
        print('Turning on the lights')



    return 'Command received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

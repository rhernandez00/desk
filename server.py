from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    data = request.json
    print(f"Received command: {data['command']}")
    # Here you can add code to process the command
    return 'Command received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/info', methods=['GET'])
def get_info():
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify ({
        'result':'success', 
        'msg': 'GET info'
    })

@app.route('/info', methods=['POST'])
def post_info():
    my_name = request.form['my_name']
    print(my_name)
    return jsonify ({
        'result':'success', 
        'msg': 'POST info'
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# Source: partially from Toward Data Science
from flask import Flask, request, jsonify, make_response
from flask_restful import Api

app = Flask(__name__)

# POST the text editor input to slang tagging & processing algo
@app.route('/api',methods=['POST','GET'])
def apiHandler():
    # POST request
    if request.method == 'POST':
        # main(input)
        req = request.get_json()
        print(f"req is {req}")
        res = make_response(jsonify({"message": "OK"}), 200)
        return res

if __name__ == '__main__':
    app.run(debug=True)
    
# genzlator.ml/
# Localhost: http://127.0.0.1:5000
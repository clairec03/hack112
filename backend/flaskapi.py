# Source: partially from Toward Data Science
from flask import Flask, request, jsonify, make_response
from tagSlang import *
from main import *
app = Flask(__name__)

# POST the text editor input to slang tagging & processing algo
@app.route('/api',methods=['POST','GET'])
def apiHandler():
    # POST request
    if request.method == 'POST':
        # main(input)
        req = request.get_json()
        print("GOT A REQ")
        print(req)

        res = make_response(jsonify(req), 200)

        if(req.startswith('__1__')):
            return mainFunct(req[5:])
        else:
            return auxFunct(req[5:])
    return (
        mainFunct('yolo')
    )

# @app.route('/search',methods=['POST','GET'])
# def apiHandler():
#     # POST request
#     if request.method == 'POST':
#         # main(input)
#         req = request.get_json()
#         print("GOT A REQ")
#         print(req)
#         #set that contains slang words
#         # slangSet = checkAll(req)


#         # print(f"req is {req}")
#         # res = make_response(jsonify({"message": "OK"}), 200)
#         res = make_response(jsonify(req), 200)
#         return auxFunct(req)

#     return (
#         mainFunct('yolo')
#     )
if __name__ == '__main__':
    app.run(debug=True)
    
# genzlator.ml/
# Localhost: http://127.0.0.1:5000
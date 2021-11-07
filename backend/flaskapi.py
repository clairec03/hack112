# Source: partially from Toward Data Science
from flask import Flask
from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast

app = Flask(__name__)
api = Api(app)

# File path for storing the slang words
@app.route('/api',methods=['GET'])
def apiHandler():
    return {
        "slang" : "definition"
    }
 
if __name__ == '__main__':
    app.run(debug=True)
# Input: a set of slang words {}
# Dictionary
# Keys : values
# Slang : ('definition', ['example sentence', ])
# def ApiHandler(Resources):
#     def get(self):
#         return {

#         }

#     def post(self):
#         return 

# genzlator.ml/
# Localhost: http://127.0.0.1:5000
# api.add_resource(Slang, '/slang')
# api.add_resource(NormalWord, '/normalword')
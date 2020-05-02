#!/usr/bin/python
from flask import Flask, jsonify, request, abort
import os
import re
import urllib

app = Flask(__name__)

@app.route("/api/carplate/", methods=['POST'])
def hello():
	print(request.json['imageURL'])
	print(request.json['fileName'])
	urllib.urlretrieve(request.json['imageURL'], filename="home/utarfyp97/carPlate/"+request.json['fileName'])
	os.system("alpr -c sg /home/utarfyp97/carPlate/"+request.json['fileName']+" > /home/utarfyp97/output.txt")
	os.system("cat /home/utarfyp97/output.txt")

	with open('/home/utarfyp97/output.txt', 'r') as myfile:
  		data = myfile.read()
		n1 = data.index("-")
		n2 = data.index("confidence")
		data = data[n1+2:n2]
		data = re.sub(r"\W", "", data)	

	response = {
        'status': data,
    	}

	return jsonify(response), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

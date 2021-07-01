#!/usr/bin/env python3
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
import constants
from flask import Flask, jsonify
import json 
from typing import List
from flask_cors import CORS

cred  = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection('player_coords_2021-06-30').order_by("player_name").stream()

#app = Flask("coords_retriever.py")
app = Flask(__name__)
CORS(app)
cors = CORS(app, resouce = {
	r"/*":{
		"origins":"*"
	}
})

@app.route("/api/v1/get_all_coords")
def get_coords_api():
	docs = db.collection('player_coords_2021-06-17').order_by("player_name").stream()
	listNames = []
	for doc in docs:
		playerName = doc.get("player_name")
		listNames.append(playerName)


	uniqueListNames = uniqueListF(listNames)
	print(uniqueListNames)

	coordsFinal = []
	for name in uniqueListNames:
		coordsPlayer = get_coords_by_name_private(name)
		coordsPerPlayer = {
			name : coordsPlayer
		}
		coordsFinal.append(coordsPerPlayer)

	result = jsonify(coordsFinal)
	return result


@app.route("/api/v1/get_coords_by_name/<name>")
def get_coords_by_name_api(name):
	name2 = name.replace("%20", " ")
	print(name)
	print(name2)
	docs = db.collection('player_coords_2021-06-17').where("player_name","==",name2).stream()
	listCoords = []
	for doc in docs:
		coords = {
			"galaxy": doc.get("galaxy_number"),
			"system": doc.get("system_number"),
			"position": doc.get("position_number")
		}
		listCoords.append(coords)

	result = jsonify(listCoords)
	return result


def get_coords_by_name_private(name):
	docs = db.collection('player_coords_2021-06-17').where("player_name","==",name).stream()
	listCoords = []
	for doc in docs:
		coords = {
			"galaxy": doc.get("galaxy_number"),
			"system": doc.get("system_number"),
			"position": doc.get("position_number")
		}

		listCoords.append(coords)


	return listCoords

def uniqueListF(list):
 
	# intilize a null list
	unique_list = []

	# traverse for all elements
	for x in list:
		# check if exists in unique_list or not
		if x not in unique_list:
			unique_list.append(x)

	return unique_list



#!/usr/bin/env python3
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
import constants
from flask import Flask, jsonify
import json 
from typing import List

cred  = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection('player_coords_2021-06-17').order_by("player_name").stream()

app = Flask(__name__)
@app.route("/")
def get_coords():
	docs = db.collection('player_coords_2021-06-17').order_by("player_name").stream()
	listCoords = []
	for doc in docs:
		coords = {
			"name": doc.get("player_name"),
			"galaxy": doc.get("galaxy_number"),
			"system": doc.get("system_number"),
			"position": doc.get("position_number")
		}

		listCoords.append(coords)
	return json.dumps(listCoords)


'''
coordsObject = {}
coordsAllPlayers = []
coordsPerPlayer = []

listCoords = []		

result = json(algo)	

for doc in docs:
	coordsO = {
		"name": doc.get("player_name"),
		"galaxy": doc.get("galaxy_number"),
		"system": doc.get("system_number"),
		"position": doc.get("position_number")
	}

	listCoords.append(coordsO)	

listCoords = sorted(listCoords, key = lambda k: k['name'])

#jsonCoords = json.dumps(listCoords)
#print(jsonCoords)

for coord in listCoords:
	name = coord["name"]
	galaxy = coord["galaxy"],
	system = coord["system"],
	position = coord["position"]

	coordPlayer = {
		name: name,
		galaxy: galaxy,
		system: system,
		position: position
	}

	for coordPlayer in coordsPlayer:
		coordsPlayer = {
			"galaxy": coord["galaxy"],
			"system": coord["system"],
			"position": coord["position"]
		}


	print("coordsO")
	print(coordsPlayerO)
'''




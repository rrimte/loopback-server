import flask
import random
import hashlib
import time
from flask import request, jsonify, abort
from flask import render_template

def get_hash():
	hash = hashlib.sha1()
	hash.update(str(time.time()).encode('utf-8'))
	return hash.hexdigest()

def process_dict_type(request, cklist, dict_elt):
	for k, v in dict_elt.items():
		tmpList = getattr(request, cklist['datatype'])[k]	
		for tmpItem in tmpList:
			for checkKey in v:
				if checkKey not in tmpItem:
					print(checkKey + ' is not in data')
					abort(400)	

def request_process(cklist_header, cklist, tpl_data):
	if cklist_header:
		for key in cklist_header:	
			if not key in request.headers:
				print(key + ' is not in headers')
				abort(400)
    
	if cklist:
		if False == hasattr(request, cklist['datatype']):
			print(cklist['datatype'] + ' is not the type of the payload')
			abort(400)

		if 'data_list' in cklist and 'datatype' in cklist:
			data_list = cklist['data_list']
			for elt in data_list:
				if isinstance(elt,dict):
					process_dict_type(request, cklist, elt)
				elif not elt in getattr(request, cklist['datatype']):
					print(elt + ' is not in request data')
					abort(400)
	return render_template(cklist['template'], **tpl_data)
	
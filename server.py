import flask
from api_common_lib import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
  return '''<h1>Comcast loopback server</h1>
  <p>/oauth/token</p>
  <p>/api/v2/request_truck_roll_validation</p>'''


	
checklist_header = ['Authorization', 'Content-type']
checklist = {'methods': ['POST'], 'datatype':'json', 'uri':'/api/v2/request_truck_roll_validation', 'template':'truckroll.j2', 
'data_list':['request_data', {'request_data':['billing_account_number', 'truck_roll_id', 'csg_scheduled_date',
'csg_scheduled_timeslot', 'cancelation_reason']}]}
template_data = {
	'status':'success', 
	'message':'test'
}

@app.route(checklist['uri'], methods=checklist['methods'])
def func1():
	return request_process(checklist_header, checklist, template_data)


checklist_header1 = ['Content-type']
checklist1 = {'methods': ['POST'], 'datatype':'form', 'uri':'/oauth/token', 'template':'token.j2', 'data_list':['client_id', 'client_secret', 'grant_type']}
template_data1 = {
	'access_token':get_hash(), 'token_type':'Bearer'
}

@app.route(checklist1['uri'], methods=checklist1['methods'])
def func12():
	return request_process(checklist_header1, checklist1, template_data1)

app.run(host='0.0.0.0')

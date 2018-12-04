import http.client, urllib.parse
import json
import datetime

def readJson(fileName):
	with open(fileName, 'r') as file:
		return json.load(file)

def main(jsonArray):

	for i in jsonArray:
		i = readyData(i)
		res = postData(i)

		if(res.status != 200):
			print("Error! {}".format(i))
			f = open("errors.txt", "a")
			f.write(i)
			f.write("\n")
			f.close()

def postData(entry):
	headers = {"Content-Type": "application/json", "Accept":"application/json"}
	conn = http.client.HTTPConnection("localhost:65443")
	entry = json.dumps(entry)
	print(entry)
	conn.request("POST", "/api/ScadaWellData", entry, headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	conn.close()
	return response


def readyData(entry):
	entry["Id"] = 0
	entry.pop("json_featuretype", 0)
	date = entry["Timestamp"]
	year = date[:4]
	date = date[4:]
	month = date[:2]
	date = date[2:]
	day = date[:2]
	date = date[2:]
	hour = date[:2]
	date = date[2:]
	minute = date[:2]
	date = date[2:]
	second = date[:2]
	entry["Timestamp"] = "{}-{}-{}T{}:{}:{}".format(year, month, day, hour, minute, second)
	entry["RecordId"] = "Import"

	return entry

var = readJson("Output.json")

main(var)

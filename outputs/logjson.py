# File logging output for AirPi.
#
# Writes files in JSON format, which can later be read into another application.

import output
import json
import datetime

class LogJSON(output.Output):
	requiredData = ["path"]

	def __init__(self,data):
		self.path=data["path"]

	def outputData(self,dataPoints):

		# Build an array of data to output
		output = {"time": str(datetime.datetime.now())}
		for i in dataPoints:
			output[i["name"]] = i["value"]
		
		# Write the data to a file
		try:
			with open(self.path, "a") as file:
				file.write(json.dumps(output) + "\n")
		except Exception, e:
			print("Failed to write data to log file: " + e.message)
			return False
		return True

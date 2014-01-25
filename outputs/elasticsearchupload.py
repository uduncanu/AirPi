# Elasticsearch uploading output for AirPi.
# 
# Requires the elasticsearch pip package to be installed:
#      pip install elasticsearch
#

import output
import json
import datetime
import elasticsearch

class ElasticsearchUpload(output.Output):
	requiredData = ["host", "index"]

	def __init__(self,data):
		self.es = elasticsearch.Elasticsearch([data["host"]]);
		self.index = data["index"]

	def outputData(self,dataPoints):

		# Build the data to send to Elasticsearch
		body = {"@timestamp": datetime.datetime.now(), "@source": "airpi", "@type":"airpi"}
		for i in dataPoints:
			body[i["name"]] = i["value"]

		# Send the data to Elasticsearch
		try:
			return self.es.index(index=self.index, doc_type="airpi", id=body["@timestamp"], body=body)
		except Exception, e:
			print("Failed to send data to Elasticsearch: " + e.message);
			return False

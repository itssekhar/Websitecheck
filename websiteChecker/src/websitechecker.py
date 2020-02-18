import logging
import requests
import re

formatString = '%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
dateFmt = '%Y-%m-%d:%H:%M:%S'
logging.basicConfig(
    format=formatString,
    datefmt=dateFmt,
    level=logging.INFO,
)

requests.packages.urllib3.disable_warnings()


class Websitechecker(object):
	
	def __init__(self):

		self.verify = False
		self.log = logging.getLogger('website-lookup')

	def url_ok(self, webaddress):

		try:
			response = requests.head(webaddress)
			return response.status_code == 200
			
		except:
			self.log.exception("API request has failed.Try later")
			return False









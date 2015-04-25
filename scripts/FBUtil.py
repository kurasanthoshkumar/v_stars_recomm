import json
import urllib
class FBUtil:
	def __init__(self):
		print ""

	def getFBProfilePicUrl(self, uid):
		return "https://graph.facebook.com/"+str(uid)+"/picture?type=large&width=180&height=240"

	def getGender(self, uid):
		try:
			url = "http://graph.facebook.com/" + str(uid)
			json_content = urllib.urlopen(url).read()
			data = json.loads(json_content)
			return data["gender"]
		except Exception:
			print "Gender not found for uid" + uid
			return None
			

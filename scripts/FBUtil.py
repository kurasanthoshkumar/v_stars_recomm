class FBUtil:
	def __init__(self):
		print ""

	def getFBProfilePicUrl(self, uid):
		return "https://graph.facebook.com/"+str(uid)+"/picture?type=large&width=180&height=240"

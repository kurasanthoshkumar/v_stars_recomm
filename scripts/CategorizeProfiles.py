from FBUtil import *
from CompareImages import *
import urllib, cStringIO
import Image
import ast
class CategorizeProfile:
	fbuid = ""
	profile_pic_path = ""
	configDict = {}
	imageConfig = "image_attributes.cfg"
	productPathPrefix="images/"
	def __init__(self, fbuid):
		print "Categorize Profile Initialized"
		self.fbuid = fbuid
		self.profile_pic_path = self.storeFBImageLocally()
		cFO = open(self.imageConfig, "r")
		self.configDict = ast.literal_eval(cFO.read())
	
	def storeFBImageLocally(self):
		outfile = "profileimages/"+str(self.fbuid)+".jpg"
		fbutil = FBUtil()
		URL = fbutil.getFBProfilePicUrl(self.fbuid)
		file = cStringIO.StringIO(urllib.urlopen(URL).read())
		img = Image.open(file)
		img.save(outfile)
		return outfile

	def getAttributes(self, outputDict):
		attributeScore={}
		for key in outputDict:
			for key1 in self.configDict[key]:
				if key1 not in attributeScore:
					attributeScore[key1] = {}
				if self.configDict[key][key1] not in attributeScore[key1]:
					attributeScore[key1][self.configDict[key][key1]] = []	
				
				attributeScore[key1][self.configDict[key][key1]].append(outputDict[key])
		topAttribute = {}
		for key in attributeScore:
			minval=0
			mincat=""
			for key1 in attributeScore[key]:
				attributeScore[key][key1] = sum(attributeScore[key][key1])/len(attributeScore[key][key1])
				if attributeScore[key][key1] < minval:
					minval = attributeScore[key][key1]
					mincat = key1
			topAttribute[key] = mincat
		print topAttribute	
	def categorize(self):
		outputDict = {}
		compareImages = CompareImages()
		for key in self.configDict:
			mse = compareImages.get_mse(self.productPathPrefix + key, self.profile_pic_path)	
			outputDict[key] = mse
			
		print self.getAttributes(outputDict)	

		
cp = CategorizeProfile(1837424483)
cp.categorize()

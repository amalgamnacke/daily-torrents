import re

class TorrentNameTranslator():
	def __init__(self):
		self.reg = r"^(.*)\.\d{4}\..*\.(\d{3,4}p)\."
	def translate(self, torrent):
		translation = {}

		result = re.match(self.reg_name, torrent)
		if name == None:
			print "Could not find name in torrent string: " + torrent
			return
		try:
			translation["name"] = result.group(1)
		except:
			pass
		try:
			translation["year"] = result.group(2)
		except:
			pass
		try:
			quality = result.group(3)
			if quality == "1080p":
				translation["1080p"] = True
			elif quality == "720p":
				translation["720p"] = True
		except:
			pass
		translation["PublicHD"] = result.count("PublicHD") > 0
		
		return translation

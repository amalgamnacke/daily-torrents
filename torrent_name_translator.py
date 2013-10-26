import re, urllib

class TorrentNameTranslator():
	def __init__(self):
		self.reg_torrent = r"^(.*)\.(3D)*(\d{4}).*(1080p|720p).*"
		self.reg_torrent_size = r".*Size (\d{1,4}\.\d{1,4}).(GiB|MiB).*"

	def translate_torrent(self, torrent):
		translation = {
			"name": "",
			"year": 0,
			"1080p": False,
			"720p": False,
			"PublicHD": False
		}

		result = re.match(self.reg_torrent, torrent)
		if result == None:
			print "Could not find name in torrent string: " + torrent
			return
		#print result.group(1)
		#print result.group(2)
		#print result.group(3)
		#print result.group(4)
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
		try:
			count = result.group().count("PublicHD")
			if count > 0:
				translation["PublicHD"] = True
		except:
			pass
		
		return translation

	def translate_size(self, text):
		if text == None: return text
		
		try:
			result = re.match(self.reg_torrent_size, text)

			if result.group(2) == "GiB":
				return int(float(result.group(1)) * 1000)
			elif result.group(2) == "MiB":
				return int(float(result.group(1)))
			else:
				return None
		except:
			return None

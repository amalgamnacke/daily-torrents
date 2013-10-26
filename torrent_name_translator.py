import re

class TorrentNameTranslator():
	def __init__(self):
		self.reg_torrent = r"^(.*)\.\d{4}\..*\.(\d{3,4}p)\."
		self.reg_torrent_size = r"Storlek (.*)&nbsp;(.*),"

	def translate_torrent(self, torrent):
		translation = {}

		result = re.match(self.reg_torrent, torrent)
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

	def translate_size(self, text):
		size = 1000000
		result = re.findall(self.reg_torrent_size, text)
		try:
			if result[1] == "GiB":
				return int(float(result[0]) * 1000)
			elif result[1] == "MiB":
				result int(result[0])
			else
				return size
		except:
			return size

from http_scraper import HttpScraper
from daily_torrents_database import DailyTorrentsDatabase
from torrent_name_translator import TorrentNameTranslator
import magnet_to_torrent as store

class DailyTorrents:
	def __init__(self):
		self.scraper = HttpScraper()
		self.db = DailyTorrentsDatabase()
		self.translator = TorrentNameTranslator()

		self.base_url_tpb = "thepiratebay.sx"
		self.base_page_tpb = "/user/"
		self.users_tpb = ["BOZX"]

		self.minimum_torrent_size = 800#mb
		self.maximum_torrent_size = 18000#mb,18gb

	def search_size(self, element):
		element = element.getnext()

		# got to last element and not found
		if element == None:
			print "Size for torrent was not found...skipping."
			return self.maximum_torrent_size+1

		size = self.translator.translate_size(element.text)
		if type(size) == type(int()):
			return size

		return self.search_size(element)


	def get_tpb_user(self, user):
		print "Scraping: " + self.base_url_tpb + self.base_page_tpb + user + "..."
		raw_html = self.scraper.scrape(self.base_url_tpb, self.base_page_tpb + user, "a.detLink")
		print "Got " + str(len(raw_html)) + " titles!"
				
		torrent_dict = {}
		for row in raw_html:
			#html_size = row.getparent().getnext().getnext().getnext().getnext().getnext().text
			torrent_size = self.search_size(row.getparent())

			# Only add torrent as an option if it legit size
			if self.minimum_torrent_size < torrent_size < self.maximum_torrent_size:
				torrent_dict[row.text] = row.getparent().getnext().get("href")
		print "Returning " + str(len(torrent_dict)) + " acceptable titles."
		return torrent_dict

	#returns format: {"Movie.Torrent.Filename.2013": "magnetlink"}
	def get_tpb_all_users(self):
		torrent_dict = {}
		for user in self.users_tpb:
			user_dict = self.get_tpb_user(user)
			torrent_dict = dict(torrent_dict.items() + user_dict.items())
		return torrent_dict

	def find_torrents_to_download(self):
		torrent_dict = self.get_tpb_all_users()
		torrent_info = []

		for torrent in torrent_dict:
			torrent_info = self.translator.translate_torrent(torrent)
			
			# if movie already downloaded
			if self.db.movie_exists(torrent_info["name"]):
				continue
			
			# look for better quality
			if torrent_info["1080p"] == False:
				for search in torrent_dict:
					if search["name"] == torrent["name"] \
					and seach["1080p"] == True:
							
		
		
		#i = 0
		#for torrent in torrent_info:
		#	print str(i) + " "+ torrent["name"] +": "+ str(torrent["PublicHD"])
		#	i=i+1
		
		
		
a = DailyTorrents()
b = a.find_torrents_to_download()

from http_scraper import HttpScraper
from daily_torrents_database import DailyTorrentsDatabase
from magnet_to_torrent import MagnetToTorrent
from torrent_name_translator import TorrentNameTranslator

class DailyTorrents:
	def __init__(self):
		self.scraper = HttpScraper()
		self.db = DailyTorrentsDatabase()
		self.store = MagnetToTorrent()
		self.translator = TorrentNameTranslator()

		self.base_url_tpb = "thepiratebay.sx"
		self.base_page_tpb = "/user/"
		self.users_tpb = ["BOZX"]

		self.minimum_torrent_size = 800#mb
		self.maximum_torrent_size = 18000#mb,18gb

	def get_tpb_user(self, user):
		print "Scraping: " + self.base_url_tpb + self.base_page_tpb + user + "..."
		raw_html = self.scraper.scrape(self.base_url_tpb, self.base_page_tpb + user, "a.detLink")
		print "Got " + str(len(raw_html)) + " titles."
				
		torrent_dict = {}
		for row in raw_html:
			torrentSize = row.getparent().getnext().getnext().getnext().getnext().getnext().text
			torrentSize = self.translator(torrentSize)
			
			# Only add torrent as an option if it legit size
			if self.minimum_torrent_size < torrentSize > self.maximum_torrent_size:
				torrent_dict[row.text] = row.getparent().getnext().get("href")
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
		
		
a = DailyTorrents()
b = a.get_tpb_all_users()
print len(b)

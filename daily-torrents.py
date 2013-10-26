from http_scraper import HttpScraper

class DailyTorrents:
	def __init__(self):
		self.scraper = HttpScraper()

		self.base_url_tpb = "thepiratebay.sx"
		self.base_page_tpb = "/user/"
		self.users_tpb = ["BOZX", "aoloffline"]

	def get_tpb_user(self, user):
		print "Scraping: " + self.base_url_tpb + self.base_page_tpb + user + "..."
		raw_html = self.scraper.scrape(self.base_url_tpb, self.base_page_tpb + user, "a.detLink")
		print "Got " + str(len(raw_html)) + " titles."
				
		torrent_dict = {}		
		for row in raw_html:
			torrent_dict[row.text] = row.getparent().getnext().get("href")
		return torrent_dict

	def get_tpb_all_users(self):
		torrent_dict = {}
		for user in self.users_tpb:
			user_dict = self.get_tpb_user(user)
			torrent_dict = dict(torrent_dict.items() + user_dict.items())
		return torrent_dict
a = DailyTorrents()
b = a.get_tpb_all_users()
print len(b)

import sqlite3 as lite

class DailyTorrentsDatabase:
	def __init__(self):
		self.database_name = "daily-torrents-database.db"

		# Initialize database
		print "Initializing SQLITE3: " + self.database_name
		con = None
		con = lite.connect(self.database_name)
		if con == None:
			print "Could not find or create new database file: "+self.database_name+". Permission? Exiting..."
			return
		
		try:
			cur = con.cursor()
			cur.execute("CREATE TABLE IF NOT EXISTS movies(title TEXT, year INT, filename TEXT, magnet_url TEXT)")
		except:
			raise
		con.close()

	def get_DB_connection(self):
		con = None
		con = lite.connect(self.database_name)
		if con == None:
			print "Could not connect to database: "+self.database_name+". Exiting..."
			return
		return con	

	def movieExists(self, title):
		con = self.get_DB_connection()
		cur = con.cursor()

		cur.execute("SELECT * FROM movies WHERE title = '"+title+"'")
		data = cur.fetchone()

		con.close()
		return data != None

	def insertMovie(self, title, year, filename, magnet_url):
		con = self.get_DB_connection()
		cur = con.cursor()

		cur.execute("INSERT INTO movies VALUES(?,?,?,?)", (title, year, filename, magnet_url))
		
		con.commit()
		con.close()


a = DailyTorrentsDatabase()
print a.movieExists("kiss")
a.insertMovie("kiss", ":::LONG URLMAN")
print a.movieExists("kiss")

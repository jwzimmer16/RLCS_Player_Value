from bs4 import BeautifulSoup as BS
import requests
import csv

rlg_url = "https://fantasy.rocket-league.com/leaderboards/players"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

csv_header = ['Name', 'Total', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6']

csv_fn = "player_stats.csv"

def getStats():
	# Get html file from rl garage site
	html_file = requests.get(rlg_url, headers=agent)
	# Parse html file
	soup = BS(html_file.content, 'html.parser')

	# Get player leaderboard table
	table = soup.find('table', attrs={'class':'tftable'})

	# Open csv for writing
	with open(csv_fn, 'wb') as csvfile:
		csv_writer = csv.writer(csvfile, delimiter=',')

		# Write csv header
		csv_writer.writerow(csv_header)
		# writeRow(csv_writer, csv_header)

		# Get table rows
		rows = table.find_all('tr')
		# Iterate through rows and write to csv
		for row in rows[1:]:
			cols = row.find_all('td')
			cols = [ele.text.strip() for ele in cols]
			cols = cols[1:]
			csv_writer.writerow(cols)
'''
def writeRow(csvw, row):
	csvw.writerow(row)
'''

def main():

	getStats()

if __name__ == "__main__":
	main()
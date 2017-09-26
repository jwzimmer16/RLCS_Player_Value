import csv
from statUpdate import getStats

stats_fn = "player_stats.csv"
player_cost_fn = "player_cost.txt"

player_value_fn = "player_values.csv"

header = ["Name", "Cost", "Avg Score/Gm", "Value"]

def updateFantasyValues():
	# Get latest stats
	getStats()
	# Get dictionary of player costs
	player_cost_dict = getPlayerCosts()
	# Initialize player list
	player_list = []

	# Open value csv to write to
	with open(player_value_fn, 'wb') as value_file:
		value_writer = csv.writer(value_file, delimiter=',')

		value_writer.writerow(header)

		# Open stats csv to read from
		with open(stats_fn, 'r') as stats_file:
			stat_reader = csv.reader(stats_file, delimiter=',')

			# Iterate through rows in stat csv
			for i, row in enumerate(stat_reader):
				# skip header
				if not(i==0):

					# Parse name, total score, weekly scores
					name = row[0]
					total = row[1]
					scores = row[2:]

					# Get Player cost from dictionary
					cost = player_cost_dict[name.lower()]

					# Get average score per game 
					if not(total):
						avg_score = 0
					else:
						avg_score = float(total) / (6.0 - float(scores.count('-')) )

					# Calculate player value (avg score / cost)
					value = avg_score /  float(cost)

					player_list.append([name, float(cost), avg_score, value])

			# Sort player list by value
			sorted_player_list = sorted(player_list, key=lambda l:l[3], reverse=True)

			# Write sorted list to csv
			for player_info in sorted_player_list:
				value_writer.writerow(player_info)


def getPlayerCosts():

	player_dict = {}

	#Open text file containing cost for each player
	with open(player_cost_fn, 'r') as cost_file:
		lines = cost_file.readlines()

		for line in lines:
			pair = line.rsplit(' ',1)

			player_dict[pair[0].lower()] = pair[1]

	return player_dict



def main():

	updateFantasyValues()

if __name__ == "__main__":
	main()
import twitter as tw
import settings
from datetime import datetime

consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
access_token = settings.access_token
access_token_secret = settings.access_token_secret

api = tw.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
             access_token_key=access_token, access_token_secret=access_token_secret) 


def get_followers_data():

	'''
		read data from your twitter followers and save them
		to a csv file:
	'''

	followers = api.GetFollowers()

	print "you have %d followers" %len(followers)

	followers_list = []

	for f in followers:		
		follower_data = []
		follower_data.append(f.name.encode('utf8'))
		# follower_data.append(f.location.encode('utf8')) if f.location else follower_data.append(None)
		follower_data.append(count_words(f.name))
		follower_data.append(f.lang.encode('utf8'))
		follower_data.append(int(f.statuses_count))
		follower_data.append(int(f.followers_count))
		follower_data.append(int(f.friends_count))
		follower_data.append(int(f.favourites_count))
		follower_data.append(int(f.listed_count))

		followers_list.append(follower_data)

	return followers_list


def save_csv(file_name, data_list):

	import csv 

	with open(file_name, 'wb') as csv_file:
		file_writer = csv.writer(csv_file)

		for user in data_list:
			print user
			try:
				file_writer.writerow(user)
			except UnicodeEncodeError, e:
				print 'error saving user ', user
				print e 

def count_words(text):
	import re
	return len(re.findall(r'\w+', text))


if __name__ == '__main__':

	followers_data = get_followers_data()

	print 'saving csv  ....'

	save_csv('followers.csv', followers_data)


	print 'saved !!'



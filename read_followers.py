import twitter as tw
import settings
from datetime import datetime
from api_init import  api


def get_user_data(user):
	_data = []
	_data.append(user.name.encode('utf8'))
	# follower_data.append(user.location.encode('utf8')) if f.location else follower_data.append(None)
	_data.append(count_words(user.name))
	_data.append(user.lang.encode('utf8'))
	_data.append(int(user.statuses_count))
	_data.append(int(user.followers_count))
	_data.append(int(user.friends_count))
	_data.append(int(user.favourites_count))
	_data.append(int(user.listed_count))

	return _data

def get_followers_data():

	'''
	read data from your twitter followers and save them
	to a csv file:
	'''

	follower_ids = api.GetFollowerIDs()
	followers_list = []

	print 'processing %d followers.' %len(follower_ids['ids'])

	for id in follower_ids['ids']:
		follower = api.GetUser(id)
		try:
			followers_list.append( get_user_data(follower))
		except AttributeError:
			print follower

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



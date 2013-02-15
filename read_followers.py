from utils.api_init import  api
from utils import file_utils

def get_user_data(user):

	_data = []
	_data.append(user.name.encode('utf8'))
	# follower_data.append(user.location.encode('utf8')) if f.location else follower_data.append(None)
	_data.append(count_words(user.name))
	# _data.append(user.lang.encode('utf8'))
	_data.append(int(user.statuses_count))
	_data.append(int(user.followers_count))
	_data.append(int(user.friends_count))
	_data.append(int(user.favourites_count))
	_data.append(int(user.listed_count))

	return _data



def read_followers(user_name):


    # 1 get new data from twitter


    user = api.GetUser(user_name)

    followers_id = api.GetFollowerIDs(user.id)

    print '%s(%s) has %d followers ' %(user_name, user.id, len(followers_id['ids']))

    user_data = []

    for _id in  followers_id['ids']:
        try:
            print user.name, _id
            # print read_followers.get_user_data(user)
            user = api.GetUser(_id)
            user_data.append(get_user_data(user))
        except Exception, e:
            print e
            break


    # 5 save the data to the csv file.

    file_utils.save_csv('followers_%s.csv' %user_name, user_data)

    return



def count_words(text):
	import re
	return len(re.findall(r'\w+', text))


if __name__ == '__main__':

    import sys

    followers_data = read_followers(sys.argv[1])

    print 'saved !!'


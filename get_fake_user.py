__author__ = 'uolter'

from urllib import urlopen
from bs4 import BeautifulSoup
from api_init import api
import read_followers
from urllib2 import URLError
from twitter import TwitterError


searchurls = [
    'http://www.pastemagazine.com/blogs/lists/2011/12/best-twitter-accounts-of-2011.html',
    'http://www.pastemagazine.com/blogs/lists/2011/12/best-twitter-accounts-of-2011.html?p=2',
    'http://www.pastemagazine.com/blogs/lists/2011/12/best-twitter-accounts-of-2011.html?p=3',
    'http://www.pastemagazine.com/blogs/lists/2011/12/best-twitter-accounts-of-2011.html?p=4',
]



def get_twitter_user(user):

    return api.GetUser(user)


def main():

    user_list = [] # list of fake users

    for url in searchurls:
        f = urlopen(url)
        html = f.read()


        soup = BeautifulSoup(html, 'html5lib')

        for link in soup.find_all("big"):
            if link.find('a'):
                user = link.find('a').text
                print user
                if user[0] == '@':
                    try:
                        # read useful data from twitter user's profile
                        user_list.append(read_followers.get_user_data(get_twitter_user(user[1:])))
                    except URLError, e:
                        print '--> not found'
                    except TwitterError:
                        print '--> twitter error .... not found(?)'


    read_followers.save_csv('fake_users.csv', user_list)


if __name__ == '__main__':

    main()
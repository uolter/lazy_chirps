__author__ = 'uolter'


from utils import api_init

from utils import file_utils

def get_timeline(username):

    print '%s timeline' %username

    user = api_init.api.GetUser(username)

    timeline = api_init.api.GetUserTimeline(username)

    return timeline



if __name__ == '__main__':

    import sys

    timeline =get_timeline(sys.argv[1])

    text = []
    for t in timeline:
        text.append([t.text.encode('utf8')])

    print text

    file_utils.save_csv('timeline_%s.csv' %sys.argv[1], text)





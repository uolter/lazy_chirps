__author__ = 'uolter'


from utils import api_init
from utils import file_utils
from datetime import datetime, timedelta
import time


one_hour_ago = datetime.today() - timedelta(hours = 1)

def search(term):

    api = api_init.api

    return api.GetSearch(term,
        geocode=None,
        since_id=None,
        max_id=None,
        until=None,
        per_page=50,
        page=1,
        lang=None,
        show_user="false")


def get_speed(result):


    start = end = minutes = None
    # compute the speed:
    if len(result) > 0:
        # Mon, 11 Feb 2013 17:40:50 +0000
        start = datetime.strptime(result[0].created_at, '%a, %d %b %Y %H:%M:%S +0000')
        end = datetime.strptime(result[-1].created_at, '%a, %d %b %Y %H:%M:%S +0000')
        minutes = (time.mktime(end.timetuple()) - time.mktime(start.timetuple())) / 60
        speed = float(len(result)) / float(minutes)
        return start, end, speed



if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:

        classification = {}
        for i in range(1, len(sys.argv)):
            print 'searching for %s' %sys.argv[i]

            result = search(sys.argv[i])

            text = []
            for t in result:
                text.append([t.text.encode('utf8')])

            start, end , speed = get_speed(result)

            print start, '--->', end
            print 'messages %d, => speed %f' %(len(result), speed)

            classification[sys.argv[i]] = speed


        for key, value in sorted(classification.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            print "%s: %s" % (key, value)

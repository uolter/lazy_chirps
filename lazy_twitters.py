'''
Created on Aug 10, 2012

@author: uolter
'''

'''
    look for users who don't tweeting for a long time
'''

from datetime import datetime
from utils.api_init import api


MAX_DAY_OLD_POST = 30 * 4 # 4 months


def str_to_date(str_date):
    
    return datetime.strptime(str_date, '%a %b %d %H:%M:%S +0000 %Y')


def is_old_days(old_date):
    
    today = datetime.today()
    
    return (today - old_date).days

def main():

    followers = api.GetFriends()
    print 'you are following %d accounts' % len(followers)

    for f in followers:
        try: 
            # how old was the last post?
            latest_status = f.GetStatus()
            if latest_status:
                days = is_old_days(str_to_date(latest_status.created_at))
                
                if days > MAX_DAY_OLD_POST:
                    # latest post is more than 6 months old.     
                    print '%s is more than %d months does not post messages' \
                    % (f.GetName(), days/30)
            else:
                print '%s never posted messages' % f.GetName()
                
        except TypeError:
            pass

if __name__ == '__main__':
    main()
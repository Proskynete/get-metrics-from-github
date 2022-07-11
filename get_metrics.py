import os
import datetime
import dateutil.parser
import pytz
import requests
import time
import collections

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if type(GITHUB_TOKEN) == type(None):
    GITHUB_TOKEN = input("Enter your personal github access token: ").strip()

GITHUB_ORGANIZATION = os.getenv('GITHUB_ORGANIZATION')
if type(GITHUB_ORGANIZATION) == type(None):
    GITHUB_ORGANIZATION = input("Enter the organization name or user name: ").strip()
    
GITHUB_REPOSITORY = input("Enter github repository name: ").strip()
DEFAULT_DAYS = 30
CUSTOM_DAYS = int(input("Enter the number of days to extract data (if you write 0, it will default to 30): ") )

DAYS = DEFAULT_DAYS if CUSTOM_DAYS == 0 else CUSTOM_DAYS

def main():
    start_time = time.time()
    utc=pytz.UTC
    reference_date = (datetime.datetime.now() - datetime.timedelta(days=DAYS)).replace(tzinfo=utc)

    page = 1
    end = False
    times = []
    users = []

    print(f"\n🏁 Start the extraction of data from the {GITHUB_REPOSITORY.upper()} project of the last {DAYS} days")
    while not end:
        print(f"💾 Extracting from page {page}...")
        pull_requests = get_pull_requests(page)
        if len(pull_requests) == 0:
            break

        for pull_request in pull_requests:
            update_at = dateutil.parser.parse(pull_request['updated_at'])
            
            if reference_date:
                if update_at < reference_date:
                    end = True
                    break

            if pull_request['merged_at'] == None:
                continue
    
            startDate = dateutil.parser.isoparse(pull_request['created_at'])  
            endDate = dateutil.parser.isoparse(pull_request['merged_at'])

            dif = (endDate - startDate).days
            times.append(dif)
            users.append(pull_request['user']['login'])
        page+=1

    if(len(times) == 0):
        print("\n💩 There are not enough PRs to generate the report.\n👾 Bye!")
        return 0
        
    executionTime = (time.time() - start_time)
    print(f"\n--- ⌛️ Total execution time: {float(f'{executionTime:.4f}')} seconds ⌛️ ---")
    
    _average = int(sum(times)/len(times))
    _max = max(times)
    _min = min(times)
    _count = len(times)
    contributors = collections.Counter(users).most_common(_count)
    line_break =  '\n\t\t'
    
    print(f"""
        Average: {_average} days
        Max: {_max} days
        Min: {_min} days
        Count: {_count} PRs
        Contributors:{line_break}{line_break.join(printContributors(contributors))}
        """)
    print("👾 See you!")

def get_pull_requests(page):
    params = {
        'state': 'closed',
        'sort': 'updated',
        'direction': 'desc',
        'per_page': 10,
        'page': page
    }
    headers={
        "Accept":"application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    
    r=requests.get(f"https://api.github.com/repos/{GITHUB_ORGANIZATION}/{GITHUB_REPOSITORY}/pulls", params=params ,headers=headers)
    return r.json()

def printContributors(contributors):
    users = []
    for user in contributors:
        users.append("- {user[0]} has {user[1]} PRs".format(user=user))
    return users

if __name__ == '__main__':
    main()
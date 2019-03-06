import datetime
import os
import requests
import time

reminder_start_date = datetime.date(2019, 3, 1) # year, month, day
reminder_time_of_day = "11:00am"
skip_weekend_days = False
task_list_file = 'testability'

this_dir = os.path.dirname(os.path.realpath(__file__))
task_list_dir = '{}/tasks/'.format(this_dir)
task_list_file_path =  '{}{}'.format(task_list_dir, task_list_file)
REMINDER_DATE = reminder_start_date # generated for readability, do not manually set

def increment_reminder_date():
  global REMINDER_DATE
  REMINDER_DATE += datetime.timedelta(days=1)


def increment_reminder_date_excluding_weekends():
  weekend_days = set([5, 6])
  increment_reminder_date()
  while REMINDER_DATE.weekday() not in weekend_days:
    increment_reminder_date()


def post_new_reminder_to_slack(task):
  url = 'https://slack.com/api/reminders.add'
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
  token = open('{}/slack_token'.format(this_dir), 'r').read().strip()
  parameters = [
    ('token', token),
    ('text', task),
    ('time', "{} at {}".format(REMINDER_DATE.strftime('%B %-d %Y'), reminder_time_of_day))
  ]
  r = requests.post(url, params=parameters, headers=headers)
  if(r.status_code == requests.status_codes.codes.OK):
    print("SUCCESS: '{}' set for {}".format(parameters[1][1], parameters[2][1]))
  else:
    print("FAILURE: Tried to post the following URL ::: {}".format(r.url))
    print("         received the following error ::: {}".format(r.text))


with open(task_list_file_path, 'r') as task_list:
  for task in task_list:
    post_new_reminder_to_slack(task.strip())
    if(skip_weekend_days is True):
      increment_reminder_date_excluding_weekends()
    else:
      increment_reminder_date()
    time.sleep(4)  # to comply with slack rate limit tier 2 (https://api.slack.com/docs/rate-limits#tiers)
# Setting reminders in slack for a #30daysoftesting session

## Overview

If you would like to create reminders for [#30daysoftesting](https://twitter.com/hashtag/30daysoftesting?lang=en) in slack, you can run this script with pyhton3.

>Note: This script will add reminders to the user who created the token.

## Prerequisits

You will need to change the following variables:
* `reminder_start_date` - default: Tomorrow
* `reminder_time_of_day` - default: 11am
* `skip_weekend_days` - default: False
* `task_list_file` - default: `testability`

Have a slack token saved in a file `./slack_token`
> Note: This is an ignored file to save you from checking in your token!

To generate a token you need to be logged into your team slack in the browser and then go to https://api.slack.com/custom-integrations/legacy-tokens

TODO:
* make it command line program with defaults
* allow for other channels for reminders

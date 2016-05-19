# groupmebot

My lame attempt at building a groupmebot

Current usage:
  Create a file 'config.py' with two variables: bot_id and group (see gen_config.py for a template). Set these to the group number of your bot and the bot id as a string, as is done in the template. Simply modifying gen_config.py will work as well, but less fun. 

Ideas:
* Run as Django app, so can be run with Heroku?
  * Done
 * First, create Django app that can send messages
  * Done
 * Then, integrate with Heroku
  * Done
* Add ability to repeat last message
* Add ability to call someone out for liking their own message
* Add ability to fetch stock information (yahoo.financials.com?)
* Add ability to fetch weather, other informational services
* Add ability to report group analytics (most liked, most kicked, etc.)
* Add ability to post a random gif from Giphy (similar to Slack?)

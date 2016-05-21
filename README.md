# groupmebot

My lame attempt at building a groupmebot

Current usage:
 * Local
  * Create a file 'config.py' with two variables: bot_id and group (see gen_config.py for a template). Set these to the group number of your bot and the bot id as a string, as is done in the template.
 * Heroku
  * Be sure to create a config variable called 'BOT_ID' and set it to your bot's key 

Ideas:
* ~~Run as Django app, so can be run with Heroku?~~ Done
 * ~~First, create Django app that can send messages~~ Done
 * ~~Then, integrate with Heroku~~ Done
* ~~Add ability to repeat last message~~ Done
* Add ability to call someone out for liking their own message
* Add ability to fetch stock information (yahoo.financials.com?)
* Add ability to fetch weather, other informational services
* Add ability to report group analytics (most liked, most kicked, etc.)
* Add ability to post a random gif from Giphy (similar to Slack?)

Bots:
* Parrotbot - Repeats whatever someone said
* Hellobot - If someone says 'hello' anywere in their message, Hellobot will reply with 'Hello <username>!'

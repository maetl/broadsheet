More Short Links
================

Mostly, I wanted a clean, fun interface for checking the latest from my favorite short-form linkblogs. I got tired of dredging through the whack-a-mole dreck in RSS readers just to get at an interesting flow of links.

A little like Giles Bowkett’s ‘Hacker Newspaper’ and Andy Baio’s ‘The Daily: Indexed’; this was an itch, and I scratched it.

My initial prototype ran on Heroku, but I demolished that because I was too tightarse to pay for the hourly cron.

You’re Mostly Interested In The Links
-------------------------------------

See a live version of the app: [not yet]

You’re Mostly Interested In How You Can Make Your Own Newspaper
---------------------------------------------------------------

Then first, you’ll need a way to upload apps to Google App Engine. Still with me? Great.

Clone this app into a local folder and use the "Add Existing Application" in the AppEngineLauncher to set it up on your localhost.

Edit the following line in the app.yaml to point to your App Engine site:

<pre>application: your-app-name</pre>

To configure the list of sources, you’ll want to edit the .yaml config where the urls are stored.

—Better setup coming soon—

Hey, this is README DRIVEN DEVELOPMENT, you can’t expect an initial hack app to actually do anything useful.
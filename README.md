Broadsheet - an automated personal newspaper 
============================================

Mostly, I wanted a clean, fun interface for checking the latest from my favorite short-form linkblogs. I got tired of sloughing through the whack-a-mole dreck in RSS readers just to get at an interesting flow of links. I wanted an interface that was fun to read and could morph and adapt to specific content.

A little like Giles Bowkett’s ‘Hacker Newspaper’ and IA’s TPUTH (http://www.tputh.com); this was an itch, and I scratched it. I’m in complete agreement with Giles about the sub-optimal design of RSS news aggregators. They seem to ignore hundreds of years of typographic experience in hierarchical information display. Recent design trends suggest a move towards more curated and readable experiences, and if the success of Instapaper is anything to go by, people are very much in favor of this.

My initial prototype ran on Heroku, but I demolished that because I was too tightarse to pay for the hourly cron.

You’re mostly interested in the links
-------------------------------------

See a live version of the app: [not yet]

You’re mostly interested in how you can make your own newspaper
---------------------------------------------------------------

First, you’ll need a way to upload apps to Google App Engine. Still with me? Great.

Clone this app into a local folder and use the "Add Existing Application" in the AppEngineLauncher to set it up on your localhost.

Edit the following line in the app.yaml to point to your App Engine site:

<pre>application: your-app-name</pre>

To configure the list of sources, you’ll want to edit the .yaml config where the urls are stored.

Themes are ghetto. Change the stylesheet reference in the index.html template and you’re good to go.

—Better setup coming soon—

Hey, this is README DRIVEN DEVELOPMENT, you can’t expect an initial hack app to actually do anything useful.
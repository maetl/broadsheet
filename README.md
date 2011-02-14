More Short Links
================

I got tired of dredging through the whack-a-mole dreck in RSS readers just to get at an interesting flow 
of tech links.

Mostly, I wanted a clean, fun interface for checking the latest from Nat Torkington’s ‘Four Short Links’ 
and Andy Baio’s ‘Waxy Links’. Throw in a few other interesting tech feeds, and you have a nice regularly
updated.

A little like Giles Bowkett’s ‘Hacker Newspaper’ (and Andy Baio’s ‘The Daily: Indexed’), this was an itch, and I scratched it.

My initial prototype ran on Heroku, but I demolished that because I was too tightarse to pay for the hourly cron.

So—Google App Engine, it is.

You’re Mostly Interested In The Links
-------------------------------------

See a live version of the app: [not yet]

You’re Mostly Interested In How You Can Make Your Own Newspaper
---------------------------------------------------------------

Then first, you’ll need a way to upload apps to Google App Engine. Still with me? Great.

Clone this app into a local folder and use the "Add Existing Application" in the AppEngineLauncher to set it up on your localhost.

To configure the list of sources, you’ll want to edit the model.py file.

—Better setup coming soon—

Hey, this is README DRIVEN DEVELOPMENT, you can’t expect an initial 5 minute hack app to actually do anything useful.
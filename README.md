Broadsheet - an automated personal newspaper 
============================================

Broadsheet is the result of idle tinkering. I got tired of sloughing through the whack-a-mole dreck in RSS readers just to get at recent posts from my favorite tech/culture linkblogs. I wanted an interface driven by typographic heirarchy rather than an unread items count — something fun to read that can morph and adapt to a changing flow of content.

A little like [Giles Bowkett’s ‘Hacker Newspaper’](http://gilesbowkett.blogspot.com/2009/04/miniapp-hacker-newspaper.html) and [IA’s TPUTH](http://www.tputh.com), this was an itch, and I scratched it.

Broadsheet is not a feed reader and is not intended for keeping up to date with regular blogs or news sites. It’s specifically designed for aggregating content from frequently updated short-form linkblogs.

My initial prototype ran on Heroku, but I demolished that because I was too tightarse to pay for the hourly cron. It’s now running on Google App Engine which has a generous quota of URL fetch requests per day.

You’re mostly interested in the links
-------------------------------------

See a live version of the app: http://moreshortlinks.appspot.com/

You’re mostly interested in how you can make your own newspaper
---------------------------------------------------------------

First, you’ll need a way to upload Python applications to Google App Engine. Still with me? Great.

Clone this repository into a local folder and use “Add Existing Application” in the AppEngineLauncher to set it up on your localhost.

Edit the following line in the <code>app.yaml</code> to register a unique App Engine site:

<pre>application: broadsheet</pre>

To configure the list of sources, you’ll want to edit the <code>sources.yaml</code> config:

<pre>sources:
  - feed: http://waxy.org/links/index.xml
    name: Waxy
    homepage: http://waxy.org/
    influence: 50</pre>

Fill out a name and url for each feed source. This should be self explanatory.

The influence factor is used as a base for calculating the weighting of links. Links from sources with higher influence values are treated as more important.

This influence score is assigned to the links by default when they are first imported. The weighting is updated based on popularity and cross references from other sources. This is pretty much a draft, and could be greatly improved.

<pre>aggregator:
  backtype_api_key: e2e2e2e2e2e2e2e2e2e2</pre>

The Backtype API key is used to access backtype.com web services. This provides a regularly refreshed count of how frequently each link has been mentioned on Twitter – a useful starting point for exploring different ways of ordering and prioritizing the display of links.

To change the way that the links are selected, you need to edit the GQL query in <code>Link.headlines()</code>. For example, you might want to change the default list order or number of items displayed:

<pre>def headlines(self):
    return self.all().order('-updated').fetch(32)</pre>

Once you have tested the app on your localhost, you can upload it to the live servers using the “Deploy” button in the AppEngineLauncher.

You’re intrigued by this and are wondering how to customize the layout
----------------------------------------------------------------------

The single HTML template that does everything is <code>/templates/index.html</code>.

All Stylesheets and Javascript assets are contained in the <code>/assets</code> folder. Stylesheets are built using the Sass tool which you’ll need to install via Rubygems:

<pre>gem install sass</pre>

To add a new theme, simply duplicate one of the existing files in the <code>/assets/css/themes</code> folder and change the CSS properties as you like.

Link to the new theme by renaming the following line in <code>/assets/css/broadsheet.scss</code>:

<pre>@import "themes/light.theme"</pre>

Then compile the assets into the master CSS file using Sass. You’ll probably want to use the <code>-t</code> flag to compress whitespace and remove other general cruft:

<pre>sass -t compressed assets/css/broadsheet.scss assets/broadsheet.css</pre>

Kapow! You now have your very own personalized newspaper. Enjoy.
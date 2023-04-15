from .Browser import GetBrowser

tb = GetBrowser()

from .RedditBot.RedditFeed import RedditFeed

rf = RedditFeed(tb)

for x in rf:
  print(x)
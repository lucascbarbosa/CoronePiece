from getEpisodes import getEpisodes
from getCases import getCases


eps=getEpisodes()
cases=getCases()
print(eps[eps['Chapter']=='121'])
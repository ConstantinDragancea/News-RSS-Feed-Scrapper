import sys
from yamsDeepSearch import getLinks

keywords = [x.lower() for x in sys.argv[1 : ]]

print(getLinks(*keywords))

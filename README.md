# News-RSS-Feed-Scrapper
A tool used to search for news articles that contain certain keywords specified by the user.
The tool searches through the entries on a website that collects articles from RSS Feeds of various news sites in Moldova. It opens the article links and searches through the text of the article for the specified keywords.

# Requirements:
- Beautiful Soup

# Usage
First, you should install the required packages. I like installing through a virtual environment, so it doesn't interfere with other projects. So, in the project folder, run the following commands:
```
python3 -m venv news_scrapper
pip3 install -r requirements.txt
```

After that, you can use the program through the main.py program, by giving the keywords you are searching for as arguments for the program:
```
python3 main.py keyword1 keyword2 keyword3 ...
```

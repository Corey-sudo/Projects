import feedparser
import webbrowser
from datetime import date

today = date.today()

def get_feed():
    print(f"Top Security Stories for {today}")
    print("\n[0]: Bleeping Computer")
    print("[1]: Dark Reading")
    print("[2]: Threat Post")
    print("[3]: Krebs on Security")
    print("[4]: Naked Security by Sophos")

    feed_list = ("https://www.bleepingcomputer.com/feed/",
                 "https://www.darkreading.com/rss.xml",
                 "https://threatpost.com/feed/",
                 "https://krebsonsecurity.com/feed/",
                 "https://nakedsecurity.sophos.com/feed/") 

    try:
        user_input = int(input("\nEnter your selection (0-4): "))
        if user_input < 0 or user_input > 4:
            print("Invalid input. Please enter a number between 0 and 4.")
            return get_feed()
            
    except ValueError as e:
        print(str(e))
        return

    feed_data = feedparser.parse(feed_list[user_input])
    article_list = []
    article_link = [] 

    for article in feed_data.entries[:5]:
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    for i, article in enumerate(article_list):
        print(f"\n[{i+1}] {article}")

    try:
        article_click = False
        while not article_click:
            user_click = int(input("\nChoose the article you would like to open (1-5): "))
            if user_click < 1 or user_click > 5:
              print("Invalid input. Please enter a number between 1 and 5.")
              return get_feed()
            else:
              print("\nPlease click the following link")
              webbrowser.open(article_link[user_click - 1])
              article_click = True

    except ValueError as e:
        print(str(e))
        return
    except Exception as e:
        print("An error occurred while opening the link.")
        print(str(e))
        return

get_feed()

from utils.api import get_polygon_client


client = get_polygon_client()

def get_ticker_info(ticker):
    details = client.get_ticker_details(
	ticker,
	)
    print(f"""\nAbout {details.name}\n
{details.description}""")

    # news_title = []
    # news_url = []
    # for news in client.list_ticker_news(
	#     ticker,
	#     order="desc",
	#     limit="2",
	#     sort="published_utc",
	#     ):
    #     news_title.append(news.title)
    #     news_url.append(news.article_url)
    
    
#     for i in range(len(news_title)):
#         print(f"""\n{news_title[i]}
# {news_url[i]}""")

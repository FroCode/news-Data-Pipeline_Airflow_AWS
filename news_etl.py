import requests
import pandas as pd

def etl_process():
    api_key = '5532fc51053a4796a6cd6dd7b2627cc4'  # Replace with your News API key

    def fetch_top_headlines(api_key, country='us', page_size=20):
        url = f'https://newsapi.org/v2/top-headlines?country={country}&pageSize={page_size}&apiKey={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            articles_list = []

            for article in articles:
                # Extract relevant information from each article
                article_info = {
                    'title': article.get('title', 'No Title'),
                    'description': article.get('description', 'No Description'),
                    'url': article.get('url', 'No URL'),
                    'publishedAt': article.get('publishedAt', 'No Date')
                }
                # Append article info to the list
                articles_list.append(article_info)

            return articles_list
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return []

    # Fetch top headlines
    page_size = 100  # Specify the number of articles you want (up to 100)
    headlines = fetch_top_headlines(api_key, page_size=page_size)

    # Convert to DataFrame and save to CSV in S3
    df = pd.DataFrame(headlines)
    df.to_csv('s3://reddits-data/news.csv', index=False)

# Note: Ensure that you have configured your AWS credentials for boto3 to work with S3.

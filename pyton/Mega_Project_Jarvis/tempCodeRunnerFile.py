  # elif "news" in c.lower():
    #     r = requests.get(
    #         f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
    #     )
    #     if r.status_code == 200:
    #         # Parse the JSON response
    #         data = r.json()

    #         # Extract the articles
    #         articles = data.get('articles', [])

    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])
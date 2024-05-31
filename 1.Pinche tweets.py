import snscrape.modules.twitter as sntwitter
import pandas as pd

# Suchparameter
query = 'pinche lang:es since:2024-01-01 until:2024-05-31 geocode:23.6345,-102.5528,1000km'

# Liste für Tweets
tweets_list = []

# Suche nach Tweets und speichere sie in der Liste
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

    # Begrenze auf 100 Tweets für das Beispiel
    if i >= 100:
        break

# Konvertiere die Liste in ein DataFrame
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Ausgabe der Tweets
print(tweets_df)

# Optional: Speichere die Tweets in einer CSV-Datei
tweets_df.to_csv('tweets.csv', index=False)

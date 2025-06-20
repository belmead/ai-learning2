"""
clean_google_play.py

This script uses Pandas to clean up the initial CSV generated by
scraper_google_play.py.

Order of operations: Fill NaNs → Datetime cast → Drop unnecessary series  → Rename series → Reorder series → Add platform col → Write clean CSV

Return: cleaned CSV 'cleaned_google_play.csv'

"""

import pandas as pd

df = pd.read_csv("raw_google_data.csv")

df["reviewCreatedVersion"] = df["reviewCreatedVersion"].fillna("Unknown")

df["at"] = pd.to_datetime(df["at"])  # Step 1: parse into datetime (naive)
df["at"] = df["at"].dt.tz_localize("US/Pacific")  # Step 2: add correct timezone
df["at"] = df["at"].dt.strftime("%Y-%m-%dT%H:%M:%S%z").str.replace(r"(\d{2})(\d{2})$", r"\1:\2", regex=True)  # Step 3: format ISO 8601

print(df["at"].dtype)  # should show datetime64[ns, UTC] before formatting
print(df["at"].head()) # check format

"""
needs to match apple's csv series names:
author_name	rating	review_text	review_date	title	app_version

current series names:
reviewId	userName	userImage	content	score	thumbsUpCount	reviewCreatedVersion	at	replyContent	repliedAt	appVersion
"""

df = df.drop(['reviewId', 
              'userImage', 
              'thumbsUpCount',
              'replyContent', 
              'repliedAt',
              'appVersion'], axis=1)

df = df.rename(columns={
              "userName" : "author_name",
              "content" : "review_text",
              "score" : "rating",
              "reviewCreatedVersion" : "app_version",
              "at" : "review_date"})

# reorder

df = df[["author_name",
        "rating", 
        "review_text", 
        "review_date", 
        "app_version"]]

df["platform"] = "android" 

df.to_csv("clean_google_play.csv", index=False)
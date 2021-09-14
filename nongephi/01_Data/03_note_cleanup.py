import pandas as pd
import numpy as np

df = pd.read_csv("./joyce_notes_titles.csv", sep='|')
print("done reading!")
print(df.info(verbose=True, null_counts=True))

# Drop blank playlists
# df['link_id'].replace('', np.nan, inplace=True)
# df.dropna(subset=['link_id'], inplace=True)

# Strip new lines OLD ATTEMPTS
# df = df.replace(r'\\n', ' ', regex=True)
# df['text_string'] = df['text_string'].astype(str)
# df['text_string'].replace(r'\\r', ' ', regex=True, inplace=True)
# df['text_string'] = df['text_string'].str.rstrip()
# df['text_string'].replace(r'\n', ' ', regex=True, inplace=True)
# df['text_string'] = df['text_string'].str.decode('utf-8', 'ignore')
# df['text_string'] = df['text_string'].apply(lambda x: "'" + str(x) + "'")
# df.update('"' + df[['text_string']].astype(str) + '"')

# Strip new lines WORKING
# PLEASE READ: once this was done, needed to search for /n in sublime-text
# replaced these with spaces to correct issue
df['text_string'] = df['text_string'].str.encode('ascii', 'ignore')

df.to_csv('joyce_notes_titles_clean.csv', index=False, sep='|')


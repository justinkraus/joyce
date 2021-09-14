import pandas as pd
from itertools import combinations


#create combined df with just museum and topics
df = pd.read_csv("./joyce_notes_edges1.csv")
print("done reading!")

def combine(batch):
    """Combine all products within one batch into pairs"""
    return pd.Series(list(combinations(set(batch), 2)))

edges = df.groupby('note_label')['ID'].apply(combine).value_counts()
edges = edges.reset_index()
edges = pd.concat([edges, edges['index'].apply(pd.Series)], axis=1)
edges.drop(['index'], axis=1, inplace=True)
edges.columns = 'Weight','Source','Target'

print(edges.head(20))
edges.to_csv('top_notes_connections.csv', mode='a', encoding='utf-8', index=False)

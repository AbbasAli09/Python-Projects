import pandas as pd
import plotly.express as px from wordcloud 
import WordCloud
import matplotlib.pyplot as plt from textblob
import TextBlob
import spacy from collections
import defaultdict from collections 
import Counter from sklearn.feature_extraction.text 
import CountVectorizer from sklearn.decomposition 
import LatentDirichletAllocation

nlp = spacy.load('en_core_web_sm')

data = pd.read_csv("articles.csv", encoding='latin-1')
print(data.head())

# Combine all titles into a single string
titles_text = ' '.join(data['Title'])

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)

# Plot the Word Cloud
fig = px.imshow(wordcloud, title='Word Cloud of Titles')
fig.update_layout(showlegend=False)
fig.show()


# Sentiment Analysis
data['Sentiment'] = data['Article'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Sentiment Distribution
fig = px.histogram(data, x='Sentiment', title='Sentiment Distribution')
fig.show()


# NER
def extract_named_entities(text):
    doc = nlp(text)
    entities = defaultdict(list)
    for ent in doc.ents:
        entities[ent.label_].append(ent.text)
    return dict(entities)

data['Named_Entities'] = data['Article'].apply(extract_named_entities)

# Visualize NER
entity_counts = Counter(entity for entities in data['Named_Entities'] for entity in entities)
entity_df = pd.DataFrame.from_dict(entity_counts, orient='index').reset_index()
entity_df.columns = ['Entity', 'Count']

fig = px.bar(entity_df.head(10), x='Entity', y='Count', title='Top 10 Named Entities')
fig.show()


# Topic Modeling
vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
tf = vectorizer.fit_transform(data['Article'])
lda_model = LatentDirichletAllocation(n_components=5, random_state=42)
lda_topic_matrix = lda_model.fit_transform(tf)

# Visualize topics
topic_names = ["Topic " + str(i) for i in range(lda_model.n_components)]
data['Dominant_Topic'] = [topic_names[i] for i in lda_topic_matrix.argmax(axis=1)]

fig = px.bar(data['Dominant_Topic'].value_counts().reset_index(), x='index', y='Dominant_Topic', title='Topic Distribution')
fig.show()

#Summary
# Text Analysis involves various techniques such as text preprocessing, sentiment analysis, named entity recognition, topic modelling,
# and text classification. Text analysis plays a crucial role in understanding and making sense of large volumes of text data,
# which is prevalent in various domains, including news articles, social media, customer reviews, and more. 

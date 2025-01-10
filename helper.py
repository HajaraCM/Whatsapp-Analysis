from urlextract import URLExtract
extractor=URLExtract()
from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import re
import emoji


stop_words = set(stopwords.words('english'))

def fetch_stats(user_type,df):
     
    if user_type != 'Overall':
        df = df[df['users'] ==user_type]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['messages']:
        words.extend(message.split())
    links=[]
    for msg in df['messages']:
        links.extend(extractor.find_urls(msg))
    return num_messages, len(words),len(links)

def most_busy_users(df):
    x = df['users'].value_counts().head()
    filtered=df[df['users'] != 'group_notification']
    percent= round(filtered['users'].value_counts()/filtered.shape[0]*100,2).reset_index().rename(columns={'count':'percent'})
    return x,percent
def word_cloud(user_type,df):
    if user_type != 'Overall':
        df = df[df['users'] == user_type]
    temp= df[df['users'] != 'group_notification']
    text = " ".join(temp['messages'].astype(str)) 
    wc= WordCloud(
    width=2000, height=1000, background_color='white',
    stopwords = stop_words, colormap='Greens',
    min_font_size = 10
    ).generate(text)
    
    return wc
def most_common_words(user_type,df):
    words=[]
    if user_type != 'Overall':
        df = df[df['users'] == user_type]
    temp= df[df['users'] != 'group_notification']
    for msg in temp['messages']:
        cleaned=re.sub(r'[^\w\s]', '', msg)
        for word in cleaned.lower().split():
            if word not in stop_words:
                words.append(word)
               

    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return  most_common_df

def emoji_helper(user_type,df):
    if user_type != 'Overall':
        df = df[df['users'] == user_type]
    emojis = []
    for message in df['messages']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

def monthly_timeline(user_type,df):

    if user_type!= 'Overall':
        df = df[df['users'] == user_type]

    timeline = df.groupby(['year', 'month', 'month_name']).count()['messages'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month_name'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline
def daily_timeline(user_type,df):

    if user_type != 'Overall':
        df = df[df['users'] == user_type]

    daily_timeline = df.groupby('only_date').count()['messages'].reset_index()

    return daily_timeline

def week_activity_map(user_type,df):

    if user_type != 'Overall':
        df = df[df['users'] == user_type]

    return df['day_name'].value_counts()

def month_activity_map(user_type,df):

    if user_type != 'Overall':
        df = df[df['users'] == user_type]

    return df['month_name'].value_counts()

def activity_heatmap(user_type,df):


    if user_type != 'Overall':

        df = df[df['users'] ==user_type]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='messages', aggfunc='count').fillna(0)

    return user_heatmap







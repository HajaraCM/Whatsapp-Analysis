import pandas as pd
import re
def preprocess(data):

        
    pattern = r"(\d{2}/\d{2}/\d{4},\s\d{1,2}:\d{2}\s?[APMapm]{2})\s*-\s*(.*)"

    # Use re.findall to capture all matches of date, time, and message
    matches = re.findall(pattern, data)

    # Store date-time and message in separate lists
    date_times = []
    messages = []

    # Loop through each match and store in corresponding lists
    for date_time, msg in matches:
        date_times.append(date_time)
        cleaned_message = msg.replace('-', '').strip()
        messages.append(msg)
    df=pd.DataFrame({'user_message':messages,'message_date':date_times})
    df['message_date'] = pd.to_datetime(df['message_date'],format='%d/%m/%Y, %I:%M %p')    
    df=df.rename(columns={'message_date':'date'})
    def clean_dataset(line):
        line = re.sub(r'^[^\w\s:]+:', 'hajara:', line)  # Matches emojis or non-alphanumeric characters as a name
        # Replace the numeric sender identifier with "user"
        line = re.sub(r'^\+?\d[\d\s]*:', 'user:', line)
        # Remove numbers after @, leaving only "@"
        line = re.sub(r'@\+?\d[\d\s]*', '@', line)
        return line
    df['user_message']= df['user_message'].apply(clean_dataset)

    users=[]
    messages=[]
    for msg in df['user_message']:
        entry = re.split('([\w\W]+?):\s', msg)
        if len(entry) > 2:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
            
    df['users']=users
    df['messages']=messages
    df.drop('user_message',axis=1,inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['only_date']=df['date'].dt.date

    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df
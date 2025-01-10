import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title('Whatsapp Chat Analyzer')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)
    

    user_list= df['users'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user=st.sidebar.selectbox('Choose Analysis Type: User or Overall',user_list)
    num_msg,words,links = helper.fetch_stats(selected_user,df)
    if st.sidebar.button('Show Analysis'):
        st.title("Top Statistics")
        col1,col2,col3=st.columns(3)
        with col1:
            st.header('Total meassages')
            st.title(num_msg)
        with col2:
            st.header('Total Words')
            st.title(words)
        with col3:
             st.header('Links Shared')
             st.title(links)
        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['messages'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['messages'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        if selected_user=='Overall':
            st.title('Most Busy Users')
            x,percent=helper.most_busy_users(df)
            fig,ax=plt.subplots()

    
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index,x.values,color=['#5A4FCF', '#A65AC9', '#5E8A7E', '#FF7F0E', '#8C564B'])
                plt.xticks(rotation=90)
                st.pyplot(fig)
            with col2:
                st.dataframe(percent)
            # WordCloud
        st.title("Wordcloud")
        df_wc = helper.word_cloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)
        st.title('Most Common Words')
        common_df= helper.most_common_words(selected_user,df)
        fig,ax = plt.subplots()

        ax.barh(common_df[0],common_df[1],color="#D4A1E7")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        emoji_df=helper.emoji_helper(selected_user,df)
        st.title('Emoji Analysis')
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax=plt.subplots()
            ax.pie(emoji_df[1],labels=emoji_df[0],autopct="%.2f%%",startangle=90)
            st.pyplot(fig)



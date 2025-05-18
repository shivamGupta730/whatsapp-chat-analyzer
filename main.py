import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions

st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

def set_custom_page_style():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1633675254245-efd890d087b8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8d2hhdHNhcHB8ZW58MHx8MHx8fDA%3D");
            background-attachment: fixed;
            background-size: cover;
        }
        .main {
            background-color: rgba(0, 0, 0, 0.65);
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: black !important;
            font-weight: bold !important;
            text-align: center;
            transition: color 0.3s ease;
        }
        h1:hover, h2:hover, h3:hover {
            color: #333 !important;
        }
        .stMetric label, .stMetric div {
            color: white;
        }
        .css-10trblm, .css-1v0mbdj, .stRadio label {
            color: white !important;
        }
        .stDataFrame {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_custom_page_style()

st.title('WhatsApp Chat Analyzer')
file = st.file_uploader("Choose a WhatsApp chat file (.txt)")

if file:
    df = functions.generateDataFrame(file)
    try:
        dayfirst = st.radio("Select Date Format in text file:", ('dd-mm-yy', 'mm-dd-yy'))
        dayfirst = True if dayfirst == 'dd-mm-yy' else False

        users = functions.getUsers(df)
        users_s = st.sidebar.selectbox("Select User to View Analysis", users)
        selected_user = ""

        if st.sidebar.button("Show Analysis"):
            selected_user = users_s
            st.title("Showing Results for : " + selected_user)

            df = functions.PreProcess(df, dayfirst)
            if selected_user != "Everyone":
                df = df[df['User'] == selected_user]

            df, media_cnt, deleted_msgs_cnt, links_cnt, word_count, msg_count = functions.getStats(df)

            st.markdown("## 📊 Chat Statistics")
            stats_c = ["Total Messages", "Total Words", "Media Shared", "Links Shared", "Messages Deleted"]
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1: st.subheader(stats_c[0]); st.title(msg_count)
            with c2: st.subheader(stats_c[1]); st.title(word_count)
            with c3: st.subheader(stats_c[2]); st.title(media_cnt)
            with c4: st.subheader(stats_c[3]); st.title(links_cnt)
            with c5: st.subheader(stats_c[4]); st.title(deleted_msgs_cnt)

            if selected_user == 'Everyone':
                st.markdown("## 👥 Messaging Frequency")
                st.subheader('Messaging Percentage Count of Users')
                x = df['User'].value_counts().head()
                name = x.index
                count = x.values

                col1, col2 = st.columns(2)
                with col1:
                    percent_df = round((df['User'].value_counts() / df.shape[0]) * 100, 2).reset_index()
                    percent_df.columns = ['User', 'Percent']
                    st.dataframe(percent_df)
                with col2:
                    fig, ax = plt.subplots()
                    ax.bar(name, count, color='skyblue')
                    ax.set_xlabel("Users")
                    ax.set_ylabel("Messages Sent")
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)

            st.markdown("## 😄 Emoji Analysis")
            emojiDF = functions.getEmoji(df)
            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(emojiDF)
            with col2:
                fig, ax = plt.subplots()
                ax.pie(emojiDF[1].head(), labels=emojiDF[0].head(), autopct="%0.2f", shadow=True)
                st.pyplot(fig)

            st.markdown('## 🗣 Most Frequent Words Used In Chat')
            commonWord = functions.MostCommonWords(df)
            fig, ax = plt.subplots()
            ax.bar(commonWord[0], commonWord[1], color='orange')
            ax.set_xlabel("Words")
            ax.set_ylabel("Frequency")
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            st.markdown('## 📅 Monthly Timeline')
            timeline = functions.getMonthlyTimeline(df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['Message'], marker='o')
            ax.set_xlabel("Month")
            ax.set_ylabel("Messages Sent")
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            st.markdown('## 📆 Daily Timeline')
            functions.dailytimeline(df)

            st.markdown('## 📈 Most Busy Days')
            functions.WeekAct(df)
            st.markdown('## 📈 Most Busy Months')
            functions.MonthAct(df)

            st.markdown("## ☁️ Wordcloud")
            df_wc = functions.create_wordcloud(df)
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            ax.axis("off")
            st.pyplot(fig)

            st.markdown("## 🔥 Weekly Activity Map")
            user_heatmap = functions.activity_heatmap(df)
            fig, ax = plt.subplots()
            sns.heatmap(user_heatmap, cmap="YlGnBu", ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error("Unable to Process Your Request. Please check your file and try again.")

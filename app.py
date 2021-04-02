import twint
import streamlit as st
import pandas as pd
import os
import base64
import os.path
import datetime

today = datetime.date.today()




def get_tweet(username,limit,lang,since):
    twint.output=[]
    c = twint.Config()
    c.Username = username
    c.Limit = limit
    c.Store_csv = True
    c.Output = "none.csv"
    c.Lang = "en"
   # c.Translate = True
    #c.TranslateDest = "fr"
    twint.run.Search(c)
    
def get_tweet_search(search,limit,lang,since):
    twint.output=[]
    c = twint.Config()
    c.Search = search
    c.Limit = limit
    c.Store_csv = True
    c.Output = "none.csv"
    c.Lang = "en"
    c.Since = since
   # c.Translate = True
    #c.TranslateDest = "fr"
    twint.run.Search(c)    
    
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'  
    
    return href


def main():
    st.write("# Generate Tweet Datasets !")
    st.write("[By Régis Amon](https://www.linkedin.com/in/r%C3%A9gis-amon-87669665/)")
    st.write("[Using the wonderfull twint library by twintproject](https://github.com/twintproject/twint/tree/master/twint)")
    
    search =None
    username=None
    
    search_type = st.radio('User or search',["user","search"])
    if search_type == "user":

          username = st.text_input("Enter tweet account")
    elif search_type == "search":
          search = st.text_input("Enter a search or hashtag")
          
    #username = st.text_input("username")
    limit = st.slider("Limit of tweets", 60, 3000, 500,step=20)
    since = st.date_input('Since',max_value=today)
    since = str(since)
    lang='en'
    

        


    if username is not None:
        #st.button(("Get tweets"))
        if st.button("Get tweets"):
            
            
    
            if os.path.isfile('none.csv'):
                os.remove('none.csv')
            else:
                print ("File not exist")
                
          
       
            #st.write("### Word cloud")
            
                st.write(get_tweet(username,limit,lang,since), use_column_width=True)
                df = pd.read_csv("none.csv")
                st.dataframe(df)
                #st.write("Right click on the image then choose ***Save as*** to download the Wordcloud")
                #st.balloons()
                
                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                
    if search is not None:
        if st.button("Get search"):
            
            
    
            if os.path.isfile('none.csv'):
                os.remove('none.csv')
            else:
                print ("File not exist")
                
          
       
            #st.write("### Word cloud")
            
                st.write(get_tweet_search(search,limit,lang,since), use_column_width=True)
                df = pd.read_csv("none.csv")
                st.dataframe(df)
                #st.write("Right click on the image then choose ***Save as*** to download the Wordcloud")
                #st.balloons()
                
                st.markdown(get_table_download_link(df), unsafe_allow_html=True)

    
if __name__=="__main__":
    main()

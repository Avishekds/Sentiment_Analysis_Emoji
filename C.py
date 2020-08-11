import streamlit as st
# NLP Pkgs
from textblob import TextBlob
import pandas as pd 
# Emoji
import emoji

# Web Scraping Pkg

from urllib.request import urlopen

# Fetch Text From Url
@st.cache
def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text




def main():
	"""Sentiment Analysis Emoji App """

	st.title("Text Sentiment Analysis & Emoji App")

	activities = ["Sentiment","Emoji App","About"]
	choice = st.sidebar.selectbox("Choice",activities)

	if choice == 'Sentiment':
		st.subheader("Sentiment Analysis")
		st.write(emoji.emojize(':red_heart:' ,use_aliases=True))
		raw_text = st.text_area("Enter Your Text","Type Here")
		if st.button("Analyze"):
			blob = TextBlob(raw_text)
			result = blob.sentiment.polarity
			if result > 0.0:
				
				st.write('Positive')
			elif result < 0.0:
				
				st.write('Negative')
			else:
				st.write('Neutral')
			st.info("Polarity Score is:: {}".format(result))

	if choice == 'Emoji App':
		st.subheader("Analyze your text with emoji")
		raw_text = st.text_area("Enter your text")
		
		if st.button("Analyze"):                         
			blob = TextBlob(raw_text)
			result = blob.sentiment.polarity
			if result <=-0.1 and result >=-0.3:
				custom_emoji = ':cry:'
				st.write(emoji.emojize(custom_emoji,use_aliases=True))
			elif result <-0.3:
				custom_emoji = ':disappointed:'
				st.write(emoji.emojize(custom_emoji,use_aliases=True))
			elif result ==0:
				st.write(emoji.emojize(':expressionless:',use_aliases=True))
			elif result >=1 and result <=5:
				st.write (emoji.emojize(':smile:',use_aliases=True))
			else:
				st.write (emoji.emojize(':grinning_face_with_smiling_eyes:',use_aliases=True))
			

	if choice == 'About':
		st.subheader("About:Sentiment Analysis & Emoji App")
		st.info("Built with Python")
		st.text("Developed by Avishek Das")

            

if __name__ == '__main__':
    main()
    
                
            
                
           
                

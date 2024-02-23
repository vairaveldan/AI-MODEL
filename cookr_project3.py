#from dotenv import load_dotenv load_dotenv()
import streamlit as st 
import os
import google.generativeai as genai
os.environ['_GOOGLE_API_KEY']="AIzaSyAi2Fv-6LoIFBCerysJMqWY8XOkLjIojw4"
genai.configure(api_key=os.environ['_GOOGLE_API_KEY'])
## function to load Gemini Pro model and get repsonse 
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat (history=[])
#def get_gemini_response(question):
a="give me a great description about "
c=" in 2-3 lines"
d="\n\n"
f="""Statement - Kitchen Description Builder. 
Description: Build algorithms to automate text generation for the kitchen type based 
on the menus that kitchen offers. The summary should be 2-3 lines in the mobile screen width.
For instance:This home chef specializes purely Punjabi dishes specifically country / villagestyle dishes. Generally, these dishes are made with organic ingredients.
This kitchen brings the best out of Keralite food, very authentic and delicious 
specials.
Prema is passionate about making delicacies of Italian food and enjoys cooking 
unique culinary specials of Italy."""
def get_gemini_response(question):
  response=chat.send_message(a+question+c+d+f, stream=True)
  return response
#initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Food Description Creator")
# Initialize session state for chat history if it doesn't exist if 'chat_history' not in st.session_state:
input=st.text_input("Input: ", key="input")
submit=st.button("Provide Description")
st.session_state['combine']=""
if submit and input:
 response=get_gemini_response(input)
## Add user query and response to session chat history  
 st.subheader("Your Description")
 for i in response:
  st.session_state['combine']+=i.text
 st.write(st.session_state['combine'])
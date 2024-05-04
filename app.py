from dotenv import load_dotenv
load_dotenv()  ##loading all the environment variables


import streamlit as st
import os 
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are a YouTube video summarizer. You will be taking the transcript text and summarizing the entire video and providing 
the important summary in points within 250 words. Please provide the summary of the text geven here :  """

## gettimg the transcript text from the youtube video
def extract_transcript(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        print(video_id)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " "
        for i in transcript_text:
            transcript += " " + i['text']   

        return transcript



    except Exception as e: 
        raise e
    
## generating the summary of the video transcript text
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text


st.title("YouTube Video summarizer")
youtube_link = st.text_input("Enter the youtube video link here : ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Summarize the video"):
    transcript_text=extract_transcript(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Summary of the video : ")
        st.write(summary)





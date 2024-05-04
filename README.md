# Video-Transcribe-Summarizer

A brief description about the project

## Introduction 
Welcome to my Video Transcribe Summarizer application! 🎥✨

Do you often find yourself overwhelmed by lengthy videos and wishing for a quicker way to grasp their content? Look no further! I made this application using the Generative AI and Python to simplify your video-watching experience.
You simply have to provide the URL of the video you'd like to summarize,and within moments, you'll receive a concise summary of the video in easy-to-read bullet points, along with a handy thumbnail to give you a visual preview.

## Problems it solved 
 - This can save your enough time by summarizing lengthy videos.
 - Facilitates content filtering.
 - Boosts productivity by providing quick insights.
- Supports studying, research, and reference.
- Translate the entire video into concise bullet points.

## Deployment 
To deploy this project run 

First install the python and create a virtual environment

```bash
conda create -p venv python==3.10 -y
```
activate the virtual environment 

```bash
conda activate venv/
```
```bash 
pip install -r requirements.txt
```
Update your API key in .env file

And then run the following command 

```bash
streamlit run app.py
```





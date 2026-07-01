import streamlit as st
import json
import os

# Page styling
st.set_page_config(page_title="Smart Content Hub", layout="wide")

st.title("🚀 Smart Content Command Center")
st.subheader("Your background automation engine feeds this clean stream.")

DATA_PATH = "/workspaces/codespaces-blank/youtube_data.json"

if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r") as file:
        try:
            raw_data = json.load(file)
            
            # 🛡️ SMART UNPACKING: Reach inside n8n's container boxes
            videos = []
            if isinstance(raw_data, list) and len(raw_data) > 0:
                first_item = raw_data[0]
                # If videos are hidden inside an inner list or a "data" key
                if isinstance(first_item, list):
                    videos = first_item
                elif isinstance(first_item, dict) and "data" in first_item:
                    videos = first_item["data"]
                else:
                    videos = raw_data
            elif isinstance(raw_data, dict) and "data" in raw_data:
                videos = raw_data["data"]

            if not videos:
                st.info("The data structure is empty. Re-run your n8n workflow pipeline!")
            else:
                st.success(f"⚡ Loaded {len(videos)} videos chronologically from your automated cache.")
                
                # Loop through and display each video beautifully
                for video in videos:
                    title = video.get("title", "No Title Available")
                    link = video.get("link", "#")
                    thumbnail = video.get("thumbnail", "https://via.placeholder.com/320x180")
                    channel = video.get("author", "Unknown Creator")
                    published_at = video.get("pubDate", "Unknown Date")
                    
                    # Clean up the timestamp layout if it exists (e.g., 2026-06-22)
                    if "T" in published_at:
                        published_at = published_at.split("T")[0]
                    
                    # Row container layout
                    with st.container():
                        col1, col2 = st.columns([1, 2])
                        
                        with col1:
                            st.image(thumbnail, use_container_width=True)
                            
                        with col2:
                            st.markdown(f"### {title}")
                            st.markdown(f"📺 **Channel:** `{channel}`  |  📅 **Published:** {published_at}")
                            st.markdown(f"🔗 [Watch on YouTube]({link})")
                            st.write("---")
                            
        except json.JSONDecodeError:
            st.error("Error reading your data file. It looks like it didn't save correctly.")
else:
    st.warning("Data file not found. Make sure your n8n workflow ran successfully!")
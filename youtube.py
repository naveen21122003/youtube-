import streamlit as st
from pytube import YouTube

def download_youtube_video(video_url, save_path):
    try:
        yt = YouTube(video_url)
        st.write("Downloading video...")
        yt.streams.get_highest_resolution().download(save_path)
        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("YouTube Video Downloader")

    st.markdown("""
    This app allows you to download YouTube videos. Simply paste the URL of the video you want to download and click the download button.
    """)

    video_url = st.text_input("Enter YouTube Video URL:")
    save_path = st.text_input("Enter path to save the video (leave empty to save in current directory):")

    if st.button("Download"):
        if video_url:
            download_youtube_video(video_url, save_path)
        else:
            st.warning("Please enter a YouTube video URL.")

if __name__ == "__main__":
    main()

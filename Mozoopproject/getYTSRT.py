from pytube import YouTube
import pysrt  # Use `pip install pysrt` if you haven't already

def download_video_and_captions(video_url: str, output_path: str):
    """
    Downloads a YouTube video and its captions in SRT format.
    
    Args:
        video_url (str): The URL of the YouTube video.
        output_path (str): Directory where the video and captions should be saved.

    Returns:
        str: File paths for the downloaded video and caption file.
    """
    try:
        # Initialize YouTube object
        yt = YouTube(video_url)
        
        # Download video
        video_stream = yt.streams.get_highest_resolution()
        video_file = video_stream.download(output_path=output_path)
        print(f"Downloaded video to: {video_file}")
        
        # Check if captions are available
        if not yt.captions:
            print("No captions available for this video.")
            return video_file, None
        
        # Download English captions, or the first available if English isn't present
        caption = yt.captions.get_by_language_code('en') or yt.captions.all()[0]
        srt_captions = caption.generate_srt_captions()
        
        # Save captions to an .srt file
        caption_file = f"{output_path}/{yt.title}.srt"
        with open(caption_file, "w", encoding="utf-8") as file:
            file.write(srt_captions)
        
        print(f"Downloaded captions to: {caption_file}")
        return video_file, caption_file
    
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Example usage:
video_url = 'https://www.youtube.com/watch?v=2I1qPBFf-vs'  # Replace with your YouTube video URL
output_path = './downloads'  # Directory for saving the files
download_video_and_captions(video_url, output_path)

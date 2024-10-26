from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import os

# Assumptions:
# - "test_video.mp4": sample video file in MP4 format
# - "test_audio.mp3": sample audio file in MP3 format
# - "image_seq_dir": directory containing a sequence of images (image_1.png, image_2.png, etc.)

# Ensure 'output' directory exists
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Video and Audio Loading Tests

def test_video_loading():
    """Test loading a video file"""
    clip = VideoFileClip("ff.mp4")
    if clip:
        print("video loaded !!!")
    assert clip is not None, "Video loading failed"
    clip.close()

def test_audio_loading():
    """Test loading an audio file"""
    audio = AudioFileClip("song.mp3")
    if audio:
        print("audio loaded !!!")

    assert audio is not None, "Audio loading failed"
    audio.close()

def test_audio_extraction():
    """Test extracting audio from a video clip"""
    video = VideoFileClip("ff.mp4")
    audio = video.audio
    if audio:
        print("audio extracted !!!")
    assert audio is not None, "Audio extraction failed"
    audio.write_audiofile("output_audio.mp3")
    assert os.path.exists("output_audio.mp3"), "Audio file not created"
    audio.close()
    video.close()
    os.remove("output_audio.mp3")

# Basic Video Editing Tests

def test_video_trimming():
    """Test trimming a video clip and save to 'output' directory."""
    video = VideoFileClip("ff.mp4").subclip(0, 5)
    output_path = os.path.join(output_dir, "trimmed_video.mp4")
    video.write_videofile(output_path)
    assert int(video.duration) == 5, "Trimming failed"
    video.close()

def test_video_concatenation():
    """Test concatenating multiple video clips and save to 'output' directory."""
    clip1 = VideoFileClip("ff.mp4").subclip(0, 3)
    clip2 = VideoFileClip("avg.mp4").subclip(0, 3)
    concatenated_clip = concatenate_videoclips([clip1, clip2])
    output_path = os.path.join(output_dir, "concatenated_video.mp4")
    concatenated_clip.write_videofile(output_path)
    assert int(concatenated_clip.duration) == 6, "Concatenation failed"
    clip1.close()
    clip2.close()
    concatenated_clip.close()

def test_subclip_creation():
    """Test creating a subclip of a video and save to 'output' directory."""
    video = VideoFileClip("ff.mp4")
    subclip = video.subclip(2, 7)
    output_path = os.path.join(output_dir, "subclip_video.mp4")
    subclip.write_videofile(output_path)
    assert int(subclip.duration) == 5, "Subclip creation failed"
    video.close()
    subclip.close()

# Text and Overlay Effects Tests



def test_transition_effects():
    """Test adding fade-in and fade-out transitions and save to 'output' directory."""
    clip = VideoFileClip("ff.mp4").subclip(0, 5).fadein(1).fadeout(1)
    
    output_path = os.path.join(output_dir, "output_transition_effects.mp4")
    clip.write_videofile(output_path)
    
    assert int(clip.duration) == 5, "Transition effect failed"
    
    # Cleanup
    clip.close()
    os.remove(output_path)

def test_text_overlay():
    """Test adding text overlay to a video and save to 'output' directory."""
    video = VideoFileClip("ff.mp4").subclip(0, 5)
    txt_clip = TextClip("Sample Text", fontsize=24, color='white').set_position('center').set_duration(5)
    result = CompositeVideoClip([video, txt_clip])
    
    output_path = os.path.join(output_dir, "output_text_overlay.mp4")
    result.write_videofile(output_path)
    
    assert os.path.exists(output_path), "Text overlay failed"
    
    # Cleanup
    video.close()
    txt_clip.close()
    result.close()
    os.remove(output_path)

def test_image_sequence_to_video():
    """Test converting image sequence to video clip"""
    img_sequence = [f"image_seq_dir/image_{i}.png" for i in range(1, 6)]
    clip = VideoFileClip(img_sequence[0]).set_duration(1)  # Mocking image sequence video creation
    clip.write_videofile("output_image_seq.mp4")
    assert os.path.exists("output_image_seq.mp4"), "Image sequence to video conversion failed"
    clip.close()
    os.remove("output_image_seq.mp4")

# Audio Editing Tests

def test_volume_adjustment():
    """Test applying volume adjustment to audio"""
    audio = AudioFileClip("test_audio.mp3")
    modified_audio = audio.volumex(0.5)
    assert audio.duration > 0, "Volume adjustment failed"
    audio.close()
    modified_audio.close()

# Screenshot and Thumbnail Generation Tests

def test_capture_frame():
    """Test capturing a frame from a video"""
    video = VideoFileClip("test_video.mp4")
    frame = video.get_frame(2)  # Get frame at 2 seconds
    assert frame is not None, "Frame capture failed"
    video.close()

# Video Generation and Scripting Tests

def test_video_script_creation():
    """Test video creation through scripting"""
    clip1 = VideoFileClip("test_video.mp4").subclip(0, 3)
    clip2 = VideoFileClip("test_video.mp4").subclip(3, 6)
    final_clip = concatenate_videoclips([clip1, clip2])
    final_clip.write_videofile("output_scripted_video.mp4")
    assert os.path.exists("output_scripted_video.mp4"), "Video scripting failed"
    clip1.close()
    clip2.close()
    final_clip.close()
    os.remove("output_scripted_video.mp4")

# Exporting Options Tests

def test_video_export():
    """Test exporting a video in a specific format and resolution"""
    video = VideoFileClip("test_video.mp4").subclip(0, 5)
    video.write_videofile("output_exported.mp4", codec='libx264', bitrate="500k", fps=24)
    assert os.path.exists("output_exported.mp4"), "Video export failed"
    video.close()
    os.remove("output_exported.mp4")


# Run all tests
if __name__ == "__main__":
    # test_video_loading()
    # test_audio_loading()
    # test_audio_extraction()

    # test_video_trimming()
    # test_video_concatenation()
    # test_subclip_creation()
    
    # test_text_overlay()
    test_transition_effects()
    # test_image_sequence_to_video()
    # test_volume_adjustment()
    # test_capture_frame()
    # test_video_script_creation()
    # test_video_export()

    print("All tests completed.")



"""

json data = [
c1: {

    "title: "clip1",
    "scenStart: "00:11:25",
    "scenEnd: "00:31:25",
    "description" : "lorem ejdyseuvduvbesbidbejs"
    },
c2: {

    "title: "clip1",
    "scenStart: "00:11:25",
    "scenEnd: "00:31:25",
    "description" : "lorem ejdyseuvduvbesbidbejs"
    },
]

"""
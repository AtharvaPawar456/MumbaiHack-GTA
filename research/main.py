from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
import os
import json
import random

# Sample data in JSON format
# dataJson = [
#     {
#         "title": "The First Meeting",
#         "scenStart": "00:11:26",
#         "scenEnd": "00:11:50",
#         "description": "Farhan and Raju meet Rancho for the first time in the hostel, beginning their journey of friendship as they bond over shared experiences."
#     },
#     {
#         "title": "The 'Aal izz well' Mantra",
#         "scenStart": "00:13:15",
#         "scenEnd": "00:13:20",
#         "description": "Rancho’s mantra 'Aal izz well' encourages a positive outlook, symbolizing their support for each other through challenges."
#     },
#     {
#         "title": "The Exam Night Rescue",
#         "scenStart": "00:52:55",
#         "scenEnd": "00:53:02",
#         "description": "Farhan and Raju attempt to steal the exam paper for Raju, showing their willingness to go to extreme lengths for a friend."
#     },
#     {
#         "title": "The 'Missing' Results",
#         "scenStart": "01:17:27",
#         "scenEnd": "01:17:42",
#         "description": "When Rancho’s name is missing from the results, Farhan and Raju’s deep concern underscores their emotional bond with him."
#     },
#     {
#         "title": "The Rooftop Bonding",
#         "scenStart": "01:17:42",
#         "scenEnd": "01:17:54",
#         "description": "The friends share their feelings on the rooftop, experiencing disappointment together, which strengthens their friendship."
#     },
#     {
#         "title": "The 'Stolen' Photo",
#         "scenStart": "01:35:13",
#         "scenEnd": "01:35:28",
#         "description": "Rancho keeps his promise to stay in touch, demonstrating the power of friendship to transcend time and distance."
#     },
#     {
#         "title": "The Journey to Find Rancho",
#         "scenStart": "01:46:44",
#         "scenEnd": "01:46:55",
#         "description": "Their journey to find Rancho reflects their commitment and determination to reconnect with him, showcasing their enduring friendship."
#     },
#     {
#         "title": "The Reunion and Acceptance",
#         "scenStart": "02:32:49",
#         "scenEnd": "02:33:05",
#         "description": "The emotional culmination of their journey, where they reunite with Rancho and acknowledge their growth and changes."
#     }
# ]

# dataJson = [
#     {
#         "title": "3 Idiots - A Comedy Trailer",
#         "scenStart": "00:03:22.390",
#         "scenEnd": "00:03:38.907",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "Welcome Back Idiots",
#         "scenStart": "00:05:12.375",
#         "scenEnd": "00:05:13.775",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "The Challenge - 5 Years Later",
#         "scenStart": "00:06:16.682",
#         "scenEnd": "00:06:22.961",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "The Bet - A Reunion",
#         "scenStart": "00:06:31.541",
#         "scenEnd": "00:06:34.146",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "The Search Begins - Where is Rancho?",
#         "scenStart": "00:07:21.828",
#         "scenEnd": "00:07:26.828",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "Who is Rancho?",
#         "scenStart": "00:09:40.489",
#         "scenEnd": "00:09:41.609",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "A Different Path",
#         "scenStart": "00:09:44.871",
#         "scenEnd": "00:09:46.871",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "The Race - Societal Pressures",
#         "scenStart": "00:09:48.865",
#         "scenEnd": "00:09:55.169",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "Finding Purpose",
#         "scenStart": "00:10:15.532",
#         "scenEnd": "00:10:19.432",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "Welcome to Hostel Life",
#         "scenStart": "00:10:44.260",
#         "scenEnd": "00:10:50.771",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "Millimeter - The Jack of All Trades",
#         "scenStart": "00:10:54.151",
#         "scenEnd": "00:11:00.096",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "New Friends, New Beginnings",
#         "scenStart": "00:11:26.550",
#         "scenEnd": "00:11:29.170",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "Hostel Camaraderie",
#         "scenStart": "00:11:32.888",
#         "scenEnd": "00:11:34.777",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "The Underwear Incident",
#         "scenStart": "00:11:48.090",
#         "scenEnd": "00:12:02.556",
#         "userPreference": "comedy"
#     },
#     {
#         "title": "The Gift",
#         "scenStart": "00:12:09.945",
#         "scenEnd": "00:12:12.775",
#         "userPreference": "comedy"
#     }
#     ]


dataJson=[
  {
    "title": "Comedy in the Class",
    "scenStart": "00:11:26,550",
    "scenEnd": "00:11:29,170",
    "song_keys": [
      "normaltunes",
      "Losing Your Marbles"
    ]
  },
  {
    "title": "Religious Argument",
    "scenStart": "00:11:34,777",
    "scenEnd": "00:11:38,977",
    "song_keys": [
      "normaltunes",
      "Losing Your Marbles"
    ]
  },
  {
    "title": "Campus Robbery",
    "scenStart": "00:14:01,944",
    "scenEnd": "00:14:05,256",
    "song_keys": [
      "normaltunes",
      "Pouncin"
    ]
  },
  {
    "title": "Counting to 10",
    "scenStart": "00:14:24,802",
    "scenEnd": "00:14:43,334",
    "song_keys": [
      "normaltunes",
      "Quirk"
    ]
  },
  {
    "title": "Aal Izz Well",
    "scenStart": "00:13:15,974",
    "scenEnd": "00:13:20,789",
    "song_keys": [
      "idiots",
      "Aal Izz Well"
    ]
  },
  {
    "title": "The Pen Challenge",
    "scenStart": "00:20:02,588",
    "scenEnd": "00:20:10,071",
    "song_keys": [
      "normaltunes",
      "Observer"
    ]
  },
  {
    "title": "The Pencil Question",
    "scenStart": "00:20:19,444",
    "scenEnd": "00:20:29,658",
    "song_keys": [
      "normaltunes",
      "Observer"
    ]
  },
  {
    "title": "The Cuckoo Bird",
    "scenStart": "00:17:50,207",
    "scenEnd": "00:18:27,549",
    "song_keys": [
      "normaltunes",
      "Tourist"
    ]
  },
  {
    "title": "The Helicopter Project",
    "scenStart": "00:28:01,417",
    "scenEnd": "00:28:15,066",
    "song_keys": [
      "normaltunes",
      "Sesame"
    ]
  },
  {
    "title": "Aal Izz Well Mantra",
    "scenStart": "00:28:31,129",
    "scenEnd": "00:28:40,563",
    "song_keys": [
      "idiots",
      "Aal Izz Well"
    ]
  },
  {
    "title": "The Watchman's Mantra",
    "scenStart": "00:28:40,978",
    "scenEnd": "00:29:16,640",
    "song_keys": [
      "idiots",
      "Aal Izz Well"
    ]
  },
  {
    "title": "The Joy Lobo Helicopter",
    "scenStart": "00:32:57,804",
    "scenEnd": "00:33:15,989",
    "song_keys": [
      "normaltunes",
      "Trabaja"
    ]
  },
  {
    "title": "The Suicide",
    "scenStart": "00:33:49,473",
    "scenEnd": "00:34:07,101",
    "song_keys": [
      "idiots",
      "Give Me Some Sunshine"
    ]
  },
  {
    "title": "The Pressure",
    "scenStart": "00:34:07,272",
    "scenEnd": "00:34:42,843",
    "song_keys": [
      "normaltunes",
      "Trabaja"
    ]
  },
  {
    "title": "The System's Blame",
    "scenStart": "00:35:05,754",
    "scenEnd": "00:35:26,834",
    "song_keys": [
      "normaltunes",
      "Trabaja"
    ]
  },
  {
    "title": "The Free Bird",
    "scenStart": "00:21:23,114",
    "scenEnd": "00:21:39,314",
    "song_keys": [
      "normaltunes",
      "Sesame"
    ]
  },
  {
    "title": "The Machine Debate",
    "scenStart": "00:21:43,567",
    "scenEnd": "00:22:58,682",
    "song_keys": [
      "normaltunes",
      "Observer"
    ]
  },
  {
    "title": "The Uniform Schooling",
    "scenStart": "00:21:07,338",
    "scenEnd": "00:21:23,017",
    "song_keys": [
      "normaltunes",
      "Pouncin"
    ]
  },
  {
    "title": "The Bathroom Battle",
    "scenStart": "00:24:50,565",
    "scenEnd": "00:24:56,243",
    "song_keys": [
      "normaltunes",
      "Quirk"
    ]
  },
  {
    "title": "The Convocation Date",
    "scenStart": "00:25:15,313",
    "scenEnd": "00:26:03,549",
    "song_keys": [
      "normaltunes",
      "Tourist"
    ]
  }
]
# Define output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Initialize an empty list to store trimmed file names
trimList = []

# audioList = ["songs\Losing Your Marbles - The Soundlings.mp3", "songs\Observer - Dyalla.mp3", "songs\Pouncin and Bouncin - The Soundlings.mp3", "songs\Quirk n Twerk - The Soundlings.mp3", "songs\Sesame - Dyalla.mp3", "songs\Tourist - Dyalla.mp3"]


audioList = {
    "avengerendgame" : {
        "avengers-notify":"songs\AvgEndGameTune\\avengers-notify-55559.mp3",
        "avengers-thor":"songs\AvgEndGameTune\\avengers-thor-49329-62948.mp3",
        "avengers-thor":"songs\AvgEndGameTune\\avengers-thor-49329.mp3",
        "superhero-theme":"songs\AvgEndGameTune\superhero-theme-7963.mp3",
        "vivegam":"songs\AvgEndGameTune\\vivegam-43590.mp3",
    },

    "idiots" : {
        "Aal Izz Well":"songs\IdiotsTune\Aal Izz Well 128 Kbps.mp3",
        "Behti Hawa Sa Tha Woh":"songs\IdiotsTune\Behti Hawa Sa Tha Woh 128 Kbps.mp3",
        "Give Me Some Sunshine":"songs\IdiotsTune\Give Me Some Sunshine 128 Kbps (1).mp3",
        "Jane Nahin Denge":"songs\IdiotsTune\Jane Nahin Denge 128 Kbps.mp3",
        "Zoobi Doobi":"songs\IdiotsTune\Zoobi Doobi 128 Kbps.mp3"},

    "normaltunes" : {
        "Losing Your Marbles":"songs\Losing Your Marbles - The Soundlings.mp3", 
        "Observer":"songs\Observer - Dyalla.mp3", 
        "Pouncin":"songs\Pouncin and Bouncin - The Soundlings.mp3", 
        "Quirk":"songs\Quirk n Twerk - The Soundlings.mp3", 
        "Sesame":"songs\Sesame - Dyalla.mp3", 
        "Tourist":"songs\Tourist - Dyalla.mp3",
        "Trabaja":"songs\Trabaja Duro Juega Duro - Luna Cantina.mp3"
        }
}

def time_to_seconds(time_str: str) -> int:
    """Convert time string 'HH:MM:SS' to seconds."""
    # h, m, s = map(int, time_str.split(':'))
    # return h * 3600 + m * 60 + s

    h, m = map(int, time_str.split(':')[:2])  # Parse hours and minutes
    if ',' in time_str:
        sec, ms = time_str.split(':')[-1].split(',')  # Separate seconds and milliseconds
    else:
        sec, ms = time_str.split(':')[-1].split('.')  # Separate seconds and milliseconds
    return h * 3600 + m*60+int(sec)

# def trim_clips(data_json):
#     """Trim video clips based on provided JSON data and add transitions."""
#     video_file = "idiots.mkv"

#     print(f"Totle Clips : {len(data_json)}")
#     for index, scene in enumerate(data_json):
#         # Convert scene start and end times to seconds
#         start_time = time_to_seconds(scene["scenStart"])
#         end_time = time_to_seconds(scene["scenEnd"])
        
#         # Trim the video clip and apply transitions
#         trimmed_clip = VideoFileClip(video_file).subclip(start_time, end_time).fadein(1).fadeout(1)
        
#         # Create a filename for the trimmed clip
#         trimmed_file_name = f"trim{index + 1}.mp4"
#         trimmed_clip.write_videofile(os.path.join(output_dir, trimmed_file_name), codec="libx264")
        
#         # Append the trimmed file name to the list
#         trimList.append(trimmed_file_name)
        
#         # Close the trimmed clip
#         trimmed_clip.close()

def trim_clips(data_json):
    """Trim video clips based on provided JSON data with a maximum duration of 5 seconds and add transitions."""
    video_file = "idiots.mkv"

    print(f"Total Clips: {len(data_json)}")
    for index, scene in enumerate(data_json):
        # Convert scene start and end times to seconds
        start_time = time_to_seconds(scene["scenStart"])
        end_time = time_to_seconds(scene["scenEnd"])
        
        # Limit clip duration to a maximum of 5 seconds
        random_number = random.randint(5, 10)
        if end_time - start_time > random_number:
            end_time = start_time + random_number
        
        # Trim the video clip and apply transitions
        trimmed_clip = VideoFileClip(video_file).subclip(start_time, end_time).fadein(1).fadeout(1)
        try:
            audio_file =  audioList[scene["song_keys"][0]][scene["song_keys"][1]]
            audio_clip = AudioFileClip(audio_file)

            # Set audio duration to match the final video
            audio_duration = trimmed_clip.duration
            audio_trimmed = audio_clip.subclip(0, min(audio_duration, audio_clip.duration))
            
            trimmed_clip=trimmed_clip.set_audio(audio_trimmed)
        except Exception as e:
            print(e)
        # Create a filename for the trimmed clip
        trimmed_file_name = f"trim{index + 1}.mp4"
        trimmed_clip.write_videofile(os.path.join(output_dir, trimmed_file_name), codec="libx264")
        
        # Append the trimmed file name to the list
        trimList.append(trimmed_file_name)
        
        # Close the trimmed clip
        trimmed_clip.close()


def concatenate_clips(trim_list):
    """Concatenate trimmed clips into a single video file."""
    clips = [VideoFileClip(os.path.join(output_dir, trim_file)) for trim_file in trim_list]
    full_video = concatenate_videoclips(clips)
    
    # # Randomly select an audio file from audioList
    # audio_file = random.choice(audioList)
    # audio_clip = AudioFileClip(audio_file)

    # # Set audio duration to match the final video
    # audio_duration = full_video.duration
    # audio_trimmed = audio_clip.subclip(0, min(audio_duration, audio_clip.duration))

    # # Set the audio of the full video
    # full_video = full_video.set_audio(audio_trimmed)

    # Save the concatenated video with audio
    full_output_path = os.path.join(output_dir, "full_video.mp4")
    full_video.write_videofile(full_output_path, codec="libx264")

    # Close all clips
    for clip in clips:
        clip.close()
    
    # # Close the audio clip
    # audio_trimmed.close()
    # audio_clip.close()

# Run the trimming and concatenation process
trim_clips(dataJson)
print(f"{'-'*50}\nMakeing Final Trailer...\n\n")
concatenate_clips(trimList)

# Delete all trimmed files
for trimmed_file in trimList:
    os.remove(os.path.join(output_dir, trimmed_file))

print("Video processing completed successfully!")

# Here we will write Text to audion logic 
# we will use Eleven labs Api
# Eleven labs Text to speech python in the url for the documnetation
# url(https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming)
# Than pip install elevenlabs

# this pasted from the documentation we will customize it according to our needs 
import os
# import uuid
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

load_dotenv()

elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

# 7 here we will give argument (folder:str)
# text: str → text is a string
# folder: str → folder is a string
# -> str → function will return a string
def text_to_speech_file(text: str,folder:str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = elevenlabs.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_flash_v2_5", # use the flash model for low latency
        # Optional voice settings that allow you to customize the output
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=0.9,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    # 7 .saving file : save_file_path = os.path.join(f"user_uploads/{folder}","audio.mp3")
    save_file_path = os.path.join(f"user_uploads/{folder}","audio.mp3")

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path
# text_to_speech_file("Hey I am a good boy and its the python course","47c280b5-b8a9-11f1-a70f-3814281c5033")
# For Testing purpose only text_to_speech_file(user text,folder name)

# To generate api key -> Click My developers->api key ->name



# Dry Run 
'''
# Create the path where the generated audio will be saved
# Example:
# user_uploads/47c280b5-b8a9-11f1-a70f-3814281c5033/audio.mp3
save_file_path = os.path.join(f"user_uploads/{folder}", "audio.mp3")

# Open audio.mp3 in write-binary mode
# "w" = write, "b" = binary
with open(save_file_path, "wb") as f:

    # Take the generated audio from response chunk by chunk
    for chunk in response:

        # If the chunk contains data, write it into the audio file
        if chunk:
            f.write(chunk)

# Show that the audio file was saved successfully
print(f"{save_file_path}: A new audio file was saved successfully!")

# Return the saved audio file path
return save_file_path

# Call the function with user text and folder name
text_to_speech_file(
    "Hey I am a good boy and its the python course",
    "47c280b5-b8a9-11f1-a70f-3814281c5033"
)
'''
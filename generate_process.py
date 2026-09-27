# This file looks for new folders inside user uploads and converts them to reel if they are not already 
# converted.

# Question why we can make this process in main.py 
# So we can do this but it ,it is not a good practice ,
# main.py simply handles the user_uploads
# And generate_process.py will handle the process
import os
# 7 importing our text to audio function 
from text_to_audio import text_to_speech_file
# 7 running this in a loop with time intervals
import time
# 8 
import subprocess

def text_to_audio(folder):
    print("TTA",folder)
    # 7. Taking folders and text
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
        print(text,folder)
        text_to_speech_file(text,folder)
    


def create_reel(folder):
    # This command will generate reel .
    '''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4

    Here ,input.txt is a file that tell the ffmpeg encoder that for how many seconds 
    you want to keep the files and what are the files you are using to generate the reel .
    
    ''' 
# My Command 
    # command = f'''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    print("CR - ", folder)
# ChatGpt Command  
    command = f'''ffmpeg -loop 1 -t 3 -i user_uploads/{folder}/image1.jpg -loop 1 -t 3 -i user_uploads/{folder}/image2.jpg -loop 1 -t 3 -i user_uploads/{folder}/image3.jpg -i user_uploads/{folder}/audio.mp3 -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,zoompan=z='min(zoom+0.0015,1.1)':d=90:s=1080x1920:fps=30[v0];[1:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,zoompan=z='min(zoom+0.0015,1.1)':d=90:s=1080x1920:fps=30[v1];[2:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,zoompan=z='min(zoom+0.0015,1.1)':d=90:s=1080x1920:fps=30[v2];[v0][v1]xfade=transition=fade:duration=0.5:offset=2.5[x1];[x1][v2]xfade=transition=fade:duration=0.5:offset=5[x2]" -map "[x2]" -map 3:a -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 192k -shortest -pix_fmt yuv420p -movflags +faststart static/reels/{folder}.mp4'''
    
    # 8 In order to run this command .
    subprocess.run(command,shell=True,check=True)
    # Here ,shell=True (It ensures running shell command as a string)
        #  ,check=True (To ensure that it doesn't throw an non zero 0 error)


    



if __name__ == "__main__":
    while True:
        print("Processing queue .....")
        # 6.done.txt is used to tell the reel is created or not    
        with open("done.txt","r") as f:
            done_folders = f.readlines()
        
        # The error3 : the done_folders has extra \n E.g: 1f1-a70f-3814281c5033\n' 
        done_folders = [f.strip() for f in done_folders]
        folders = os.listdir("user_uploads")
        # print(folders,done_folders) #For testing purpose only 
        for folder in folders:
            if(folder not in done_folders): # this file recevies the folder name which is :text_to_audio
                text_to_audio(folder) # Generate the audio.mp3 from desc.txt
                create_reel(folder) # convert the images and audio.mp3 inside the folder to a reel 
                with open("done.txt","a") as f:
                    f.write(folder + "\n")
        time.sleep(4)



# Dry Run of 6. done.txt To get the audio and video 
# if __name__ == "__main__":

    # Read folders which are already processed
    #
    # done.txt:
    # 101
    # 102
    #
    # done_folders = ["101\n", "102\n"]

    # with open("done.txt","r") as f:
    #     done_folders = f.readlines()


    # Remove \n
    #
    # ["101\n", "102\n"]
    #       ↓
    # ["101", "102"]

    # done_folders = [f.strip() for f in done_folders]


    # Get all folders from user_uploads
    #
    # user_uploads:
    # 101
    # 102
    # 103
    #
    # folders = ["101", "102", "103"]

    # folders = os.listdir("user_uploads")


    # Check folders one by one

    # for folder in folders:

        # 101 → already processed → skip
        # 102 → already processed → skip
        # 103 → not processed → continue

        # if(folder not in done_folders):

            # Create audio from desc.txt
            # text_to_audio(folder)

            # Create reel from files inside the folder
            # create_reel(folder)

            # Save folder name in done.txt
            # so it will not be processed again

            # with open("done.txt","a") as f:
            #     f.write(folder + "\n")


# Dry run 


    # 8 ffmpeg : Using ffmpeg to generate videos.
    # FFmpeg is a powerful command-line tool for processing audio and video files.
    # Think of it as a toolbox for audio/video.
    # Main purposes of FFmpeg
    # 🎬 Convert video formats — MP4 → AVI, MOV → MP4, etc.
    # 🎵 Convert audio formats — WAV → MP3, etc.
    # ✂️ Cut/trim videos
    # 🔊 Extract audio from video
    # 🖼️ Combine images into a video
    # 🎙️ Combine audio + video
    # 📐 Resize videos
    # 📦 Compress audio/video
    # 🔄 Change codecs and resolutions

    # Steps to use ffmpeg 
    # Step 1 : Download ffmpeg
    # Step 2 : Copy all the files after extracting it than 
    # Step 3 : Click This PC -> Localdisk ->Programfiles than Create ffmpeg folder paste all the files .
    # Step 4 : Copy the path after clicking on bin folder which has ffmpeg.exe. (C:\Program Files\ffmpeg\bin)
    # Step 5 : After copy this ,search env -> Edit System Environment Variables ->path ->Edit 
    # ->Paste the copied path  ->ok ->ok (Done environment Variable is added).
    # Step 6 : To check it is install or not ,open terminal type ffmpeg -> run 
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

def text_to_audio(folder):
    # print("TTA",folder)
    # 7. Taking folders and text
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
        print(text,folder)
        #  text_to_speech_file(text,folder)
    pass


def create_reel(folder):
    # print("CR",folder)
    pass


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
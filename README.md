This is a project undertaken at Boston University in class EC601. 

The aim of this project is to create a python program which does the following:
1. Takes a twitter handle from the user
2. Downloads the images from that twitter handle
3. Compiles a video out of the images using FFMPEG
4. Uses the google cloud intelligence API to figure out a brief description about the stuff being tweeted about.

To realise this, I made separate modules to define their functionality. These files include:
1. Tweetscanner: This file is supposed to get the twitter feeds using the tweepy module of python and then extract the image URLs form it. It is then downloading the data from the internet as images which is to be analysed.
2. make_video: The images obtained in the tweetscanner function are stored locally and stiched into a video using the ffmpeg command on the command line.
3. analysis: The output video is then fed to the Google Cloud Intelligence API to provide with the various labels that can be identified and the same are displayed to the user.

The above functions are all combined by the help of the main_program.py python script. to run the program, follow the steps as mentioned below:-
1. Open terminal
2. Change into the directory with the program
3. In terminal, run the command python main_program.py
4. Follow the on-screen instructions to navigate thorugh the program, and Enjoy! 

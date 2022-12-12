# Smartsave
The program observe the download folder of a user and when a new file is created, it opens a UI platform to ask if the user want to change the location of the file, and if so it reccomend where to move the file to by looking at the file extension

!!!for the program to work you need to change the path in this line in the main file:observer.schedule(event_handler, 'C:\\Users\\zeldi\\Downloads', recursive=True) and put the path of your local downloads directory. Also make sure the folders Documents,Audio,videos,photos,Suspicious are in the same directory with all of the program files

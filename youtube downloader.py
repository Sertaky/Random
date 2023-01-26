# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=2T05-8GMAMk&ab_channel=AJ%2B%D9%83%D8%A8%D8%B1%D9%8A%D8%AA"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
#mp4files = yt.filter('mp4')

#to set the name of the file
#yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')


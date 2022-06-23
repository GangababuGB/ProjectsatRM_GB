from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
# yt.title = 'AWS-ML'
print("Length of video: ",yt.length/60)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()
#Starting download
#ys.download(input('enter location: '))
print("Downloading Initiated...")
ys.download('E:\YTD')
print("Downloading in Progress........")
print("Download completed!!")

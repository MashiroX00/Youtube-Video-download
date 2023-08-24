from pytube import YouTube

link = input("Enter your youtube link: ")

yt1 = YouTube(link)
print(yt1.title)
check = input("What do you want to download 1 for video 2 for audio.")

if check == "1":
    videos = yt1.streams.filter(progressive = True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    strm = int(input("please enter your index you want to download: "))
    videos[strm].download()
    print('Download Succacefully')



elif check == "2":
    yt2 = YouTube(link)
    audio = yt2.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in aud:
        print(i)
    strm2 = int(input("type index to download: "))
    audio[strm2].download()
    print('Download Succacefully')


##!/usr/bin/python3
#EmreYbs

from rich.console import Console
from rich import print
from rich.console import Console
from rich.markdown import Markdown
from termcolor import colored,cprint
from pytube import YouTube

#Creating video lists

MARKDOWN = """
# Welcome to Youtube Video Downloader 

*Notes*
1. This CLI app is a bit weird, I accept:). I wanted to try some libraries and mix them while learning about CLI tools. *For learning purposes:)*
2. However, the code is functional because you can download one video 
3. or download as many links by adding in **video_list** *variable* in the code. It is a list for a reason and there exists a loop for that necessity.
4. Don't forget to change the Youtube Video link everytime you want to download. Sometimes I download one video, sometimes more as in a list.
5. On a Mac and Linux, the code works well for me but with Windows 10,there are few issues because of the imported modules.
6. Please **do not** download copyrighted music videos, etc. I accept no responsibility:)
"""

console = Console()
welcome = Markdown(MARKDOWN)
console.print(welcome)

print("\n\n\t\t[u]Welcome to :heart: Youtube Video Downloader[/u], [bold cyan]EmreYbs[/bold cyan]:smiley:\n")
cprint("Download can be slow.Don't panic",'magenta','on_white')

# On Purpose, I assign a List to the variable here. So when you need more videos, add in the List below.
video_list = ['https://www.youtube.com/watch?v=ujId4ipkBio'] # Add more links if you need to download a couple of Youtube Videos



for i in video_list:
    try:
        yt = YouTube(i)
        cprint('URL to Download : ' + i,'blue','on_white')
        cprint('Downloading video: ' + yt.streams[0].title,'red','on_white')
    except:
        console.print("Connection Error",style='red')

  
stream = yt.streams.filter(res="720p").first()
stream.download("Downloads/")
print("Video was downloaded in [red]720p[/red] resolution, as long as it was available")
cprint("Remember: You can download one or more videos. Just edit the code as you wish",'magenta','on_white')
print("[bold green]Bye for now[/bold green] :smiley:")
print("\n:thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up:\n")




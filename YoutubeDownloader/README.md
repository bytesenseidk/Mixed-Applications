# YoutubeDownloader_CLI
Simple fast youtube downloader

![downloader](https://user-images.githubusercontent.com/50791042/126369283-916472a2-5333-44a2-bf3b-d51b30e5da33.PNG)

FFmpeg Install:
1. FFmpeg download link Windows 10: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z
2. Extract files to a folder named FFmpeg
- FFmpeg:
  - bin
  - doc
  - presets
    - LICENCE
    - README
3. Copy or clip folder to C-Drive or desired folder
4. Open PowerShell as admin
5. Type this command (Depends on your save path for the folder "FFmpeg"):
    - setx /m PATH "C:\FFmpeg\bin;%PATH%"
    - If done right, PowerShell will show this message:
        - SUCCESS: Specified value was saved.
6. Test version number:
    1. Restart PowerShell
    2. Type: 
        - ffmpeg -version

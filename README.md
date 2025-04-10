High-Quality YouTube Video Downloader (Ubuntu VPS Ready)

Download multiple YouTube videos in highest quality, auto-merge audio & video into MP4 format, with real-time progress tracking — all from a simple .txt file of links.
Perfect for VPS users, content creators, and automation fans.

Features:

Downloads best video + audio combo and merges into MP4

Supports batch downloads from a .txt file (1 link per line)

Progress bar using tqdm for clean terminal output

Retries & handles unstable connections

Saves output videos in ~/videos/ directory (auto-created)



---

Installation (Ubuntu 20.04+ VPS)

1. Clone the repo or download the script



git clone https://github.com/karthikraja1008/ytdl-txt.git
cd yt-high-quality-downloader

2. Install required packages



sudo apt update && sudo apt install python3-pip ffmpeg -y
pip3 install yt-dlp tqdm

3. Prepare your links



Create a text file (e.g., links.txt)

Add one YouTube link per line:


https://www.youtube.com/watch?v=abc123
https://www.youtube.com/watch?v=xyz456

4. Run the script



python3 fast_cr7_downloader.py links.txt


---

Output

All downloaded MP4 files will be saved in: ~/videos/

Files are named based on the video title



---

Example

python3 fast_cr7_downloader.py my_video_list.txt

> Output:



[12:01:22] [1/3] Starting: https://youtube.com/watch?v=abc123
Downloading: 89%
...
[12:03:11] [1/3] Finished

[12:03:12] [2/3] Starting: ...


---



---

License

MIT


---


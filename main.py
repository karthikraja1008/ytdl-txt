import yt_dlp
from tqdm import tqdm
import sys
import os
from datetime import datetime

SAVE_PATH = os.path.expanduser("~/videos")

def log(msg):
    now = datetime.now().strftime('%H:%M:%S')
    print(f"[{now}] {msg}", flush=True)

def ensure_folder():
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
        log(f"Created folder: {SAVE_PATH}")

def download_video(url):
    progress_bar = tqdm(total=100, desc="Downloading", unit="%")

    def hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0.0%').strip().replace('%', '')
            try:
                progress_bar.n = float(percent)
                progress_bar.refresh()
            except:
                pass
        elif d['status'] == 'finished':
            progress_bar.n = 100
            progress_bar.refresh()
            progress_bar.close()

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(SAVE_PATH, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': True,
        'progress_hooks': [hook],
        'retries': 5,
        'concurrent_fragment_downloads': 5,
        'fragment_retries': 5,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        log(f"Download failed: {e}")

def main(file_path):
    ensure_folder()

    if not os.path.exists(file_path):
        log("Input file not found.")
        return

    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for idx, url in enumerate(urls, 1):
        log(f"[{idx}/{len(urls)}] Starting: {url}")
        download_video(url)
        log(f"[{idx}/{len(urls)}] Finished\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py link.txt")
    else:
        main(sys.argv[1])

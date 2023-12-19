import os
import yt_dlp
import sys

def download_and_save_mp3(file_name, youtube_link):
    if not os.path.exists("tubtong_music/" + file_name + ".mp3"):
        options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'tubtong_music/{file_name}.%(ext)s',
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([youtube_link])
        print(f"[สำเร็จ] ดาวน์โหลด {file_name} สำเร็จ!")
    else:
        print(f"[ข้าม] {file_name} ดาวน์โหลดไปแล้ว")

def process_input(input_string):
    lines = input_string.strip().split('\n')
    for line in lines:
        parts = line.strip().split(' ')
        if len(parts) == 2:
            file_name, youtube_link = parts
            if youtube_link != '-':
                download_and_save_mp3(file_name, youtube_link)
            else:
                print(f"[เตือน] {file_name} ลิ้งค์ไม่สมบูรณ์")
        else:
            print(f"[ข้าม] {line}")

def process_file_input(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            input_string = file.read()
            process_input(input_string)
    else:
        print(f"หาไฟล์ {file_path} ไม่เจอ")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("วิธีใช้งาน: python downloadf.py music_lists.txt")
    else:
        input_file = sys.argv[1]
        process_file_input(input_file)

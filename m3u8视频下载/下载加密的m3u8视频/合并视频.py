# coding: utf-8
import glob

with open("movie.mp4", "wb") as fw:
    files = glob.glob("temp_videos/*.ts")
    for file in files:
        with open(file, "rb") as fr:
            fw.write(fr.read())
            print(f"\r{file}已经合并！总数：{len(files)}", end="    ")

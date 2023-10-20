'''
Задача 10

Оптимизируй код программы

Бо недавно стало интересно как работают загрузка видео 
в TikTok, он решил почитать об этом в интернете. Бо 
примерно понял как она работают поэтому он решил 
написать свою программу для этого, однако Бо заметил 
что его программа работает куда медленнее, помоги Бо оптимизировать его код.
'''

videos = "video_1.mp4 video_2.mp4 video_3.mp4 video_4.mp4 video_5.mp4"

video_1 = videos[0:11]
video_2 = videos[12:23]
video_3 = videos[24:35]
video_4 = videos[36:47]
video_5 = videos[48:59]

right_format = ".mp4"

video_1_right_format = video_1.endswith(right_format)
video_2_right_format = video_2.endswith(right_format)
video_3_right_format = video_3.endswith(right_format)
video_4_right_format = video_4.endswith(right_format)
video_5_right_format = video_5.endswith(right_format)


print("Можно ли загрузить первое видео:", video_1_right_format)
print("Можно ли загрузить второе видео:", video_2_right_format)
print("Можно ли загрузить третье видео:", video_3_right_format)
print("Можно ли загрузить четвёртое видео:", video_4_right_format)
print("Можно ли загрузить пятое видео:", video_5_right_format)

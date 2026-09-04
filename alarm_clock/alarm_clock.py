from datetime import datetime
import threading
import time
import pygame
import os

alarm = input("Set Alarm: ").split(":")

alarm_hour = int(alarm[0])
alarm_minute = int(alarm[1])

def alarm_clock(alarm_hour, alarm_minute):
    music = "my_music.mp3"
    is_running = True

    while is_running:
        os.system("cls")

        now = datetime.now()

        print(f"{now.hour}:{now.minute:02d}")

        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("⏰ Wake Up!")

            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

alarm_thread = threading.Thread(target=alarm_clock, args=(alarm_hour, alarm_minute))
alarm_thread.start()
for i in range(10):
    print(f"[Main] Program masih berjalan... {i}")
    time.sleep(1)
alarm_thread.join()
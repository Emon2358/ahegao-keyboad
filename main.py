import keyboard
import threading
import pygame
import random
import os

# pygameの初期化とミキサーのセットアップ
pygame.mixer.init()

# 音声ファイルのリスト
sound_files = [
    r,
    r,
    r,
    r,
    r,
    r
]

def play_random_sound():
    # ランダムに音声ファイルを選択し、再生
    sound_file = random.choice(sound_files)
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

def on_any_key(event):
    # 新しいスレッドで音声を再生
    threading.Thread(target=play_random_sound).start()

# すべてのキーが押されたときに `on_any_key` 関数を呼び出す
keyboard.hook(on_any_key)

# ESCキーで終了可能
keyboard.wait("esc")



import os

IMAGE_FILENAMES = ['thumbs_down.jpg', 'victory.jpg', 'thumbs_up.jpg', 'pointing_up.jpg']

for index, name in enumerate(IMAGE_FILENAMES):
  url = f'https://storage.googleapis.com/mediapipe-tasks/gesture_recognizer/{name}'
  os.system("curl " + url + f" > {name}")

import os
py = []
class Player:
    def __init__(self):
        self.name = "C:\\Users\\USER\\"
    
    def video(self):
     for root, dirs, files in os.walk(self.name):
       for file in files:
          if file.endswith(".mp4"):
             py.append(file)
             print(py)


    def audio(self):
     for root, dirs, files in os.walk(self.name):
       for file in files:
          if file.endswith(".mp3"):
             py.append(file)
             print(py)
    
    def css(self):
     for root, dirs, files in os.walk(self.name):
       for file in files:
          if file.endswith(".css"):
             py.append(file)
             print(py)

    def java(self):
     for root, dirs, files in os.walk(self.name):
       for file in files:
          if file.endswith(".js"):
             py.append(file)
             print(py)

    def html(self):
     for root, dirs, files in os.walk(self.name):
       for file in files:
          if file.endswith(".html"):
             py.append(file)
             print(py)

    def python(self):
     for root, dirs, files in os.walk(self.name):
       for file in files:
          if file.endswith(".py"):
             py.append(file)
             print(py)

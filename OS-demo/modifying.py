import os

os.getcwd()
os.chdir('/Users/christophekafrouni/Desktop/Images-Sample')
os.getcwd()

for i, img in enumerate(os.listdir()):
    os.rename(img, f'{i:02}.jpeg')

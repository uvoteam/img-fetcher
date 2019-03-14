import sys
import re
import os
import urllib.request
import shutil

allowedExt = ["png", "jpg", "jpeg", "svg"]

for data in sys.stdin:
    urls = re.findall(r'\"(https?://[^"]+)"', data)
    if not os.path.exists('./output'):
        os.mkdir('output')
    if len(urls):
        for url in urls:
            if len(url):
                try:
                    lastDot = url.rindex('.')
                    ext = url[lastDot+1:]
                    lastSlash = url.rindex('/')
                    imageName = url[lastSlash+1:]
                    endpoint = os.getcwd() + "/output/" + imageName
                    if not os.path.exists(endpoint) and ext in allowedExt:
                        filename, headers = urllib.request.urlretrieve(url)
                        shutil.move(filename, endpoint)
                        print(imageName)
                except ValueError:
                    print(url)
                    pass


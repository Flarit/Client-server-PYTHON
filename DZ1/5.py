import subprocess
import chardet

ya = ['ping', 'yandex.ru']
yandex = subprocess.Popen(ya, stdout=subprocess.PIPE)
for line in yandex.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

yo = ['ping', 'youtube.com']
youtube = subprocess.Popen(yo, stdout=subprocess.PIPE)
for line in youtube.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
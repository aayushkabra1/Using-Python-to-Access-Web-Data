import urllib.request, urllib.parse, urllib.error


file_reader = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in file_reader:
    print(line.decode().strip())
import urllib.request


response = urllib.request.urlopen("http://placekitten.com/5000/3000")
catImg = response.read()
with open("cat_5000_3000.jpg","wb") as f:
    f.write(catImg)

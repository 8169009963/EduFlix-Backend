import requests
def fetch_poster(url1):
    url1= url1.replace("https://www.youtube.com/watch?v=", "")
    url = "https://img.youtube.com/vi/{}/0.jpg".format(url1)
    # full_path = requests.get(url)
    print(url)
    return url
fetch_poster('https://www.youtube.com/watch?v=OnbcKzlWNeE')
from bs4 import BeautifulSoup
import requests

url = "https://unsplash.com/wallpapers/desktop/computer"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
#searches within website to find class mItv1
results = soup.find(class_="mItv1")
#searches within that class to find div with class YdIix
img_elements = results.find_all("div", class_="YdIix")
#for each div with that class, finds all image urls marked with class rEAWd to get each image URL
for img_element in img_elements:
    image_urls = img_element.find_all("a", class_="rEAWd")
    for image_url in image_urls:
        actual = image_url["href"]
        #prints full url
        print(f"unsplash.com{actual}\n")






import os
from django.db import models
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from video_creator.models import RedditPost
from video_creator.models import StockVideo


class RedditPostVideo(models.Model):
    title = models.CharField(max_length=150)
    post = models.ForeignKey(RedditPost, on_delete=models.CASCADE, related_name='videos')
    stock_video = models.ForeignKey(StockVideo, on_delete=models.CASCADE, related_name='videos')

    # def get_data(self):
    #     options = webdriver.FirefoxOptions()
    #     options.add_argument("--width=390")
    #     options.add_argument("--height=844")
    #     driver = webdriver.Firefox(service=FirefoxService(), options=options)
        
    #     driver.get(self.url)
    #     driver.add_cookie({"name": "eu_cookie", "value": '{"opted":true,"nonessential":false}'})

    #     element = driver.find_element(By.CLASS_NAME, "Post")
    #     self.text = element.find_element(By.TAG_NAME, "h1").text + "\n"
    #     body = element.find_elements(By.TAG_NAME, "p")
    #     self.text += "\n".join(map(lambda p: p.text, body))
    #     self.path = os.path.join(post_path, "header")
    #     x = int(element.location["x"])
    #     y = int(element.location["y"])
    #     w = x + int(element.size["width"])
    #     h = y + int(element.size["height"])

    #     sshot_bytes = driver.get_full_page_screenshot_as_png()
    #     page_sshot = Image.open(io.BytesIO(sshot_bytes)).crop((x, y, w, h))
    #     page_sshot.save(self.path + ".png")

    def __str__(self):
        return self.title

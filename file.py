from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--width=390")
options.add_argument("--height=844")
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver = webdriver.Chrome(options=options)

driver.get("https://www.reddit.com/r/AskReddit/comments/d0jjc2/the_2010s_decade_will_be_over_in_4_months_what_do/")

element = driver.find_element(By.CLASS_NAME, "Post")
text = element.find_element(By.TAG_NAME, "h1").text + "\n"
print(text)

body = element.find_elements(By.TAG_NAME, "p")
text += "\n".join(map(lambda p: p.text, body))
print(text)
# self.path = os.path.join(post_path, "header")

# x = int(element.location["x"])
# y = int(element.location["y"])
# w = x + int(element.size["width"])
# h = y + int(element.size["height"])

# sshot_bytes = driver.get_full_page_screenshot_as_png()
# page_sshot = Image.open(io.BytesIO(sshot_bytes)).crop((x, y, w, h))
# page_sshot.save(self.path + ".png")

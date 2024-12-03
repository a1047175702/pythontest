""" 
爬取myfreemp3.com中的音乐
by mohun


 """
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# 初始化 WebDriver（这里使用的是 Chrome 浏览器驱动）
options = webdriver.ChromeOptions()
# print(options)
# options.add_argument("--headless")  # 启动无头模式（不显示浏览器界面）
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(executable_path="chromedriver",options=options)

# 打开目标网页
# driver.get("https://tools.liumingye.cn/music#/")
driver.get("https://tools.liumingye.cn/music/#/artist/kyxK")


# 等待页面加载（这里简单等待3秒，你可以根据需要调整）
time.sleep(3)

# 获取页面源码
page_source = driver.page_source

# 使用 BeautifulSoup 解析 HTML 页面
soup = BeautifulSoup(page_source, "html.parser")

# 根据网页的结构找到所有歌曲的下载链接
# 假设歌曲下载链接包含在 <a> 标签中，可以通过分析网页找到正确的标签和属性
download_links = []

# 找到所有含有下载链接的 <a> 标签，具体属性需要根据页面结构进行调整
for a_tag in soup.find_all("button",class_=True):
    link = a_tag["class"]
   
    if "!text-inherit" in link:  # 假设下载链接中包含 'download' 字符串
        a_tag.click()
        time.sleep(1)
        download_links.append(link)

# 输出所有下载链接
for idx, link in enumerate(download_links, 1):
    print(f"歌曲 {idx} 下载链接: {link}")

# 关闭浏览器
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

# 初始化 WebDriver（这里使用的是 Chrome 浏览器驱动）
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 启动无头模式（不显示浏览器界面）
driver = webdriver.Chrome(options=options)

# 打开目标网页
driver.get("https://tools.liumingye.cn/music/#/artist/N86k")

""" # 等待页面完全加载，确保歌曲数据已加载
try:
    # 等待直到页面的某个元素加载完毕（例如歌曲列表加载完毕）
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".item relative rounded-md transition-colors"))  # 根据页面实际的 class 名称选择
    )
except Exception as e:
    print("页面加载失败:", e)
    driver.quit()
    exit() """

# 获取页面源码
page_source = driver.page_source

# 使用 BeautifulSoup 解析 HTML 页面
soup = BeautifulSoup(page_source, "html.parser")

# 找到所有歌曲的下载链接
download_links = []

# 假设下载链接在 <a> 标签中，并且是包含下载地址的链接
for a_tag in soup.find_all("button",class_=True):
    link = a_tag["class"]


    if "!text-inherit" in link:  # 下载链接的 URL 包含 'download'
        download_links.append(link)

# 输出找到的下载链接
if download_links:
    print(f"共找到 {len(download_links)} 个下载链接")
else:
    print("未找到下载链接")

# 模拟点击每一个下载链接
for download_element in driver.find_elements(By.XPATH, f"//button[@class='arco-btn arco-btn-text arco-btn-shape-circle arco-btn-size-medium arco-btn-status-normal text-btn !text-inherit']"):
    
    try:
        # 获取链接的元素
        # download_element = driver.find_element(By.CLASS_NAME,'arco-btn arco-btn-text arco-btn-shape-circle arco-btn-size-medium arco-btn-status-normal text-btn !text-inherit').click()
         # 获取链接的元素
        
        # 使用 ActionChains 模拟点击
        actions = ActionChains(driver)
        actions.click(download_element).perform()
        time.sleep(1)
        i = 0 
        for download_btn in driver.find_elements(By.XPATH, f"//div[@class='mx-context-menu-item-wrapper']"):
            i=i+1
            if i ==5:
                print(i , download_btn.get_property('innerHTML'))
                res = download_btn.click()
                time.sleep(1)
        # 等待页面跳转或下载（根据需要调整等待时间）
        time.sleep(1)

        # 这里你可以获取跳转后的 URL 或其他信息
        # current_url = driver.current_url
        # print(f"第 {idx} 个链接的跳转结果：{current_url}")
        
    except Exception as e:
        print(f"第 {idx} 个链接点击失败: {e}")

# 关闭浏览器
driver.quit()

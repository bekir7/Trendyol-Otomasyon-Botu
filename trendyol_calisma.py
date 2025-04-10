from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver başlat
service = Service("C:/Users/user/Desktop/chromedriver.exe")  
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)

driver.get("https://www.trendyol.com/")
driver.maximize_window()

# Çerezleri reddet
wait.until(EC.element_to_be_clickable((By.ID, "Combined-Shape"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

# Erkek kategorisine git
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='navigation-wrapper']/nav/ul/li[2]"))).click()

# Bir ürüne tıkla
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='browsing-gw-homepage']/div/div[1]/div[1]/div/article[3]/div/div/div[1]/div/div/a"))).click()

# Ürün adı al
urun = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='account-gw-just-for-you']/div/div/div[1]/div/div[2]/a/div[2]/div/div[1]")))
urun.click()

urun_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]"))).text
print(urun_text)

# Beden seç, sepete ekle
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/aside/div/div/div[2]/div/div[2]/div/div/button"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/div[1]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div/div[2]/div[2]/div/div[1]/div[5]/button"))).click()

# Sepete git
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='side-bar-basket-container']/div/a/div[1]"))).click()

# Sepetteki ürün adını kontrol et
sepet_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pb-container']/div/div[3]/div[3]/div/div[3]/a/p[1]"))).text
print(sepet_text)

if urun_text == sepet_text:
    print("isimler aynı")
else:
    print("isimler farklı")

time.sleep(2)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configura el controlador de Chrome
driver = webdriver.Chrome()

# Abre la página de YouTube
driver.get("https://www.youtube.com")

# Encuentra el campo de búsqueda
search_box = driver.find_element(By.NAME, "search_query")

# Ingresa el término de búsqueda y presiona Enter
search_box.send_keys("tutorial de Python")
search_box.send_keys(Keys.RETURN)

# Espera un momento para que se carguen los resultados (puedes ajustar esto según sea necesario)
time.sleep(5)

# Encuentra el primer resultado de la búsqueda y haz clic en él
first_result = driver.find_element(By.CSS_SELECTOR, "#contents a#video-title")
first_result.click()

# Espera un momento para que se cargue el video (puedes ajustar esto según sea necesario)
time.sleep(5)

# Cierra el navegador
driver.quit()

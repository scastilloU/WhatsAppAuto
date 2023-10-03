from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configura el controlador de Chrome
driver = webdriver.Chrome()

# Abre la página de Google
driver.get("https://www.google.com")

# Encuentra el campo de búsqueda y escribe "Selenium"
search_box = driver.find_element(By.NAME, "q")  # Usamos el atributo "name" para ubicar el campo de búsqueda
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)  # Simula presionar la tecla "Enter" para realizar la búsqueda

# Espera un momento (puedes ajustar esto según sea necesario)
driver.implicitly_wait(5)

# Cierra el navegador
driver.quit()

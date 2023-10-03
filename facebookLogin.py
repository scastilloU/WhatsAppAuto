from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configura el controlador de Chrome
driver = webdriver.Chrome()

# Abre la página de Facebook
driver.get("https://www.facebook.com")

# Encuentra el campo de entrada para correo electrónico y contraseña
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass") 

# Ingresa tu correo electrónico y contraseña aquí
email_field.send_keys("tu_correo_electronico")
password_field.send_keys("tu_contraseña")

# Envía el formulario de inicio de sesión
password_field.send_keys(Keys.RETURN)

# Espera un momento (puedes ajustar esto según sea necesario)
driver.implicitly_wait(5)

# Cierra el navegador
driver.quit()

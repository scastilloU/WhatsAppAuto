from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Import the 'By' module
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip

# Replace 'YOUR_CONTACT_NAME' with the name of the contact or group you want to message
contact_name = "MyNotes"

# Replace 'YOUR_MESSAGE' with the message you want to send



# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Open WhatsApp Web abrir chrome driver open chrome y busque esta pagina
driver.get('https://web.whatsapp.com/')

chatbot=input("Ponle nombre al chatbot:")
input("Presione enter luego de poner el codigo QR usando su telefono...")

with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

message = (
    "* Hola soy tu Chat bot: "+chatbot+"\n *"
    "Te Recomiendo las siguientes opciones:\n"
    "• *Opcion 1*: Deposito\n"
    "• *Opcion 2*: Debito\n"
    "• *Opcion 3*: Credito\n"
    "\n"
)
#time.sleep(20)

# Locate the search input and search for the contact or group
search_box = driver.find_element(By.XPATH, "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
active_element = driver.switch_to.active_element
search_box.send_keys(contact_name)
search_box.send_keys(Keys.ENTER)
active_element.send_keys(Keys.RETURN)
time.sleep(2)
print("Localizo el elemento que se busco en el search input")


# Locate the message input box and send the message  /html/body/div[1]/div/div/div[4]/div/div[2]/div/div/div/div[2]/div/div/div
#time.sleep(500)  

time.sleep(2)
contact_element = driver.find_element(By.XPATH, "//*[@id='pane-side']/div/div/div/div[1]")
actions = ActionChains(driver)
actions.move_to_element(contact_element).click().perform()
print('Contact element clicked')





contact_element = driver.find_element(By.XPATH, "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")

active_element = driver.switch_to.active_element
time.sleep(5)


active_element.send_keys(message)
active_element.send_keys(Keys.RETURN)


print("Contact element clicked")

time.sleep(15)
# Close the WebDriver   
driver.close()


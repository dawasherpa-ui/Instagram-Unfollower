from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace the placeholders with your Instagram username and password
username = "Username"#put your acc username
password = "hello12332"#put the acc password

# List of usernames to unfollow
users_to_unfollow =   [
  "taaraaa_g", "tamang.sayera", "tamang3059", "tamang_kamala", "tamangrebeca", "thakuri_goma", "thapa5486",
  "thapatrishti", "theeng_alisa", "thelifeofsumi_03", "theyadoregyans", "theycallmebaka__", "theycallmedipti",
  "theyluv_uh", "theyluvsneha_", "tmg.christina__", "toca_moonyoutuber", "tse_ring.you_den", "tsering190",
  "twinkle__bhatt", "twinklesahani1", "txstybrat_", "unforgettwble00___", "unikaagurunq", "unos_stha",
  "upadhyaya765", "upretideekxyaa", "urusha_bhandari", "usakiran_grg11", "usha.rana.magar", "ushakarki72",
  "ushakhatri_", "uswizzyy", "utsav_chyy", "va_gawoti_c_restha", "vaidya_sajina", "varshha_rai", "vawonarae222",
  "veedhyachhetri", "vib3swith_cherry77", "vidushi_ranaaa", "vini_.b._", "w_sd2019", "whateva094", "with_sangee",
  "wynnnyyyy", "x.kaberi", "xayamagar.xayamagar", "xmi_28", "xoxo_bivusha", "xtha_sushma", "yajeecrcim", "yanc_grg",
  "yangma_lama", "yangmucerpa", "yashaswirlrana", "yashika_0017_", "yasmin___raiii", "yayambu_yakha", "yikes_arp",
  "yo_jne", "yojeengurung", "your_mummy03", "yourfav._bedikabruhhh", "yuki_sherpa0", "yukiiiii_naaa",
  "yushikhakarki_", "yuxgsiubsm", "ywvmkz", "zinita20"
];


# Open Instagram login page
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the login page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

# Find the username input field and enter username
username_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username_input.send_keys(username)

# Find the password input field and enter password
password_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password_input.send_keys(password)

# Click on the login button
login_button = driver.find_element(By.XPATH, "//button[contains(.,'Log in')]")
login_button.click()

# Wait for the user's home page to load (indicating successful login)
try:
    time.sleep(25)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
except Exception as e:
    time.sleep(4)
    print(f"Login failed: {e}")

# Loop through the list of users to unfollow
for user in users_to_unfollow:
    # Search for the user's profile
    driver.get("https://www.instagram.com/" + user + "/")

    # Wait for the user's profile page to load
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.url_contains("/" + user + "/"))

    # Click on the unfollow button
    try:
        unfollow_button = driver.find_element(By.XPATH, '//button[contains(., "Following")]')
        unfollow_button.click()

        # Introduce a delay after clicking "Following" button
        time.sleep(2)

        confirm_unfollow_button = driver.find_element(By.XPATH, '//span[contains(., "Unfollow")]')
        confirm_unfollow_button.click()
        print(f"Successfully unfollowed @{user}.")
        time.sleep(3)
        # Introduce a delay after clicking "Unfollow" button

    except Exception as e:
        print(f"Already unfollowed @{user}")

# Close the browser
print("All Work Done")
driver.quit()

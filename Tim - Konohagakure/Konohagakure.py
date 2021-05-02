from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from faker import Faker

fake = Faker(["id_ID"])
base_url = "http://automationpractice.com/index.php"

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.action = ActionChains(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class A_LoginTest(BaseTest):
    def test_001_LoginSuccess(self):

    # Step 1 - CLick Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'))
        ).click()

    # Step 2 - Type Email
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        ).send_keys("narto@konoha.com")

    # Step 3 - Type Password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'passwd'))
        ).send_keys("123narto321")

    # Step 4 - Click Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitLogin'))
        ).click()

    # Step 5 - Verify Login Success
        userLoginSuccess = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').text
        self.assertEqual("Ahmad Narto", userLoginSuccess)

    # Step 6 - Click Sign Out
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'))
        ).click()

        time.sleep(5)

    def test_002_WrongEmail(self):

    # Step 1 - CLick Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'))
        ).click()

    # Step 2 - Type Email
        wrongEmail = fake.ascii_email()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        ).send_keys(wrongEmail)

    # Step 3 - Type Password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'passwd'))
        ).send_keys("123narto321")

    # Step 4 - Click Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitLogin'))
        ).click()

    # Step 5 - Verify Wrong Email
        actualResult = self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li').text
        self.assertEqual("Authentication failed.", actualResult)

        time.sleep(5)

    def test_003_WrongPassword(self):

        # Step 1 - CLick Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'))
        ).click()

        # Step 2 - Type Email
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        ).send_keys("narto@konoha.com")

        # Step 3 - Type Password
        wrongPassword = fake.password()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'passwd'))
        ).send_keys(wrongPassword)

        # Step 4 - Click Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitLogin'))
        ).click()

        # Step 5 - Verify Wrong Password
        actualResult = self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li').text
        self.assertEqual("Authentication failed.", actualResult)

        time.sleep(5)

class B_RegisterTest(BaseTest):

    def test_001_RegSuccess(self):

    # Step 1 - Click Sign In button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'login'))
        ).click()

    # Step 2 - Type Email
        user_email = fake.ascii_email()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email_create'))
        ).send_keys(user_email)

    # Step 3 - Click Create an account button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        ).click()

    # Step 4 - Click Gender button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="id_gender1"]'))
        ).click()

        time.sleep(1)

    # Step 5 - Type First Name
        fName = fake.first_name()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'customer_firstname'))
        ).send_keys(fName)

        time.sleep(1)

    # Step 6 - Type Last Name
        lName = fake.last_name()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'customer_lastname'))
        ).send_keys(lName)

        time.sleep(1)

    #  Step 7 - Type Password
        passwordGen = fake.password()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="passwd"]'))
        ).send_keys(passwordGen)

        time.sleep(1)

    # Step 8 - Input Date of Birth
        selectDays = Select(self.driver.find_element_by_id('days'))
        selectDays.select_by_value("20")

        selectMonths = Select(self.driver.find_element_by_id('months'))
        selectMonths.select_by_value("1")

        selectYears = Select(self.driver.find_element_by_id('years'))
        selectYears.select_by_value("2001")

        time.sleep(1)

    # Step 9 - Click Sign up newsletter
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="newsletter"]'))
    #     ).click()
    #
    # # Step 10 - Click receive special offers
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="optin"]'))
    #     ).click()

    # Step 11  - Type Company
        company = fake.company()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'company'))
        ).send_keys(company)

        time.sleep(1)

    # Step 12 - Type Address
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'address1'))
        ).send_keys("1587 Elizabeth Trail Apt. 821")

        time.sleep(1)

    # Step 13 - Type City
        city = fake.city()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'city'))
        ).send_keys(city)

        time.sleep(1)

    # Step 14 - Select State
        selectState = Select(self.driver.find_element_by_id('id_state'))
        selectState.select_by_visible_text("California")

        time.sleep(1)

    # Step 15 - Type Zip code
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'postcode'))
        ).send_keys("90001")

        time.sleep(1)

    # Step 16 - Select Country
        selectCountry = Select(self.driver.find_element_by_id('id_country'))
        selectCountry.select_by_visible_text("United States")

        time.sleep(1)

    # Step 17 - Type Additional info
        textGen = fake.text()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'other'))
        ).send_keys(textGen)

        time.sleep(1)

    # Step 18 - Type Mobile phone
        phone = fake.phone_number()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'phone_mobile'))
        ).send_keys(phone)

        time.sleep(1)

    # Step 19 - Type Reference
        reference = fake.name()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'alias'))
        ).clear()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'alias'))
        ).send_keys(reference)

    # Step 20 - Click Register button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submitAccount'))
        ).click()

        time.sleep(3)

    # Step 21 - Verify Register success
        info_account = self.driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        self.assertEqual("Welcome to your account. Here you can manage all of your personal information and orders.", info_account)

    # Step 22 - Click Log Out
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a'))
        ).click()

        time.sleep(3)

    def test_002_RegFailed(self):
        # Step 1 - Click Sign In button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'login'))
        ).click()

        # Step 2 - Type Email
        user_email = fake.ascii_email()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email_create'))
        ).send_keys(user_email)

        # Step 3 - Click Create an account button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        ).click()

        # Step 4 - Click Gender button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="id_gender1"]'))
        ).click()

        time.sleep(1)

        # Step 5 - Type First Name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'customer_firstname'))
        ).send_keys("@hm4d")

        time.sleep(1)

        # Step 6 - Type Last Name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'customer_lastname'))
        ).send_keys("N@rt0")

        time.sleep(1)

        #  Step 7 - Type Password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="passwd"]'))
        ).send_keys("p4$$")

        time.sleep(1)

        # Step 8 - Input Date of Birth
        selectDays = Select(self.driver.find_element_by_id('days'))
        selectDays.select_by_value("20")

        selectMonths = Select(self.driver.find_element_by_id('months'))
        selectMonths.select_by_value("1")

        selectYears = Select(self.driver.find_element_by_id('years'))
        selectYears.select_by_value("2001")

        time.sleep(1)

        # Step 9 - Click Sign up newsletter
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, '//*[@id="newsletter"]'))
        #     ).click()
        #
        # # Step 10 - Click receive special offers
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, '//*[@id="optin"]'))
        #     ).click()

        # Step 11  - Type Company
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'company'))
        ).send_keys("k0mp@ny!")

        time.sleep(1)

        # Step 12 - Type Address
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'address1'))
        ).send_keys("TPS Bojong Kenyot")

        time.sleep(1)

        # Step 13 - Type City
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'city'))
        ).send_keys("J3q@rd4h")

        time.sleep(1)

        # Step 14 - Select State
        selectState = Select(self.driver.find_element_by_id('id_state'))
        selectState.select_by_visible_text("California")

        time.sleep(1)

        # Step 15 - Type Zip code
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'postcode'))
        ).send_keys("kosong")

        time.sleep(1)

        # Step 16 - Select Country
        selectCountry = Select(self.driver.find_element_by_id('id_country'))
        selectCountry.select_by_visible_text("United States")

        time.sleep(1)

        # Step 17 - Type Additional info
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'other'))
        ).send_keys("1234 Lorem !!!")

        time.sleep(1)

        # Step 18 - Type Mobile phone
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'phone_mobile'))
        ).send_keys("o80gBg99!")

        time.sleep(1)

        # Step 19 - Type Reference
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'alias'))
        ).clear()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'alias'))
        ).send_keys("r3k0mend@5!")

        # Step 20 - Click Register button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'submitAccount'))
        ).click()

        time.sleep(1)

        # Step 21 - Verify Register failed
        actual_result = self.driver.find_element_by_xpath('//*[@id="center_column"]/div/p').text
        self.assertEqual("There are 6 errors", actual_result)

        time.sleep(3)

    def test_003_AlreadyRegistered(self):

    # Step 1 - Click Sign In button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'login'))
        ).click()

    # Step 2 - Type Email
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email_create'))
        ).send_keys("narto@konoha.com")

    # Step 3 - Click Create an account button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        ).click()

        time.sleep(3)

    # Step 4 - Verify Already Registered
        actualResult = self.driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li').text
        self.assertEqual("An account using this email address has already been registered. Please enter a valid password or request a new one.", actualResult)

        time.sleep(3)


class C_AddToCartTest(BaseTest):
    def test_001_fromHome(self):

        # Step 1 - Choose Item by Moving the pointer to the item
        ProductHover = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]')
        self.action.move_to_element(ProductHover).perform()

        # Step 2 - Click Add to Cart Button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]/span'))
        ).click()

        time.sleep(5)

        # Step 3 - Verify Result
        actual_result = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2').text
        self.assertEqual("Product successfully added to your shopping cart", actual_result)

        time.sleep(5)


    def test_002_fromCategory(self):

    # Step 1 - Click Category (T-SHIRT)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a'))
        ).click()

    # Step 2 - Move to element
        item = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li')
        self.action.move_to_element(item).perform()

    # Step 3 - Add to cart
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span'))
        ).click()

        time.sleep(5)

    # Step 4 - Verify Result
        actual_result = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2').text
        self.assertEqual("Product successfully added to your shopping cart", actual_result)

        time.sleep(5)

    def test_003_fromDetail(self):

        # Step 1 - Click Product
        item = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]')
        self.action.move_to_element(item).perform()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="homefeatured"]/li[2]'))
        ).click()

        # Step 2 - Click Add to Cart button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'Submit'))
        ).click()

        time.sleep(3)

        # Step 3 - Verify Result
        actual_result = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2').text
        self.assertEqual("Product successfully added to your shopping cart", actual_result)

    def test_004_fromSearch(self):

    # Step 1 - Search Item
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_query_top'))
        ).send_keys("blouse")

    # Step 2 - Submit Search
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'submit_search'))
        ).click()

    # Step 3 - Navigate to item
        item1 = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[1]/div')
        self.action.move_to_element(item1).perform()

    # Step 4 - Click Add to cart
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[1]/span'))
        ).click()

        time.sleep(2)

    # Step 5 - Verify Result
        actual_result = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2').text
        self.assertEqual("Product successfully added to your shopping cart", actual_result)

        time.sleep(3)



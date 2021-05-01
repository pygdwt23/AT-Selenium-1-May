from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from faker import Faker

fake = Faker()
base_url = "http://automationpractice.com/index.php"

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get(base_url)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

# class LoginTest(BaseTest):
#     # def test_001_LoginSuccess(self):
#     # def test_002_WrongEmail(self):
#     # def test_001_WrongPassword(self):

class RegisterTest(BaseTest):

    def test_001_RegSuccess(self):

    # Step 1 - Click Sign In button
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'login'))
        ).click()

    # Step 2 - Type Email
        user_email = fake.ascii_email()
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID, 'email_create'))
        ).send_keys(user_email)

    # Step 3 - Click Create an account button
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.ID, 'SubmitCreate'))
        ).click()

    # Step 4 - Click Gender button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="id_gender1"]'))
        ).click()

    # Step 5 - Type First Name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'customer_firstname'))
        ).send_keys("Ahmad")

    # Step 6 - Type Last Name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'customer_lastname'))
        ).send_keys("Narto")

    #  Step 7 - Type Password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="passwd"]'))
        ).send_keys("password123")

    # Step 8 - Input Date of Birth
        selectDays = Select(self.driver.find_element_by_id('days'))
        selectDays.select_by_value("20")

        selectMonths = Select(self.driver.find_element_by_id('months'))
        selectMonths.select_by_value("1")

        selectYears = Select(self.driver.find_element_by_id('years'))
        selectYears.select_by_value("2001")

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

    # Step 12 - Type Address
        address1 = fake.address()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'address1'))
        ).send_keys(address1)

    # Step 13 - Type City
        city = fake.city()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'city'))
        ).send_keys(city)

    # Step 14 - Select State
        selectState = Select(self.driver.find_element_by_id('id_state'))
        selectState.select_by_visible_text("California")

    # Step 15 - Type Zip code
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'postcode'))
        ).send_keys("90001")

    # Step 16 - Select Country
        selectCountry = Select(self.driver.find_element_by_id('id_country'))
        selectCountry.select_by_visible_text("United States")

    # Step 17 - Type Additional info
        textGen = fake.text()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'other'))
        ).send_keys(textGen)

    # Step 18 - Type Mobile phone
        phone = fake.phone_number()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'phone_mobile'))
        ).send_keys(phone)

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

        time.sleep(5)

    # Step 21 - Verify Register success
        registeredUser = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').text
        self.assertEqual("Ahmad Narto", registeredUser)

    # Step 22 - Click Log Out
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span'))
        ).click()

        time.sleep(5)

    # def test_002_RegFailed(self):
    # def test_003_AlreadyRegistered(self):

# Add To Cart Test
class AddToCartTest(BaseTest):
    # def test_001_fromHome(self):

        # # Step 1 - Choose Item by Moving the pointer
        # ProductHover = self.driver.find_element_by_xpath('//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[2]/span')
        # self.action.move_to_element(ProductHover).perform()
        #
        # # # Step 2 - Click Add to Cart Button
        # # WebDriverWait(self.driver, 10).until(
        # #     EC.element_to_be_clickable((By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]/span'))
        # # ).click()

    # def test_002_fromCategory(self):

    def test_003_fromDetail(self):

        # Step 1 - Click Product
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="homefeatured"]/li[2]'))
        ).click()

        # Step 2 - Click Add to Cart button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'Submit'))
        ).click()

        time.sleep(3)

        # Step 3 - Verify
        actual_result = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[1]/h2').text
        self.assertEqual("Product successfully added to your shopping cart", actual_result)

    # def test_004_fromSearch


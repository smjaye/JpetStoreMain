import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import jpetstore_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists
from selenium.webdriver import Keys


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'Launch {locators.app} App')
    print(f'__________________________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to Jpetstore App website
    driver.get(locators.jpet_store_url)

# check that Moodle URL and the home page title are as expected
    if driver.current_url == locators.jpet_store_url and driver.title == locators.jpet_store_homepage_title :
        print(f'Yey! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()



def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def register_new_user():
    if driver.current_url == locators.jpet_store_url:
        driver.find_element(By.LINK_TEXT, 'Sign In').click()
        sleep(0.5)
        assert driver.find_element(By.LINK_TEXT, 'Register Now!').is_displayed()
        driver.find_element(By.LINK_TEXT, 'Register Now!').click()
        sleep(0.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.userid)
        sleep(0.5)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.5)
        driver.find_element(By.NAME, 'repeatedPassword').send_keys(locators.password)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.firstName').send_keys(locators.first_name)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.lastName').send_keys(locators.last_name)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.email').send_keys(locators.email)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.phone').send_keys(locators.phone_number)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.address1').send_keys(locators.address1)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.address2').send_keys(locators.address2)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.city').send_keys(locators.city)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.state').send_keys(locators.state)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.zip').send_keys(locators.zip)
        sleep(0.5)
        driver.find_element(By.NAME, 'account.country').send_keys(locators.country)
        sleep(0.5)
        Select(driver.find_element(By.NAME, 'account.languagePreference')).select_by_visible_text('english')
        sleep(0.5)
        Select(driver.find_element(By.NAME, 'account.favouriteCategoryId')).select_by_visible_text('DOGS')
        sleep(0.5)
        driver.find_element(By.NAME, 'account.listOption').click()
        sleep(0.5)
        driver.find_element(By.NAME, 'account.bannerOption').click()
        sleep(0.5)
        ##########################################################################################
        # CLICK SAVE ACCOUNT INFORMATION TO COMPLETE REGISTRATION
        driver.find_element(By.NAME, 'newAccount').click()
        sleep(0.5)
        print(f'New user is registered!')
        print(f'userid is: {locators.userid}')
        print(f'username is : {locators.full_name}')


def my_cart():
    print(f'*********************************************************************************')
    driver.find_element(By.XPATH, '//img[@src="../images/dogs_icon.gif"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "K9-RT-01")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "Add to Cart")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[normalize-space()="Return to Main Menu"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//img[@src="../images/dogs_icon.gif"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "K9-RT-02")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "EST-22")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "Add to Cart")]').click()
    sleep(0.75)
    print(f'**********My Shopping cart is displayed***************')
    assert driver.find_element(By.XPATH, '//h2[contains(., "Shopping Cart")]').is_displayed()
    for i in range(len(locators.shopping_cart)):
        print(f'Item displayed:- {i} : {locators.shopping_cart[i]}')

    print(f'***********Adding more items to the cart******************** ')
    driver.find_element(By.XPATH, '//a[normalize-space()="Return to Main Menu"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//img[@src="../images/birds_icon.gif"]').click()
    sleep(0.75)
    driver.find_element(By.CSS_SELECTOR, 'a[href="/actions/Catalog.action?viewProduct=&productId=AV-CB-01"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[@class="Button"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[normalize-space()="Return to Main Menu"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//img[@src="../images/fish_icon.gif"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "FI-SW-01")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "Add to Cart")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//img[@src="../images/sm_fish.gif"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "FI-FW-02")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "EST-21")]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//a[contains(., "Add to Cart")]').click()
    sleep(0.75)


def update_cart():
    print(f'*************Updating the quantity in cart***********************')
    driver.find_element(By.NAME, 'EST-21').clear()
    sleep(0.5)
    driver.find_element(By.NAME, 'EST-21').send_keys('2')
    sleep(0.5)
    driver.find_element(By.NAME, 'updateCartQuantities').click()
    sleep(0.75)
    print(f'**************Validating that the cart is updated******************')
    assert driver.find_element(By.XPATH, '//td[normalize-space()="$10.58"]').is_displayed()
    sleep(0.5)
    print(f'The quantity of Adult female Goldfish is updated to 2 and total cost is also updated!')

    print(f'***********Removing an item from the cart***************************')
    driver.find_element(By.XPATH, '//tbody/tr[5]/td[8]/a[1]').click()
    sleep(0.75)
    print(f'*************Validating to check all items are displayed in Shopping cart****************************')
    for i in range(len(locators.itemid)):
        assert driver.find_element(By.XPATH, f'//a[contains(., "{locators.itemid[i]}")]').is_displayed()
        verifyshoppingcart = driver.find_element(By.XPATH, f'//a[contains(., "{locators.itemid[i]}")]').is_displayed()
        print(f'The item {locators.itemid[i]} is displayed: {verifyshoppingcart}')
        sleep(1)


def check_out():
        print(f'*********Proceeding to checkout*****************************************')
        driver.find_element(By.XPATH, '//a[contains(., "Proceed to Checkout")]').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '//a[contains(., "Confirm")]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//li[normalize-space()="Thank you, your order has been submitted."]').is_displayed()
        order_details = driver.find_element(By.XPATH, '//li[normalize-space()="Thank you, your order has been submitted."]').is_displayed()
        print(order_details)
        driver.find_element(By.XPATH, '//a[normalize-space()="Return to Main Menu"]').click()
        sleep(0.5)
        print(f'Hope you had a great time shopping with Jpetstore')


# setUp()
# register_new_user()
# my_cart()
# update_cart()
# check_out()
# tearDown()


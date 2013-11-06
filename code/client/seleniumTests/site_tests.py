from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from functools import wraps
from unittest_data_provider import data_provider
import random
import datetime

import unittest
import time
import sys
import os

site_url="https://qa.salsitasoft.com/projects/website/"
left_menu_id="nav-section"
top_menu_id="nav-main"
bottom_navigation="nav-subsection"
error_message="Please fill in the required fields."
report_path="code/client/seleniumTests/results/"

SCREENSHOT_FORMAT = 'code/client/seleniumTests/results/screenshots/%s_%s.png'

def screenshot_on_error(test): #this method makes screenshot on test fail
    @wraps(test)
    def inner(*args, **kwargs):
        try:
            test(*args, **kwargs)
        except:
            test_object = args[0] # self in the test
            dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
            filename = SCREENSHOT_FORMAT % (test_object.id(), dateTimeStamp)
 
            try:
                #test_object.selenium.capture_screenshot(filename)
                test_object.driver.save_screenshot(filename)
            except:
                pass
 
            raise
    return inner


class tests(unittest.TestCase):

    data = lambda: (
        ( "New Customer ", "", "Test Company " , True ),
        ( "New Customer ", "wrong_mail", "Test Company " , True ),
        ( "New Customer ", "test@test.com", "Test Company " , False),
        ( "", "test@test.com", "Test Company " , True ),
        ( "", "", "" , False ),
        ( "", "", "" , True ),
        ( "", "test@test.com", "Test Company " , True ),
        ( "", "", "Test Company " , True ),
        ( "", "", "Test Company " , False ),
        ( "New Customer ", "", "" , True ),
        ( "New Customer ", "", "" , False ),
        ( "New Customer ", "test@test.com", "" , True ),
        ( "", "", "Test Company " , True ),
        ( "", "", "Test Company " , False),
        ( "", "test@test.com", "" , True )
    )

    def setUp(self):
        """Setup new tests"""
        self.driver = webdriver.Remote(
            desired_capabilities={
                "browserName": os.environ['SEL_BROWSER'],
                "platform": os.environ['SEL_PLATFORM'] },
            command_executor=os.environ['SEL_HUB_URL'])
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_open_each_page(self):
        """Test check all menu elements are clickable and section name is equal to page title"""
        driver=self.driver
        driver.get(site_url+'solutions')
        cur_url=driver.current_url
        top_menu=driver.find_element_by_id(top_menu_id)
        top_menu_elements=top_menu.find_elements_by_class_name("ng-binding")
        for i in range(2,len(top_menu_elements)):
            top_menu_elements[i].click()
            print("page url ", driver.current_url)
            print("page title ", driver.title)
            print("section name", top_menu_elements[i].text)
            try:
                self.assertEqual(driver.title, top_menu_elements[i].text) # here will be compare text title and section name
                print("Title and section are eqaul")
            except AssertionError as e: self.verificationErrors.append(str(e)+ "\n Title and section are not equal")
            left_menu_elements=driver.find_element_by_id(left_menu_id).find_elements_by_class_name("ng-binding")
            if len(left_menu_elements)>0:
                for j in range(1,len(left_menu_elements)):
                    left_menu_elements[j].click()
                    print("page url ", driver.current_url)
                    print("page title ", driver.title)
                    print("section name", left_menu_elements[j].text)
                    try:
                        self.assertEqual(driver.title, left_menu_elements[j].text) # here will be compare text title and section name
                        print("Title and section are eqaul")
                    except AssertionError as e: self.verificationErrors.append(str(e)+ "\n Title and section are not equal")
                    bottom_menu_elements=driver.find_element_by_id(bottom_navigation).find_elements_by_class_name("ng-binding")
                    if len(bottom_menu_elements)>0:
                        for k in range(1,len(bottom_menu_elements)):
                            bottom_menu_elements[k].click()
                            print("page url ", driver.current_url)
                            print("page title ", driver.title)
                            print("section name", bottom_menu_elements[k].text)
                            try:
                                self.assertEqual(driver.title, bottom_menu_elements[k].text) # here will be compare text title and section name
                                print("Title and section are eqaul")
                            except AssertionError as e: self.verificationErrors.append(str(e)+ "\n Title and section are not equal")

    def test_arrow_right_click(self):
        """Test click on right arrow key"""
        driver=self.driver
        driver.get(site_url+'solutions')
        # get all top menu elements
        top_menu=driver.find_element_by_id(top_menu_id)
        top_menu_elements=top_menu.find_elements_by_class_name("ng-binding")
        print("Elements count", len(top_menu_elements))
        for i in range(1,len(top_menu_elements)-1):
            old_title=driver.title
            key_down = ActionChains(driver).send_keys(Keys.ARROW_RIGHT)
            key_down.perform()
            self.assertNotEqual(driver.title, old_title,  "Right arrow key click doesn't work")
            print("Page title is ", driver.title)
        old_title=driver.title
        key_down = ActionChains(driver).send_keys(Keys.ARROW_RIGHT)
        key_down.perform()
        self.assertEqual(driver.title, old_title, "Right arrow key click doesn't work")
    @screenshot_on_error
    def test_arrow_down_click(self):
        """Test click on down arrow key"""
        driver=self.driver
        driver.get(site_url+'solutions')
        time.sleep(2)
        # get all top menu elements
        left_menu_elements=driver.find_element_by_id(left_menu_id).find_elements_by_class_name("ng-binding")
        if len(left_menu_elements)>0:
            for i in range(len(left_menu_elements)-1,0, -1):
                old_title=driver.title
                key_down = ActionChains(driver).send_keys(Keys.ARROW_DOWN)
                key_down.perform()
                self.assertNotEqual(driver.title, old_title, "Down arrow key click doesn't work")
                print("Page title is ", driver.title)
            old_title=driver.title
            key_down = ActionChains(driver).send_keys(Keys.ARROW_DOWN)
            key_down.perform()
            self.assertEqual(driver.title, old_title, "Down arrow key click doesn't work")
    @screenshot_on_error
    def test_arrow_left_click(self):
        """Test click on left arrow key"""
        driver=self.driver
        driver.get(site_url+'contact-us')
        time.sleep(2)
        # get all top menu elements
        top_menu=driver.find_element_by_id(top_menu_id)
        top_menu_elements=top_menu.find_elements_by_class_name("ng-binding")
        for i in range(len(top_menu_elements)-1,0, -1):
            old_title=driver.title
            key_down = ActionChains(driver).send_keys(Keys.ARROW_LEFT)
            key_down.perform()
            self.assertNotEqual(driver.title, old_title, "Left arrow key click doesn't work")
            print("Page title is ", driver.title)
        old_title=driver.title
        key_down = ActionChains(driver).send_keys(Keys.ARROW_LEFT)
        key_down.perform()
        self.assertEqual(driver.title, old_title, "Left arrow key click doesn't work")
    @screenshot_on_error
    def test_vert_scroll_down_mouse(self):
        """Test vertical scroll using mouse wheel to the down"""
        driver=self.driver
        sites=[site_url+'solutions', site_url+'technologies',site_url+'projects']
        for item in sites:
            driver.get(item)
            left_menu_elements=driver.find_element_by_id(left_menu_id).find_elements_by_class_name("ng-binding")
            if len(left_menu_elements)>0:
                for i in range(len(left_menu_elements)-1,0, -1):
                    old_title=driver.title
                    driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaY=-120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
                    time.sleep(1)
                    self.assertNotEqual(driver.title, old_title,  "Scroll to the down using mouse doesn't work")
                    print("Page title is ", driver.title)
                old_title=driver.title
                driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaY=-120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
                self.assertEqual(driver.title, old_title, "Scroll to the down using mouse wheel doesn't work")

    @screenshot_on_error
    def test_vert_scroll_up_mouse(self):
        """Test vertical scroll using mouse wheel to the up"""
        driver=self.driver  
        driver.get(site_url+'solutions/mobile-apps')
        left_menu_elements=driver.find_element_by_id(left_menu_id).find_elements_by_class_name("ng-binding")
        if len(left_menu_elements)>0:
            for i in range(len(left_menu_elements)-1,0, -1):
                old_title=driver.title
                driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaY=120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
                time.sleep(1)
                self.assertNotEqual(driver.title, old_title,  "Scroll to the up using mouse doesn't work")
                print("Page title is ", driver.title)
            old_title=driver.title
            driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaY=120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
            self.assertEqual(driver.title, old_title, "Scroll to the up using mouse wheel doesn't work")

    @screenshot_on_error
    def test_hor_scroll_left_mouse(self):
        """Test horisontal scroll using mouse wheel to the left"""
        driver=self.driver  
        driver.get(site_url+'contact-us')
        time.sleep(1)
        # get all top menu elements
        top_menu=driver.find_element_by_id(top_menu_id)
        top_menu_elements=top_menu.find_elements_by_class_name("ng-binding")
        for i in range(len(top_menu_elements)-1,0, -1):
            old_title=driver.title
            driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaX=120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
            time.sleep(1)
            self.assertNotEqual(driver.title, old_title, "Scroll to the left using mouse doesn't work")
            #print("Page title is ", driver.title)
        old_title=driver.title
        driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaX=120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
        self.assertEqual(driver.title, old_title, "Scroll to the left using mouse wheel doesn't work")
        
    @screenshot_on_error    
    def test_hor_scroll_right_mouse(self):
        """Test horisontal scroll using mouse wheel to the right"""
        driver=self.driver  
        driver.get(site_url)
        old_title=driver.title
        driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaX=-120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
        time.sleep(1)
        self.assertNotEqual(driver.title, old_title) 
        top_menu=driver.find_element_by_id(top_menu_id)
        top_menu_elements=top_menu.find_elements_by_class_name("ng-binding")
        print("Elements count", len(top_menu_elements))
        for i in range(1,len(top_menu_elements)-1):
            old_title=driver.title
            driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaX=-120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
            time.sleep(1)
            self.assertNotEqual(driver.title, old_title, "Scroll to the right using mouse wheel doesn't work")
            print("Page title is ", driver.title)
        old_title=driver.title
        driver.execute_script("var elm = document.getElementsByTagName('body')[0]; var e=document.createEvent('MouseEvents');e.wheelDeltaX=-120;e.initMouseEvent('DOMMouseScroll' ,true,true, window,120,0,0,0,0,0,0,0,0,0,null);elm.dispatchEvent(e);")
        self.assertEqual(driver.title, old_title, "Scroll to the right using mouse doesn't work")
        
    @screenshot_on_error
    @data_provider(data)
    def test_validation_form(self, name, mail, company, sum):
        """Test validation on contact form"""
        driver=self.driver
        driver.get(site_url+'contact-us')
        self.contact_insert(name, mail, company ,sum)
        contact_form=driver.find_element_by_id("contact-us-form")
        self.assertEqual(contact_form.find_element_by_xpath("//p[@ng-if='error']").text,  error_message) # Check if user get error message after provide information in not all required field

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def hover(self, element):
        mouse_over = ActionChains(self.driver).move_to_element(element)
        mouse_over.perform()

    def contact_insert(self, name, mail, company, sum ):
        driver=self.driver
        contact_form=driver.find_element_by_id("contact-us-form")
        #fill in Name text area
        contact_form.find_element_by_xpath("//input[@type='text']").send_keys(name)
        #fill in mail area
        contact_form.find_element_by_xpath("//input[@type='email']").send_keys(mail)
        #fill in Company area
        contact_form.find_element_by_name("company").send_keys(company)
        #Choose budget
        if sum==True:
            contact_form.find_element_by_xpath("//a[@class='chosen-single chosen-default']").click()
            result=contact_form.find_element_by_xpath("//ul[@class='chosen-results']")
            results=result.find_elements_by_tag_name("li")
            #rand=random.randint(0, len(results))
            results[0].click()
            #results[rand].click()
        time.sleep(1)
        #Click on send
        contact_form.find_element_by_xpath("//button").click()
        time.sleep(1)

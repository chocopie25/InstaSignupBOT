from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



def SignInstaBOT(mail,name,uname,passw):

    br = webdriver.Chrome()
    #br.maximize_window()
    br.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
    time.sleep(2)

    user = br.find_element_by_name("emailOrPhone")
    user.clear()
    user.send_keys(mail) 
    time.sleep(2)
    
    
    user = br.find_element_by_name("fullName")
    user.clear()
    user.send_keys(name) 
    time.sleep(2)
    
    user = br.find_element_by_name("username")
    user.clear()
    user.send_keys(uname) 
    time.sleep(2)
    
    user = br.find_element_by_name("password")
    user.clear()
    user.send_keys(passw) 
    user.send_keys(Keys.ENTER)
    time.sleep(2)
    user.send_keys(Keys.ENTER)
    
    '''btn1 = br.find_element_by_partial_link_text("Sign")
    btn1.click()
    time.sleep(2)
    
        
    
    btn1 = br.find_element_by_css_selector(" .aic .z0 div")
    btn1.click()
    time.sleep(2)
    
    
    user = br.find_element_by_css_selector(".oj div textarea  ")
    user.clear()
    user.send_keys(name1) 
    
    user = br.find_element_by_css_selector(".aoD.az6  input ")
    user.clear()
    user.send_keys("BOT Mail")    
    
    user = br.find_element_by_css_selector(".Ar.Au div ")
    user.clear()
    user.send_keys("Hello, its my first BOT!!!")  
    
    btn1 = br.find_element_by_css_selector("tr.btC td:nth-of-type(1) div div:nth-of-type(2) ")
    btn1.click()
    time.sleep(2)'''


import string
from random import *
A=[]
for m in range(0,100):
 characters = string.ascii_letters + string.punctuation  + string.digits
 password1 =  "".join(choice(characters) for x in range(randint(8, 16)))
 A.append(password1)


B=[]
for m in range(0,100):
 randomInt =randint(000,1000)
 randomInt=str(randomInt)
 email= "inbewacs"+ randomInt +"@gmail.com" 
 B.append(email)
#for m in range(0,100):
print(B[1])
print("inbewacs"+ randomInt)
print(A[1])

if __name__ == "__main__":
	SignInstaBOT(B[1], 'RAM',"inbewacs"+ randomInt,A[1])
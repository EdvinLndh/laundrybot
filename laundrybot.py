from selenium import webdriver
from selenium.webdriver.common.by import By


username=<username>
password=<password>
day = None

browser_open = False

def choose_day() -> int: 
  
    while True: 
        try: 
            day = input("""Please choose a day to book laundry:
    ==== 1: Monday      ==== 
    ==== 2: Tuesday     ====
    ==== 3: Wednesday   ====
    ==== 4: Thursday    ====
    ==== 5: Friday      ====
    ==== 6: Saturday    ====
    ==== 7: Sunday      ====
    ==== 0: Exit        ====
    """)
            day = int(day)
            if day < 0 or day > 7:
                print("Please enter a number between 0-7.")
            elif day == 0:
                if browser_open: 
                    browser.quit()
                quit(0)
            else: 
                break
                
        except Exception as e: 
            print("Please enter a valid number. " + str(e))


day = choose_day()
try: 
    browser = webdriver.Firefox()
except Exception as e:
    print("You might not have firefox installed. " + str(e)) 

browser.get(<booking_url>)
browser_open = True


def login(): 

    try: 
        loginButton = browser.find_element(by=By.CSS_SELECTOR, value='td[onclick="ShowPopupMenuL();"]')
        loginButton.click()
    except: 
        print("Didn't find login button")
    try: 
        userInput = browser.find_element(by=By.CSS_SELECTOR, value='input[name="User"]')
    except: 
        print("Didn't find login input")
    try: 
        passInput = browser.find_element(by=By.CSS_SELECTOR, value='input[name="pw"]')
    except: 
        print("Didn't find password input")

    userInput.send_keys(username)
    passInput.send_keys(password)

    try: 
        submitButton = browser.find_element(by=By.CSS_SELECTOR, value='button[style="width: 200 px"]')
        submitButton.click()
    except: 
        print("Didnt find submit button")


def pickLaundryPlace():
    try:
        browser.find_element(by=By.CSS_SELECTOR, value='td[onmouseup="ShowPopupMenu5();"]').click()
        chooseStoraNydala12 = browser.find_element(by=By.CSS_SELECTOR, value='td[onclick="MenuHit5(this.innerHTML,2);"]')
        chooseStoraNydala12.click()
    except: 
        print("Didnt find laundry choosing button")

def pickTimeAndDays(time, day):
    try: 
        table = browser.find_element(by=By.CSS_SELECTOR, value='table[width="730"]')
    except: 
        print("Didnt find table")

    # 7 & 8 are 17-19 and 19-07 respectively
    try:
        table_rows = table.find_elements(by=By.TAG_NAME, value='tr')
        timeRow = table_rows[time]

        days = timeRow.find_elements(by=By.TAG_NAME, value='td')
        days[day].click()
        bookButton = browser.find_element(by=By.ID, value="Btn2")
        if bookButton.get_attribute("onmouseup") == "": 
            print(bookButton.get_attribute("onmouseup"))
            print("Time is already booked!")
            raise Exception
        else: 
            bookButton.click()
                    
    except Exception as e: 
            print("Didnt find rows" + str(e))



login()
pickLaundryPlace()

print("Everything successful so far. Keep in mind that the booking will be from 17 to 07.")
while(True):
    if day != None:            
        try: 
            pickTimeAndDays(7, day)
            pickTimeAndDays(8, day)    
            break
        except Exception as e: 
            print("This time seems to be booked, error: " + str(e))
            day = choose_day()
            continue

print("Booking sucessful!")
browser.quit()
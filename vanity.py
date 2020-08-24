from selenium import webdriver
import getpass


def wait(time=5):  # Wait function to allow for load times
    return driver.implicitly_wait(time)


def username():  # Enter a username into the terminal
    name = input(str("What is the username?   "))
    return name


def password():  # Enter password into terminal without showing the input
    word = getpass.getpass("Enter your password: ")
    return word


def tag():  # Enter the hash tag that the script will search for
    tag1 = input(str("What is the hashtag you would like to use?  #"))
    tag1 = "#" + tag1
    return tag1


def likes():  # How long the script should run for
    number = input("How many images do you want to like?   ")
    return number


user = username()
pass_w = password()
h_tag = tag()
number_of_likes = int(likes())

# Open instagram
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
wait(10)

# Login to your instagram account
driver.find_element_by_name("username").send_keys(user)  # Username
driver.find_element_by_name("password").send_keys(pass_w)  # Password
wait()
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()  # Click login
wait()

# Search for the specific tag
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
wait()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(h_tag)
wait()

# Pick first tag in the dropdown list from instagram
search = driver.find_element_by_xpath\
    ('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div').click()

# search for images most recently uploaded
most_recent = driver.find_element_by_xpath\
    ('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div').click()

# Loop which likes an image and scrolls to the next
for i in range(number_of_likes):
    like = driver.find_element_by_xpath\
        ('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
    wait(10)
    next1 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()

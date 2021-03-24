#For practice use only
#ATS covid questionnaire should be completed based on how you feel everyday

from selenium import webdriver
from selenium.webdriver.support.select import Select


athleteID = "Enter User"
password = "Enter Pass"
database = "atsstevens"

driver = webdriver.Chrome(executable_path= r"Your_Executable_path")
driver.get("https://www.atsusers.com/ATSWeb/Default.aspx")
text_area = driver.find_element_by_xpath('//*[@id="MainContent_txtUserName"]')
text_area.send_keys(athleteID)
text_area = driver.find_element_by_xpath('//*[@id="MainContent_txtPassword"]')
text_area.send_keys(password)
text_area = driver.find_element_by_xpath('//*[@id="MainContent_txtDatabaseName"]')
text_area.send_keys(database)

login = driver.find_element_by_xpath('//*[@id="MainContent_cmdLogin"]')
login.click()

athleteInfo = driver.find_element_by_xpath('//*[@id="MainContent_cmdAthlete"]/img')
athleteInfo.click()

forms = driver.find_element_by_xpath('//*[@id="MainContent_liForms"]/a')
forms.click()

dropdown = Select(driver.find_element_by_xpath('//*[@id="MainContent_ddFormName"]'))
dropdown.select_by_visible_text("Daily Covid-19 Screening")

new = driver.find_element_by_xpath('//*[@id="MainContent_cmdNewForm"]')
new.click()

for i in range(11):
    question_string = "MainContent_RptrAthleteForms_rblYesCHecked_{}_1_{}".format(i,i)
    question = driver.find_element_by_id(question_string)
    question.click()

save = driver.find_element_by_xpath('//*[@id="MainContent_cmdSaveForms2"]')
save.click()


driver.close()

print("Done")

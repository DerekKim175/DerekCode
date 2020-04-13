import pymysql
import requests
import bs4
import schedule
import time
import telegram

telegram_token = '1136527964:AAHM6ERIl1hetRflIB1KrQuQC4pwIPUyYkw'
telegram_id = '1220354777'

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd = 'Chiggawithagun1.', db='weather', charset='utf8')

cursor = db.cursor()

def corona():
	s = ''
	corona_url = "https://www.worldometers.info/coronavirus/#countries"
	corona_requests = requests.get(corona_url)
	corona_html = corona_requests.text
	bs4_corona = bs4.BeautifulSoup(corona_html, 'html.parser')
	country = bs4_corona.find_all('a',attrs={'class','mt_a'})

	for i in range(0,50):

		nation = (country[i].text.strip())

		total = country[i].findNext().text

		total_cases = country[i].findNext()
		new = total_cases.findNext().text

		if new == "":
		    new = "0"

		new_cases  = country[i].findNext('td').findNext('td')
		death = new_cases.findNext().text

		total_death = country[i].findNext('td').findNext('td').findNext('td')
		new_death = total_death.findNext().text

		if new_death == "":
		    new_death = "0"


		y = 'INSERT INTO `weather`.`CoronaVirus_Data` (`country`,`total_cases`,`new_cases`,`total_deaths`,`new_deaths`) VALUES ("'+nation+'","'+total+'","'+new+'","'+death+'","'+new_death+'");'
		cursor.execute(y)
		db.commit()

		s += str(i+1)+" Country: "+nation+"\n Total Cases: "+total+ "\n New Cases: "+new+"\n Total Death: "+death+"\n New Death: "+new_death+"\n"
		return s

	bot = telegram.Bot(token = telegram_token)
	bot.sendMessage(telegram_id, s)

schedule.every().day.at("22:15").do(corona)


while True:
	schedule.run_pending()
	time.sleep(1)
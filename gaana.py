import requests,webbrowser
from pprint import pprint
from bs4 import BeautifulSoup

r=requests.get('https://gaana.com/topcharts').text
soup=BeautifulSoup(r,'html.parser')

data=soup.find_all('div',class_='arwtork_label')
u=[]
c=1
for i in data:
	print(c,i.a.text)
	c+=1
	u.append(i.a['href'])

choice=int(input('Enter the number of category which u want to listen\n'))
url='https://gaana.com'+u[choice-1]	

re=requests.get(url).text
soup2=BeautifulSoup(re,'html.parser')
top_charts=soup2.find_all('div',class_='playlist_thumb_det')
count=0
songs_url=[]
for value in top_charts:
	count+=1
	print(count,value.a.text)
	songs_url.append(value.a['href'])	
webbrowser.open(songs_url[int(input('enter the no of song which u want to play\n'))-1])
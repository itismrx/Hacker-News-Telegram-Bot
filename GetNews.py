import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
def sorted_votes(news):
  return sorted(news,key=lambda k:k['votes'],reverse=True)
def HackerNews(links,subtext):
    news = []
    messege = ''
    counter = 0
    for index,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 100 and counter < 5:
                line = '----------------------------------------------------'
                towrite = "\n🗞 " + title + "\n\n 🔗 " + href + "\n\n      🖤Vote : " + str(points) + "\n"+line
                #print(towrite)
                messege += towrite
                news.append({'title':title,'link':href , 'votes':points})
                counter += 1
  
    return messege
def getNews():
    return HackerNews(links,subtext)

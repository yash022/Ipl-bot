import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup


def teams_data():
    url='https://www.iplt20.com/'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
    request=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(request.text,"html.parser")

    teams=[]
    points=[]

    teams_data=[]

    for  i in range(len(soup.findAll("span",attrs={'class':'standings-table__team-name standings-table__team-name--short js-team'}))):
        teams.append((soup.findAll("span",attrs={'class':'standings-table__team-name standings-table__team-name--short js-team'})[i].text))

    for  i in range(len(soup.findAll("td",attrs={'class':'standings-table__highlight js-points'}))):
        points.append((soup.findAll("td",attrs={'class':'standings-table__highlight js-points'})[i].text))

    for row in zip(teams,points):
        teams_data.append('-'.join(row))

    Final_teams_data = str(teams_data).replace("["," ").replace("["," ").replace("'"," ").replace("]"," ").replace(",","\n")
    return Final_teams_data


def open_IPL_website():
    import webbrowser
    webbrowser.open("https://www.iplt20.com/")


def latest_match_score():
    url ='https://www.cricbuzz.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')

    match_score=("The last match was between"+" "+soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[0].get_text()+" "+"and"+" "+soup.find_all(class_='cb-ovr-flo cb-hmscg-tm-nm')[1].get_text()+" "+"and the score was"+" "+
    soup.find_all(class_='cb-ovr-flo')[8].get_text()+soup.find_all(class_='cb-ovr-flo')[10].get_text()+","+soup.find_all(class_='cb-ovr-flo cb-text-complete')[0].get_text())

    return match_score

def play_ipl_msd_song():
    url='https://pywhatkit.herokuapp.com/playonyt?topic=helicopter+7'
    request=requests.get(url)
    webbrowser.open(request.text)

def match_schedule():
    webbrowser.open("https://resources.platform.iplt20.com/IPL/document/2021/09/28/fa3228b5-f4d6-484d-b31e-fcd91d551e44/VIVO-IPL-2021-Match-Schedule-UAE_010101.pdf")

def next_match():
    url='https://www.iplt20.com/matches/schedule/men'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
    request=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(request.text,"html.parser")

    date=(soup.find_all("h3",attrs={'class':'match-list__date js-date'})[0].text)
    team_1=soup.find_all("p",attrs={'class':'fixture__team-name'})[0].text
    team_2=soup.find_all("p",attrs={'class':'fixture__team-name'})[1].text
    time=soup.find_all("strong",attrs={'class':'fixture__time'})[0].text

    return("Next match is scheduled on"+" "+date+" "+"between"+" "+team_1+" and"+" "+team_2+" at"+" "+time)
    
def ipl_news():
    url='https://www.google.com/search?q=ipl+&biw=1600&bih=722&sxsrf=AOaemvItLw2SlmB9jX9LHK3eqX6V-hd9kw%3A1633950322246&ei=chpkYbKjDsPcz7sPlIKYqAk&ved=0ahUKEwiypKakm8LzAhVD7nMBHRQBBpUQ4dUDCA4&uact=5&oq=ipl+&gs_lcp=Cgdnd3Mtd2l6EANKBAhBGABQAFgAYI4CaABwAngAgAEAiAEAkgEAmAEA&sclient=gws-wiz#sie=lg;/g/11fqtnjjg0;5;/m/03b_lm1;nw;fp;1;;'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
    request=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(request.text,"html.parser")

    unfiltered_list=[]
    index=[]

    for i in range(len(soup.find_all("div",attrs={'class':'nDgy9d'}))):
        index.append(str(i))

    for i in range(len(soup.find_all("div",attrs={'class':'nDgy9d'}))):
        unfiltered_list.append(soup.find_all("div",attrs={'class':'nDgy9d'})[i].text.replace(","," ").replace("\n"," " ))


    Final=[]

    for i in zip(index,unfiltered_list):
        Final.append('. '.join(i))

    return(str(Final).replace("'"," ").replace("["," ").replace("]"," ").replace(",","\n\n"))

def team_members(team):
    url="https://www.google.com/search?q="+team+"+members+2021+ipl"
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}
    request=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(request.text,"html.parser")

    team_members=[]

    for i in range(len(soup.find_all("div",attrs={'class':'dAassd'}))):
        team_members.append(soup.find_all("div",attrs={'class':'dAassd'})[i].text)

    return(str(team_members).replace("'"," ").replace("["," ").replace("]"," "))


def help():
    return("!scoreboard - use this command to get the points and the ranking of all the teams in IPL \n  !open IPL website - use this to open the official website of IPL \n !latest score - use this to get the score of the lastest match \n !msd - use this to play msd song \n !match schedule - use this to see the match schedule \n !next match - use this to get the details of the next match \n !ipl news - use this to get the latest news related to IPL \n type team members of + team name to find team members of a particular team" 
)


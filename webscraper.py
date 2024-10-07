from bs4 import BeautifulSoup
import csv
import os
import requests

def RansomHub():

    with open('RansomHub.html', 'r') as f:
        contents = f.read()

        soup = BeautifulSoup(contents, "html.parser")


        boxes = soup.find_all('div', class_='col-12 col-md-6 col-lg-4')
        info = []
        for box in boxes:
            victim = box.find('div', class_='card-title text-center').text
            date = box.find('div', class_='card-footer').text
            date = date.replace(" ", "")
            date = date.strip()
            date = date[:10]
            group = 'RansomHub'

            cell = [date, victim, group]

            info.append(cell)

    print(info)

    with open("RansomHub.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(info)


    
def Play():

    directory = 'Play_HTML'
    data = []
    for filename in os.listdir(directory):
        print(filename)
        with open(f'{directory}/{filename}', 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, "html.parser")
            boxes = soup.find_all('th', class_='News')

            for box in boxes:
                info = box.find('div').text
                info = info.split()

                if(info[0] == 'United' and info[1] == 'States'):
                    country = 'United States'
                    info.pop(0)
                    info.pop(0)        
                elif(info[0] == 'United' and info[1] == 'Kingdom'):
                    country = 'United Kingdom'
                    info.pop(0)
                    info.pop(0)
                else:
                    country = info[0]
                    info.pop(0)

                victim =  ''.join(filter(str.isalnum, info[0]))

                info.pop(0)
                date = ""
                group = 'PLAY'
                for char in info[2]:
                    if(char.isalpha()):
                        continue
                    date += char
                cell = [date, victim, country, group]
                data.append(cell)

    with open("PLAY.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)


def LockBit3():

    # defining the html contents of a URL.
    url = 'https://www.ransomlook.io/group/lockbit3'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find_all('table')

    posts = table[2]
    content = posts.find_all('td')
    dateidx = 0
    victimidx = 1
    data = []

    while(dateidx<len(content)):
        date = content[dateidx].text.strip()
        victim = content[victimidx].text.strip()
        group = 'Lockbit3' 
        dateidx +=4
        victimidx +=4
        cell = [date, victim, group]
        data.append(cell)

        print(cell)   

    with open("Lockbit3.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)

def Lock():
    data = []
    with open('LockBit3.0.html', 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        boxes = soup.find_all('a', class_='post-block')
        
        for box in boxes:
            victim_site = box.find('div', class_='post-title').text.strip()
            published_date = box.find('div', class_='updated-post-date').text.strip()
            published_date = published_date.replace('Updated:', '').replace(',','').strip()[:11]
            group = 'LockBit3.0'
            cell = [published_date, victim_site, group]
            data.append(cell)


    with open("LockBit3.0_new.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)


Lock()

#RansomHub()
#Play()
#LockBit3()
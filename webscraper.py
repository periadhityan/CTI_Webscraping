from bs4 import BeautifulSoup
import csv
import os

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

Play()
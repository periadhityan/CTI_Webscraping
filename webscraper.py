from bs4 import BeautifulSoup
import csv

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

    


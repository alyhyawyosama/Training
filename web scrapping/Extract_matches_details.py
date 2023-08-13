# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:54:37 2023

@author: Asama
"""

import requests
from bs4 import BeautifulSoup #convert to parser 
import csv

def main(page):
    src = page.content #return page content in undity form
    #make the page content in parse to deal with it as objects
    soup = BeautifulSoup(src,"lxml") #to make the page content in readable contents
    championShips = soup.find_all("div",{"class":"matchCard"})
    matches_details= []
    def get_match_info(championShip):
        champiion_title = championShip.contents[1].find("h2").text.strip()
        #Or we can use this
        #champiion_title = championShip.contents[1].contents[1].contents[3].text.strip()
        all_matches = championShip.contents[3].find_all("li")
        number_of_matches = len(all_matches)
        
        for i in range(number_of_matches):
            
            # get team name
            teamA = all_matches[i].find('div',{'class':'teamA'}).text.strip()
            teamB = all_matches[i].find('div',{'class':'teamB'}).text.strip()
            
            # get team reault
            match_result = all_matches[i].find("div",{"class":"MResult"}).find_all("span",{"class":"score"})

            match_time = all_matches[i].find("div",{"class":"MResult"}).find("span",{"class":"time"}).text.strip()
            
            # get score
            score = f"{match_result[0].text.strip()} _ {match_result[1].text.strip() }"

            matches_details.append({"first_team":teamB,"result":score,"second_team":teamA,"time":match_time,"type":champiion_title})
    for i in range(len(championShips)):    
        get_match_info(championShips[i])
    
    keys = matches_details[0].keys()
    
    # open create excel file if not exist and write into
    with open("matche.csv","w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("file created")
        

    
        
date = "8/12/2023"      
page  = requests.get(f"https://www.yallakora.com/match-center/مركز-المباريات?date={date}")

main(page)    


 
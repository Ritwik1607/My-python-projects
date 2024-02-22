from selenium import webdriver
import time
import random
arr=['Sambhrant Tiwari','Yuvraj Singh','Atri Das','Rivu Chakraborty']
arr2 = [
    "sparkling",
    "mysterious",
    "whimsical",
    "effervescent",
    "enigmatic",
    "serene",
    "captivating",
    "bewitching",
    "radiant",
    "tranquil",
    "resplendent",
    "ethereal",
    "mesmerizing",
    "splendid",
    "glorious",
    "enchanting",
    "charismatic",
    "vibrant",
    "breathtaking",
    "spellbinding"
]
arr3=['No','speaker could be better','it was good','next time should be 2 way talk','there sholud have been a quiz']
web=webdriver.Chrome()
web.get('https://forms.gle/mgpZ7223t6tSQZEy6')
time.sleep(2)
exp=random.choice(arr2)
expe=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
expe.send_keys(exp)
sel_but=web.find_element('xpath','//*[@id="i9"]/div[3]/div')
sel_but.click()
sel_but1=web.find_element('xpath','//*[@id="i22"]/div[3]/div')
sel_but1.click()
com=random.choice(arr)
comm=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
comm.send_keys(com)
sel_but2=web.find_element('xpath','//*[@id="i33"]/div[3]/div')
sel_but2.click()
feed=random.choice(arr3)
fb=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')
fb.send_keys(feed)
submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()                     

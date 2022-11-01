import requests
from lxml import etree
from bs4 import BeautifulSoup


class ElPris(object):
    def __init__(self, HEADERS):  
        self.norlys = requests.get("https://norlys.dk/kundeservice/el/gaeldende-elpriser/", HEADERS)
        self.flex_sti = r'//*[@id="elprodukter"]/div/div/div/div/table[2]/tbody/tr[2]/td[2]'
        self.pulje_sti = r'//*[@id="elprodukter"]/div/div/div/div/table[1]/tbody/tr[2]/td[2]'
        self.flex, self.pulje = self.hent_priser()


    def __str__(self):
        skift, dif = self.sammenlign()
        if skift:
            return str(f"SKIFT AFTALE!!\n\nFlex Pris:\t{self.flex}\nPulje Pris:\t{self.pulje}\nDifferens:\t{dif}")
        return str(f"BEHOLD AFTALE!!\n\nFlex Pris:\t{self.flex}\nPulje Pris:\t{self.pulje}\nDifferens:\t{dif}")

    
    def pris(self, aftale):
        soup = BeautifulSoup(self.norlys.content, 'html.parser')
        dom = etree.HTML(str(soup))
        return dom.xpath(aftale)[0].text
    

    def hent_priser(self):
        flex = self.pris(self.flex_sti)
        pulje = self.pris(self.pulje_sti)
        return flex, pulje
    

    def sammenlign(self):
        flex = float(self.flex.split()[0].replace(',', '.'))
        pulje = float(self.pulje.split()[0].replace(',', '.'))
        differens = abs(flex - pulje)
        if flex > pulje:
            return True, differens
        return False, differens
        
            

if __name__ == "__main__":
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
    print(ElPris(HEADERS))
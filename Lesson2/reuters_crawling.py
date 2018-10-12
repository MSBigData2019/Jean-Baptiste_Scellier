# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup

website_prefix = "http://www.reuters.com/finance/stocks/financial-highlights/"

def main():
    print("LVMH :")
    get_values_for_company('LVMH')
    print("\nAirbus :")
    get_values_for_company('AIR')
    print("\nDanone :")
    get_values_for_company('DANO')

def get_values_for_company(company):
    get_sales_quarter_ending_for_company(company)
    get_share_price_value_for_company(company)
    get_share_price_change_for_company(company)
    get_percent_shares_owned_institutional_holders_for_company(company)
    get_dividend_yields_for_company(company)

def get_share_price_value_for_company(company):
    res = requests.get(website_prefix + '/' + company + '.PA')
    soup = BeautifulSoup(res.text, "lxml")
    tag = soup.find("div", class_= "sectionQuoteDetail")
    span = tag.find_all(re.compile("span"))
    value = span[1].text.replace("\t", "").replace("\n", "")
    print("Prix de l'action : " + value)

def get_share_price_change_for_company(company):
    res = requests.get(website_prefix + '/' + company + '.PA')
    soup = BeautifulSoup(res.text, "lxml")
    tag = soup.find("span", class_= "valueContentPercent")
    variation = tag.text.replace("\t", "").replace(" ", "").replace("\n", "")
    print("Variation du prix de l'action : " + variation)

def get_sales_quarter_ending_for_company(company):
    res = requests.get(website_prefix + '/' + company + '.PA')
    soup = BeautifulSoup(res.text, "lxml")
    div = soup.find_all("div", class_="moduleBody")
    td = div[2].find_all("td", class_="data")
    print("Ventes du dernier trimestre : " + td[1].text)

def get_percent_shares_owned_institutional_holders_for_company(company):
    res = requests.get(website_prefix + '/' + company + '.PA')
    soup = BeautifulSoup(res.text, "lxml")
    div = soup.find_all("div", class_="column2 gridPanel grid4")
    module = div[0].find_all("div", class_="moduleBody")
    tr = module[3].find_all("tr", class_="stripe")
    td = tr[0].find_all("td", class_= "data")
    print("Part des actions détenues par des institutions : " + td[0].text)

def get_dividend_yields_for_company(company):
    res = requests.get(website_prefix + '/' + company + '.PA')
    soup = BeautifulSoup(res.text, "lxml")
    div = soup.find_all("div", class_="column1 gridPanel grid8")
    module = div[0].find_all("div", class_="moduleBody")
    tr = module[3].find_all("tr", class_="stripe")
    td = tr[0].find_all("td", class_="data")
    print("Dividend yield de l'entreprise : " + td[0].text)
    print("Dividend yield de l'industrie : " + td[1].text)
    print("Dividend yield du secteur : " + td[2].text)

main()
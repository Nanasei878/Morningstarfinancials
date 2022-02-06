from bs4 import BeautifulSoup
import requests
import pandas as pd


def data_fetch(key):
    
    url= "https://www.morningstar.co.uk/uk/funds/snapshot/snapshot.aspx?id=" + key
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #lists = soup.find_all("div", {"id": "mainContentDiv"})
    
    
    lists1 = soup.find("div", {"id": "mainContentDiv"})
    title = lists1.find('div', class_="snapshotTitleBox")
    title = title.find('h1').text 
    
    
    tab1 = lists1.find('table', class_="snapshotTextColor snapshotTextFontStyle snapshotTable overviewKeyStatsTable")
    
    tab1_itmz = tab1.find_all('td',class_='line text')
    tab1_itmz = tab1.find_all('td',class_='line text')
    
    
    nav= tab1_itmz[0].text
    day_change = tab1_itmz[1].text.replace('\n', '')
    ia_setor = tab1_itmz[2].text
    isin = tab1_itmz[3].text
    initial_charge = tab1_itmz[6].text
    ongoing_charge = tab1_itmz[7].text
    
    tab1_itmz[7].text
    
    
    '''for list in lists:
            title = list.find('div', class_="snapshotTitleBox")
            title = title.find('h1').text'''
    
    
    
    tab2 = lists1.find("div", {"id": "overviewTrailingReturnsDiv"})       
    #tab2_t = tab2.find("table", _class="snapshotTextColor snapshotTextFontStyle snapshotTable overviewTrailingReturnsTable")
    
    tab2_h = tab2.find_all('tr')
    
    
    as_of = tab2_h[0].find_all('td')[1].text
    ytd = tab2_h[1].find_all('td')[1].text
    three_Years_Annualised = tab2_h[2].find_all('td')[1].text
    five_Years_Annualised = tab2_h[3].find_all('td')[1].text
    ten_Years_Annualised = tab2_h[4].find_all('td')[1].text
    
    tab2x = lists1.find_all("table", {"class": "snapshotTextColor snapshotTextFontStyle snapshotTable overviewKeyStatsTable"})   
    twelve_month_yield = tab2x[1].find('td',{"class":"value number"}).text
    
    seventeen = lists1.find('td', {"class":"col3 value number"}).text
    eigheteen = lists1.find('td', {"class":"col4 value number"}).text
    nineteen = lists1.find('td', {"class":"col5 value number"}).text
    twenty = lists1.find('td', {"class":"col6 value number"}).text
    twentyone = lists1.find('td', {"class":"col7 value number"}).text
    
    
    bmark = lists1.find_all( "span", {"class":"value"})
    benchmark = bmark[1].text
    
    info = [url,title, isin, ia_setor, benchmark,initial_charge, ongoing_charge, nav, day_change,as_of,ytd,three_Years_Annualised,
            five_Years_Annualised,ten_Years_Annualised, twelve_month_yield,twentyone,twenty,nineteen,eigheteen,seventeen]
    
    return info
info = []
for x in keyz:
    scrape = data_fetch(x)
    info.append(scrape)
info
data = [info]
df = pd.DataFrame(data, columns = ['MORNINGSTAR_LINK','NAME','ISIN','IA_SECTOR','BENCHMARK','INITIAL', 'ONGOING', 'NAV', 'DAY_CHANGE', 'AS_OF', 'YTD', '3_YEAR', '5_YEAR','10_YEAR', '12M_YIELD', '2021','2020', '2019', '2018','2017'])
df['NAV']
df.to_csv('morningstar.csv')
len(info)
info
df = pd.DataFrame(info, columns = ['MORNINGSTAR_LINK','NAME','ISIN','IA_SECTOR','BENCHMARK','INITIAL', 'ONGOING', 'NAV', 'DAY_CHANGE', 'AS_OF', 'YTD', '3_YEAR', '5_YEAR','10_YEAR', '12M_YIELD', '2021','2020', '2019', '2018','2017'])
df.to_csv('morningstar.csv')

#for yahoofinance:
#stock = soup.find_all('div', {'class' : "My(6px) Pos(r) smartphone_Mt(6px) W(100%) "})[0].find().text
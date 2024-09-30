import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    c_codes = ['arg','aus','bra','can','che','ch1','chn','cze','dnk','euz','gbr','hkg','hun','idn','irs','jpn','kor', 
               'mex', 'mys', 'nzl', 'pol', 'rus', 'sgp', 'swe', 'tha', 'twn',
               'usa', 'zaf', 'are', 'aze', 'bhr', 'col', 'cri', 'egy', 'gtm', 'hon', 'hrv', 'jor', 'kwt', 
               'lbn', 'lka', 'mda', 'nic', 'nor', 'omn', 'pak', 'per', 'phl', 'qat', 'rou', 'sau', 'tur', 'ury', 'ven', 'vnm']
    if country_code.lower() in c_codes:
        query = df[(df['iso_a3'].str.lower() == country_code.lower()) & (df['date'].str.startswith(str(year)))]
        round_a = round(query['dollar_price'].mean(),2)
    
    return round_a

def get_big_mac_price_by_country(country_code):
    c_codes = ['arg','aus','bra','can','che','ch1','chn','cze','dnk','euz','gbr','hkg','hun','idn','irs','jpn','kor', 
               'mex', 'mys', 'nzl', 'pol', 'rus', 'sgp', 'swe', 'tha', 'twn',
               'usa', 'zaf', 'are', 'aze', 'bhr', 'col', 'cri', 'egy', 'gtm', 'hon', 'hrv', 'jor', 'kwt', 
               'lbn', 'lka', 'mda', 'nic', 'nor', 'omn', 'pak', 'per', 'phl', 'qat', 'rou', 'sau', 'tur', 'ury', 'ven', 'vnm']
    if country_code.lower() in c_codes:
        query = df[(df['iso_a3'].str.lower() == country_code.lower())]
        round_b = round(query['dollar_price'].mean(),2)
    
    return round_b

def get_the_cheapest_big_mac_price_by_year(year):
    years = df[df['date'].str.startswith(str(year))]
    p_c = years['dollar_price'].min()
    link = years.query('dollar_price == @p_c')
    name = link['name'].iloc[0]
    c_name = link['iso_a3'].iloc[0].upper()
    
    return f"{name}({c_name}): ${p_c:.2f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    years = df[df['date'].str.startswith(str(year))]
    p_d = years['dollar_price'].max()
    link = years.query('dollar_price == @p_d')
    name = link['name'].iloc[0]
    c_name = link['iso_a3'].iloc[0].upper()
    
    return f"{name}({c_name}): ${p_d:.2f}"

if __name__ == "__main__":
   r_a = get_the_cheapest_big_mac_price_by_year(2009)
   print(r_a)
   r_b = get_big_mac_price_by_country("mex")
   print(r_b)
   r_c = get_the_cheapest_big_mac_price_by_year(2008)
   print(r_c)
   r_d = get_the_most_expensive_big_mac_price_by_year(2003)
   print(r_d)
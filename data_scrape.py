import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import concurrent.futures
import time

def get_table_names(link):
    source = requests.get(link).text
    soup = BeautifulSoup(source, "lxml")
    tables = [li['data-id'] for li in soup.find('ul',{'id':'data-list'}).find_all('li')]
    return tables

def run_sql(sql_query, table, fields=False):
    sql_query = sql_query.replace('TABLE_PLACEHOLDER',table)
    source = requests.get(f'https://data.ibb.gov.tr/api/3/action/datastore_search_sql?sql={sql_query}')
    try:
        result = pd.DataFrame(json.loads(source.text)['result']['records'])
        if fields:
            return pd.DataFrame(json.loads(source.text)['result']['fields'])
    except KeyError:
        result = json.loads(source.text)
    return result


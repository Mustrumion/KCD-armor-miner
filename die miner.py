import xml.etree.ElementTree as et
import pandas as pd
import os

def get_proba(path: str = os.path.join("Data", "die.xml")) -> pd.DataFrame:
    cols = [f'side_weight_{i+1}' for i in range(6)]
    cols.append('item_id')

    root = et.parse(path)
    rows = root.findall('.//row')

    xml_data = [[row.get(col) for col in cols] 
        for row in rows]

    df_xml = pd.DataFrame(xml_data, columns=cols)
    df_xml = df_xml.set_index('item_id')
    df_xml = df_xml.apply(pd.to_numeric)
    odds_sum = df_xml.sum(axis=1)

    df_xml = df_xml.div(odds_sum, axis=0)
    return df_xml


def get_ui_names(path: str = os.path.join("Data", "player_item.xml")) -> pd.DataFrame:
    cols = ['item_id', 'ui_name']

    root = et.parse(path)
    rows = root.findall('.//row')

    xml_data = [[row.get('item_id'), row.get('ui_name')] 
        for row in rows]
    df_xml = pd.DataFrame(xml_data, columns=cols)
    return df_xml


def get_actual_names(path: str = os.path.join("Data", "text_ui_items.xml")) -> pd.DataFrame:
    cols = ['ui_name', 'name modded', 'name vanilla']

    root = et.parse(path)
    rows = root.findall('.//Row')

    xml_data = [[row[0].text, row[2].text, row[1].text] 
        for row in rows]
    df_xml = pd.DataFrame(xml_data, columns=cols)
    return df_xml
	

proba_df = get_proba()
names_df = get_ui_names()
text_df = get_actual_names()

df = proba_df.join(names_df.set_index('item_id'), how='left')
df = df.reset_index(level=0).set_index('ui_name').join(text_df.set_index('ui_name'), how='left')

directory = 'Die Results'

if not os.path.exists(directory):
    os.mkdir(directory)

df.to_csv(f'{directory}/All.csv')
print(df)
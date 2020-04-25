import xml.etree.ElementTree as et
import pandas as pd

def get_defense(path: str = "armor.xml") -> pd.DataFrame:
    cols = ['item_id', 'armor_type_id', 'noise', 'stab_def', 'slash_def', 'smash_def', 'max_status']

    root = et.parse(path)
    rows = root.findall('.//row')

    xml_data = [[row.get('item_id'), row.get('armor_type_id'), row.get('noise'), 
        row.get('stab_def'), row.get('slash_def'), row.get('smash_def'), row.get('max_status')] 
        for row in rows]

    df_xml = pd.DataFrame(xml_data, columns=cols)
    df_xml['noise'] = df_xml['noise'].astype(float) * 100
    df_xml['slash_def'] = df_xml['slash_def'].astype(float) * 10
    df_xml['smash_def'] = df_xml['smash_def'].astype(float) * 10
    df_xml['stab_def'] = df_xml['stab_def'].astype(float) * 10
    return df_xml


def get_ui_names(path: str = "player_item.xml") -> pd.DataFrame:
    cols = ['item_id', 'ui_name']

    root = et.parse(path)
    rows = root.findall('.//row')

    xml_data = [[row.get('item_id'), row.get('ui_name')] 
        for row in rows]
    df_xml = pd.DataFrame(xml_data, columns=cols)
    return df_xml


def get_actual_names(path: str = "text_ui_items.xml") -> pd.DataFrame:
    cols = ['ui_name', 'name']

    root = et.parse(path)
    rows = root.findall('.//Row')

    xml_data = [[row[0].text, row[2].text] 
        for row in rows]
    df_xml = pd.DataFrame(xml_data, columns=cols)
    return df_xml


def get_charisma(path: str = "equippable_item.xml") -> pd.DataFrame:
    cols = ['item_id', 'charisma', 'conspicuousness', 'visibility']

    root = et.parse(path)
    rows = root.findall('.//row')

    xml_data = [[row.get('item_id'), row.get('charisma'),
        row.get('conspicuousness'), row.get('visibility')] 
        for row in rows]
    df_xml = pd.DataFrame(xml_data, columns=cols)
    df_xml['conspicuousness'] = (df_xml['conspicuousness'].astype(float) + 1) * 50
    df_xml['visibility'] = (df_xml['visibility'].astype(float) + 1) * 50
    return df_xml


def get_weight(path: str = "pickable_item.xml") -> pd.DataFrame:
    cols = ['item_id', 'weight']

    root = et.parse(path)
    rows = root.findall('.//row')

    xml_data = [[row.get('item_id'), row.get('weight')] 
        for row in rows]
    df_xml = pd.DataFrame(xml_data, columns=cols)
    df_xml['weight'] = df_xml['weight'].astype(float)
    return df_xml

defense_df = get_defense()
names_df = get_ui_names()
charisma_df = get_charisma()
text_df = get_actual_names()
weight_df = get_weight()

df = defense_df.set_index('item_id').join(names_df.set_index('item_id'), how='left')
df = df.join(charisma_df.set_index('item_id'), how='left')
df = df.join(weight_df.set_index('item_id'), how='left')
df = df.reset_index(level=0).set_index('ui_name').join(text_df.set_index('ui_name'), how='left')
df.dropna(inplace= True)

# this won't work for non-modded text_ui_items
df = df[df['name'].str.contains("-")]
df[['category', 'name']] = df['name'].str.split("-", 1, expand=True)
df['category'] = df['category'].str.strip()
df['name'] = df['name'].str.strip()

groups = [pd.DataFrame(y) for x, y in df.groupby('category', as_index=False)]

for group in groups:
    group.to_csv(f'{group["category"].iloc[0]}.csv')
df.to_csv('All.csv')
print(df)
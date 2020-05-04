import xmltodict 
import os
import shutil
import datetime
from pathlib import Path

result_dir = Path('EeasyRepReturns')

shutil.rmtree(result_dir, ignore_errors=True)

edited_name = 'reputation_change.xml'

with open('reputation_change.xml', 'r') as repfile:
    data = xmltodict.parse(repfile.read())

for row in data['database']['table']['rows']['row']:
    change = float(row['@change'])
    if change > 0:
        row['@change'] = str(change * 2.0)
    elif change < 0:
        row['@change'] = str(change * 0.5)

resfile = result_dir/'Libs'/'Tables'/'rpg'/edited_name
os.makedirs(str(resfile.parent), exist_ok=True)

with open(str(resfile), 'w+') as repfile:
    repfile.write(xmltodict.unparse(data))

shutil.make_archive(str(result_dir), 'zip', str(result_dir))
shutil.rmtree(result_dir, ignore_errors=True)

desired_pak_loc = result_dir / 'Data' / f'{result_dir.stem}.pak'
os.makedirs(str(desired_pak_loc.parent), exist_ok=True) 

os.rename(f'{result_dir.stem}.zip', str(desired_pak_loc))

with open(str(result_dir / 'mod.manifest'), 'w+') as manifest:
    manifest.write(f'''<?xml version="1.07" encoding="utf-8"?>
<kcd_mod>
    <info>
        <name>EeasyRepReturns</name>
        <description>Makes positive reputation twice as impactful, while negative rep gain gets halved. FU Local Hero perk.</description>
        <author>Mustrum</author>
        <version>1.9.5</version>
        <created_on>{datetime.datetime.today().strftime("%d.%m.%Y")}</created_on>
    </info>
</kcd_mod>''')

shutil.make_archive(str(result_dir), 'zip', str(result_dir))

shutil.rmtree(result_dir, ignore_errors=True)

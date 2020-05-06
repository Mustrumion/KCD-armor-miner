# General info

Under Creative Commons 3.0.

This repository is dedicated for storage and versioning of my mods and data miners for KCD.

# Purpose

armor miner.py - extracts armor statistics from the game files 

die miner.py - extracts weighted dice chance statistics 

easy_reputation_mod_creator.py - creates Easy Reputation Returns mod

# Usage

Run miner.py with extrated game xmls in the working directory.

It uses modded item names to categorize items (I made this script for my own use, so I didn't bother to find the actual connections). There will be a modification needed for this to work with default/other language item names.

The mod in question is 'A Sorted Inventory' from Nexus Mods. Highly recommended QOL mod.

# Data

Data needed for the scripts comes from game files. All xmls apart from text_ui_items.xml can be found in:

<game dir>\data\Tables.pak\Libs\Tables (Tables.pak needs to be opened with an archive manager, I recommand 7zip)

text_ui_items.xml can be found among localization files.

Script results are uploaded to the repo in the Results directory.

# Google sheets with the data
for dice:
https://docs.google.com/spreadsheets/d/1Ojv0jCWhfojsWmgvAMHoIuFAROpXosgv-0-KoGFFVqM/edit?usp=sharing

for armor:
https://docs.google.com/spreadsheets/d/1Y4kKKTVA_ZK1SWkw0IlVLF3m-TrxJighvUEM-3JZRP4/edit?usp=sharing

The Score column was added by me and is completely arbitrary. It was intended to measure usefulness of items for my slightly-thievering-knight Henry.

There is no weight data in that sheet since I found where it is stored after the sheet was complete. I didn't have enough energy to update it.

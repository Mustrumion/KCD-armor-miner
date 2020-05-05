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

Data in the repo comes from version 1.9.5. All xmls apart from text_ui_items.xml can be found in the game files:

<game dir>\data\Tables.pak\Libs\Tables\item (Tables.pak needs to be opened with an archive manager, I recommand 7zip)

text_ui_items.xml can be found among localization files.

Script results are also uploaded to the repo in the Results directory.

# Visibility and Conspiciousness

The values outputed by the script are the ones shown in the item description ingame. 

They strongly correlete with the actual active values, but it seems that the game lies to you to not overwhelm you with the visibility mechanic.
It seems like the most of the armor is divided into sections, and only the outermost (and possibly second) layer covering other armor counts towards visibility and conspiciousness. Pretty cool mechanic.

# Google sheet with the data
for dice:
https://docs.google.com/spreadsheets/d/1Ojv0jCWhfojsWmgvAMHoIuFAROpXosgv-0-KoGFFVqM/edit?usp=sharing

for armor:
https://docs.google.com/spreadsheets/d/1Y4kKKTVA_ZK1SWkw0IlVLF3m-TrxJighvUEM-3JZRP4/edit?usp=sharing

The Score column was added by me and is completely arbitrary. It was intended to measure usefulness of items for my slightly-thievering-knight Henry.

There is no weight data in that sheet since I found where it is stored after the sheet was complete. I didn't have enough energy to update it.

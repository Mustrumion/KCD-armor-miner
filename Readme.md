# Usage

Run miner.py with extrated game xmls in the working directory.

It uses modded item names to categorize items (I made this script for my own use, so I didn't bother to find the actual connections). There will be a modification needed to work with default/other language item names.

The mod in question is 'A Sorted Inventory' from Nexus Mods. Highly recommended QOL mod.

# Data

All xmls apart from text_ui_items.xml can be found in the game files:

<game dir>\data\Tables.pak\Libs\Tables\item (Tables.pak needs to be opened with an archive manager, I recommand 7zip)

text_ui_items.xml can be found among localization files.

# Visibility and Conspiciousness

The values outputed by the script are the ones shown in the item decription ingame. 

They strongly correlete with the actual active values, but it seems that the game lies to you to not overwhelm you with the visibility mechanic.
It seems like the most of the armor is divided into sections, and only the outermost (and possibly second) layer covering other armor counts towards visibility and conspiciousness. Pretty cool mechanic.

# Google sheet with the data

https://docs.google.com/spreadsheets/d/1Y4kKKTVA_ZK1SWkw0IlVLF3m-TrxJighvUEM-3JZRP4/edit?usp=sharing

The Score column was added by me and is completely arbitrary. It was intended to measure usefulness of items for my slightly-thievering-virgin-knight Henry (from Skalitz).

There is no weight data in that sheet since I found where it is stored after the sheet was complete. I didn't have enough energy to update it.
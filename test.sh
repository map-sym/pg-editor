#! /bin/bash

# author: Krzysztof Czarnecki
# email: czarnecki.krzysiek@gmail.com
# application: EMPER simulator
# brief: economic and strategic simulator
# opensource licence: GPL-3.0

./verify_database.py example.db

# ./dump_tables.sh example.db
# ./find_partial.py example.db

./list_params.py example.db
./list_nations.py example.db
./list_terrains.py example.db

./extract_tmap.py example.db tmap.ppm --resize=1 --border=0.5 
./extract_pmap.py example.db pmap-loo.ppm --palette=default.json --resize=2 --rivers LOO
./extract_pmap.py example.db pmap-par.ppm --palette=default.json --resize=2 --rivers PAR

./gener_smap.py example.db RENEW 771188:10 BB22FF:8 COAST:1 BUILDABLE:1
./gener_smap.py example.db STONE 440022:50 884400:50 FF4400:10 FFAA11:1 FFDD44:0.3 TUNDR:0.2 COAST:0.2 BUILDABLE:1
./gener_smap.py example.db AGRA 771188:25 BB22FF:25 448844:5 33BB33:20 FFAA11:10 884400:1 FFDD44:0.07 COAST:20 HLINE:230 SIGMA:11000 THOLD:0.06 BUILDABLE:1
./gener_smap.py example.db WOOD 771188:30 BB22FF:30 448844:30 33BB33:18 FFAA11:2 COAST:20 AAAA99:-20 FFDD44:-0.2 HLINE:230 SIGMA:9200 THOLD:0.2 BUILDABLE:1

./extract_smap.py example.db smap-stone.ppm --resize=2 --palette=default.json --rivers STONE
./extract_smap.py example.db smap-renew.ppm --resize=2 --palette=default.json --rivers RENEW
./extract_smap.py example.db smap-gold.ppm --resize=2 --palette=default.json --rivers GOLD
./extract_smap.py example.db smap-wood.ppm --resize=2 --palette=default.json --rivers WOOD
./extract_smap.py example.db smap-agra.ppm --resize=2 --palette=default.json --rivers AGRA

./extract_nmap.py example.db nmap-2.ppm --resize=1 --palette=default.json --rivers  MZG:880000 HMB DUQ BGY GOU GOP OXS MRH BJO ZBD GDV:880000
./calc_chain.py example.db MZG HMB DUQ BGY GOU GOP OXS MRH BJO ZBD GDV

./extract_nmap.py example.db nmap-3.ppm --resize=1 --palette=default.json --rivers MZG:880000 ANK QNT GTP JJA ZYQ YQF NYU BFN XJK ODT GDV:880000
./calc_chain.py example.db MZG ANK QNT GTP JJA ZYQ YQF NYU BFN XJK ODT GDV







# geeqie node.ppm
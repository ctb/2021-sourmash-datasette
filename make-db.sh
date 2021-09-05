#! /bin/bash
rm -f gathertax.db
data/process-tax.py data/*.csv -o gather.csv
csvs-to-sqlite gather.csv gathertax.db \
               -t gathertax -c domain -c phylum -c order -c class -c family \
               -c genus -c species \
               -f lineage

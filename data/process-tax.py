#! /usr/bin/env python
import argparse
import sys
import csv
import itertools


def break_out_lineages(lin):
    new_d = {}
    taxlist = ('domain', 'phylum', 'class', 'order', 'family', 'genus',
               'species')
    lin = lin.split(';')
    for rank, name in itertools.zip_longest(taxlist, lin, fillvalue=''):
        new_d[rank] = name

    return new_d


def main():
    p = argparse.ArgumentParser()
    p.add_argument('gathertax_csvs', nargs='+')
    p.add_argument('-o', '--output', required=True)
    args = p.parse_args()

    new_rows = []
    for inpfile in args.gathertax_csvs:
        with open(inpfile, newline='') as fp:
            rows = csv.DictReader(fp)
            for row in rows:
                lineage = row['lineage']
                new_cols = break_out_lineages(lineage)

                row.update(new_cols)
                new_rows.append(row)

    if not new_rows:
        print("No rows loaded!?", file=sys.stderr)
        sys.exit(-1)

    with open(args.output, 'w', newline="") as outfp:
        w = csv.DictWriter(outfp, fieldnames=new_rows[0].keys())
        w.writeheader()

        for row in new_rows:
            w.writerow(row)

    print(f"Wrote {len(new_rows)} rows.", file=sys.stderr)


if __name__ == '__main__':
    sys.exit(main())

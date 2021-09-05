# 2021-sourmash-datasette

Exploring sourmash 'gather' output taxonomy with datasette.

## Quickstart

First install datasette, csvs-to-sqlite.

Then:

```
./make-db.sh
datasette gathertax.db --static sourmash:static/ -o
```

Then go to /sourmash/ at the resulting URL.



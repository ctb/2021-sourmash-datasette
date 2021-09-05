# 2021-sourmash-datasette

Exploring sourmash 'gather' output taxonomy with datasette.

## Quickstart

First install datasette, csvs-to-sqlite.

Then:

```
./make-db.sh
datasette gathertax.db --static foo:static/ -o
```

Then go to /foo/ at the resulting URL.



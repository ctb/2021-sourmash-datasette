# 2021-sourmash-datasette

Exploring sourmash 'gather' and 'taxonomy' output with
[datasette](https://datasette.io/).

## Quickstart

First install [datasette](https://datasette.io/) and
[csvs-to-sqlite](https://datasette.io/tools/csvs-to-sqlite).
This can be done with conda or mamba:
```
conda env create -n datasette -f environment.yml
conda activate datasette
```

Then run:

```
# convert sourmash gather/sourmash tax output lineages into their own cols
./make-db.sh

# run datasette!
datasette gathertax.db --static sourmash:static/ -o
```

Finally, go to `/sourmash/index.html` at your datasette site - by
default, it should be at
[127.0.0.1:8001/sourmash/index.html](http://127.0.0.1:8001/sourmash/index.html).

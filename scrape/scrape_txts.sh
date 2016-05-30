#!/usr/bin/env bash
head -5 data/ids | xargs -L1 -I{} bash -c "curl 'http://oeis.org/search?q=id:{}&fmt=text' > scrape/txts/{}.txt"

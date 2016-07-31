#!/usr/bin/env bash
IDS_FILE="$1"
: ${IDS_FILE:='data/ids'}
MAX_IDS=5
head "-${MAX_IDS}" "${IDS_FILE}" | xargs -L1 -I{} bash -c "curl 'http://oeis.org/search?q=id:{}&fmt=text' > scrape/txts/{}.txt"

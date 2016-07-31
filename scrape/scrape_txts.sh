#!/usr/bin/env bash
IDS_FILE="$1"
: ${IDS_FILE:='data/ids'}
MAX_IDS=5
TXTS_DIR='scrape/txts'
URL='http://oeis.org/search?q=id:'
head "-${MAX_IDS}" "${IDS_FILE}" | xargs -L1 -I{} bash -c "[[ -f ${TXTS_DIR}/{}.txt ]] || curl '${URL}{}&fmt=text' > ${TXTS_DIR}/{}.txt"

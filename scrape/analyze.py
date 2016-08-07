#!/usr/bin/env python3

import tempfile
import subprocess

LOCAL_TXTS_PATH = 'scrape/txts/'
MAX_IDS = 5


# Input: a list of ids (Max: 5)
#
# Download all their texts (unless they already exist)
def scrape(ids):
    if len(ids) > MAX_IDS:
        return None
    ids_file = tempfile.NamedTemporaryFile(mode='w+t')
    for i in ids:
        ids_file.write("%s\n" % i)
    ids_file.flush()
    subprocess.run(
        ['bash', 'scrape/scrape_txts.sh', ids_file.name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )


# Parse a formula block, and add the whole black to the result.
# A block is a formula that is either:
# 1. a single row
# 2. sequence (pun intended :) of consecutive rows,
# marked by (Start) and (End), e.g.
#
# %F A000009 From Evangelos Georgiadis, Andrew V. Sutherland,
#   Kiran S. Kedlaya (egeorg(AT)mit.edu), Mar 03 2009: (Start)
# %F A000009 a(0)=1. a(n)= 2*(Sum_{k=1} (-1)^(k+1) a(n-k^2)) + sigma(n) where
# %F A000009 sigma(n)= (-1)^(j) if (n=(j*(3*j+1))/2 OR n=(j*(3*j-1))/2)
# %F A000009 otherwise sigma(n)=0. (End)
def parse_formula(last_state, content, res):
    if content.endswith("(Start)"):
        formula_state = "start"
    elif content.endswith("(End)"):
        formula_state = "end"
    else:
        formula_state = "in_out"
    if formula_state not in ["start", "end"]:
        if last_state == "start":
            formula_state = "in"
        elif last_state == "end":
            formula_state = "out"
        else:
            formula_state = last_state
    if formula_state in ["start", "out"]:
        res.append(content)
    else:
        res[-1] += "\n{}".format(content)

    return formula_state


# Input: a list of ids (Max: 5)
#
# Extract fields from the texts of their corresponding series:
# (i) list of keywords for each sequence.
#     Extract from the field:  KEYWORD
# (ii) a graph connecting all pairs of sequences,
#     where edges are also directed and labeles.
#     Extract from the field:  CROSSREFS
# (iii) formulas for each sequence.
#     Extract from the field : FORMULA
def parse(ids):
    res = {}
    for i in ids:
        res[i] = {}
        res[i]["refs"] = []
        res[i]["formulas"] = []
        res[i]["keywords"] = []
        file = open(LOCAL_TXTS_PATH + i + '.txt', 'rt')
        # 2 chars (%F) + 2 spaces = 4
        prefix_len = 4 + len(i)
        formula_state = "out"
        for line in file:
            content = line[prefix_len:-1]
            if line[0:2] == '%K':
                res[i]['keywords'] += content.split(',')
            if line[0:2] == '%F':
                formula_state = parse_formula(
                                    formula_state,
                                    content,
                                    res[i]['formulas']
                                )
            if line[0:2] == '%Y':
                res[i]["refs"].append(content)
    return res


if __name__ == '__main__':
    ids = ['A000009', 'A000010']
    scrape(ids)
    print(parse(ids))

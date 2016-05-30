#!/usr/bin/env bash
cat data/names | sed '/^#/d' | cut -d' ' -f1 > data/ids

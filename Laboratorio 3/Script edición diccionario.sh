#!/bin/bash

sed -E '/^[0-9]/d; s/^(.)(.*)$/\u\1\20/' rockyou.txt > rockyou_mod.dic

wc -l rockyou_mod.dic

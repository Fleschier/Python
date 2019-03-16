#! /usr/bin/env python
#coding=utf-8

def clear_text(textlines):
    lines=[]
    for line in textlines:
        line=line.strip()
        if len(line)>0:
            lines.append(line)
    return ' '.join(lines)

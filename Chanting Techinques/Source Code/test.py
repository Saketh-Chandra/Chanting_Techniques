import dhandapatha as dh
import dwajapatha as dw
import ghanapatha as gh
import jathapatha as ja
import kramapatha as kr
import malapatha as ma
import rathapatha as ra
import Rekhapatha as re
import sikhapatha as si


def printf(x):
    for a in x:
        print(' '.join(a))


s="1 2 3 4 5 6"
aa=gh.ghanapatha(s)
printf(aa)

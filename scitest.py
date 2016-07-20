# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:18:58 2016

@author: virginiasaulnier
"""
from io import StringIO
from skbio import DistanceMatrix
from skbio import fisher_alpha

dm_fh =StringIO("\ta\tb\tc\n"
                "a\t0.0\t0.5\t1.0\n"
                "b\t0.5\t0.0\t0.75\n"
                "c\t1.0\t0.75\t0.0\n")
                
dm = DistanceMatrix.read(dm_fh)
print(dm)

my_pairs= StringIO("ac,gt,cg,gc,at,ta,gc,ta,tg")
dm2 = DistanceMatrix.from_iterable(my_pairs,metric= fisher_alpha(),key=id)
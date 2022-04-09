# Project-1008-HSE

## Let's start with the **Analysis of hydrogen bonds.ipynb** file
>goal: to get maps from the file created by gromacs name_file.xpm

+ Adding libraries
```py
import numpy as np
import matplotlib.pyplot as plt
import re
from matplotlib.backends.backend_pdf import PdfPages
```
+ adding your hbond file for gromacs
#### **instead of you_name_file.txt insert the name of your file**
```py
reader = open('you_name_file.txt', 'r')
data = reader.read()
```
It looks like this:
```
"                                                                                                                                                                o                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      o                o          oo                                   ooo   o                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      o    oo         o                 o                 o   o                                                                                                                                                                                              o                o       o           o                                                                                                          o                    o o    oo                o           o                                                                             o                                              o              o         o        o                    oo                o                                                                                                              o     o       o                                                                                                   oo o  o                         o        o  o    o               o                   o oo ooo ooo      oo o  o     ooooo ooo   o oo ooo oo        o         oo                        ooooooo   o        o                                o o  o                  o  oo     o oo  o                 o    oo oo  o o o "
```
+ Next, run the rest of the code:
```py
fig = plt.figure(figsize=(20, 13))
splitted = list(map(lambda x: x.strip().replace('"', ''), data.split('",')))
maxx = len(splitted)

for i, line in enumerate(splitted):
  nums = line.replace("o", str(maxx-i)).replace(" ","0")
  pattern = f"{str(maxx-i)}|0"
  nums = re.findall(pattern, nums)
  plot_data = np.array(list(map(int, nums)))
  idx = list(map(bool, plot_data))
  figure = plt.plot(np.arange(len(plot_data))[idx], plot_data[idx], 'ro',  markersize=2)
fig.savefig('my drawing file.pdf')
```
### The result will be saved in the "my drawing" files
<br>
<br>
<br>
<br>

# Working with the file **formatting contacts between amino acid residues_txt or formatting contacts between amino acid residues_csv.py**

>goal: to format the ResCont file

## The difference between these files is in the output file it is txt or csv as the name suggests
+ adding your ResCont file 
```py
reader = open('ResCont.txt', 'r')
```
It looks like this:
```
0
   0    0    2 ASP   N     :   0    0    2 ASP   N     d=0.00 ,   0    0    2 ASP   CA    d=1.51 ,   0    0    2 ASP   CB    d=2.47 ,   0    0    2 ASP   CG    d=2.95 ,   0    0    2 ASP   OD1   d=2.83 ,   0    0    2 ASP   OD2   d=4.00 ,   0    0    2 ASP   C     d=2.57 ,   0    0    2 ASP   O     d=3.04 ,   0    0    3 VAL   N     d=3.56 ,   0    0    3 VAL   CA    d=4.94 ,
   0    0    2 ASP   CA    :   0    0    2 ASP   N     d=1.51 ,   0    0    2 ASP   CA    d=0.00 ,   0    0    2 ASP   CB    d=1.48 ,   0    0    2 ASP   CG    d=2.58 ,   0    0    2 ASP   OD1   d=2.87 ,   0    0    2 ASP   OD2   d=3.70 ,   0    0    2 ASP   C     d=1.57 ,   0    0    2 ASP   O     d=2.49 ,   0    0    3 VAL   N     d=2.38 ,   0    0    3 VAL   CA    d=3.79 ,   0    0    3 VAL   CB    d=4.79 ,   0    0    3 VAL   CG2   d=4.98 ,   0    0    3 VAL   C     d=4.38 ,   0    0    3 VAL   O     d=4.20 ,   0    0   50 LEU   O     d=4.28 ,   0    0   52 HIS   NE2   d=4.98 ,
```
+ Next, run the rest of the code
### The result will be saved in the "result" file
<br>
<br>
<br>
<br>

# Working with the file **contacts between amino acid residues.ipynb**
>goal: get maps from a file ResCont.txt
+ Adding libraries
```py
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid') # стиль графиков 
import matplotlib.pyplot as plt
from matplotlib import cm
import json
import math,sys,re,os,time
from argparse import ArgumentParser
import matplotlib
matplotlib.use('Agg')
import matplotlib.gridspec as gridspec
from matplotlib.colors import colorConverter,ListedColormap
```
There should be a file in the folder with the python file ResCont.txt
+ Next, run code

**requires an ide that supports the output of cards to the display**

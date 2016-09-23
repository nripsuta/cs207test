{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;}
{\colortbl;\red255\green255\blue255;\red83\green83\blue83;\red245\green245\blue245;\red15\green112\blue1;
\red38\green38\blue38;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
%%
\f1\b \cf4 file
\f0\b0 \cf5  amath.py\
\
def myaverage(l:list)->float:\
    """\
    Calculate the average of list l\
    \
    Examples:\
    \
    >>> myaverage([1,2])\
    1.5\
    \
    """\
    n = len(l)\
    if n==0:\
        raise ValueError("cant calculate mean of length 0 list")\
    try:\
        thesum = sum(l)\
    except:\
        raise TypeError("Cannot sum things of different types")\
    average = thesum/n\
    return average\
\
def mymedian(l:list)->float:\
    """\
    Calculate the average of list l\
    \
    Examples:\
    \
    >>> mymedian([1,2,3])\
    2\
    \
    >>> mymedian([1,2,3,4])\
    2.5\
    """\
    try:\
        lsorted = sorted(l)\
    except:\
        raise TypeError("Unable to sort array")\
    n = len(lsorted)\
    if n==0:\
        raise ValueError("cant calculate median of length 0 list")\
    mididx = len(lsorted)//2\
    if len(lsorted) % 2 == 0: #even\
        return (lsorted[mididx-1] + lsorted[mididx])/2\
    else:\
        return lsorted[mididx]}
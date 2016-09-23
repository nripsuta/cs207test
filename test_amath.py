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
\f0\b0 \cf5  test_amath.py\
\
from pytest import raises\
from amath import myaverage, mymedian\
\
def test_mymath_mean():\
    assert myaverage([9,3]) == 6\
\
def test_char():\
    with raises(TypeError):\
        myaverage(['a',3])\
\
def test_mymath():\
    assert mymedian([9,3, 6]) == 6\
    \
def test_zero_median():\
    with raises(ValueError):\
        mymedian([])\
        \
def test_char_median():\
    with raises(TypeError):\
        mymedian(['a', 3])}
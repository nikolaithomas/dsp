[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
#This problem is asking us to create a histogram of the actual number of people under 18 in a family vs the number of people under 18 self reported by children within the family. This creates a bias in the data as families with more children will have each child report the number of children within their family whereas families with 0 children would not be represented as their child could not self report. In addition families with a small number of children would have less reports representing their family size as they have fewer children to participate in the survey. I first imported the 2002FemResp and created a data frame, and cleaned it. Then I created a PMF of the biased data to be graphed against the intrinsic actual PMF. Finally I plotted both PMFs and computed the means. The PMFs for the biased eliminated all of the data for households with 0 children. The mean of the actual pmf was 1.0242051550438309 while the mean of the biased was 2.4036791006642821. Heavily skewed.
from __future__ import print_function

import numpy as np
import sys
import nsfg
import thinkstats2
import thinkplot
%matplotlib inline

def ReadFemRespondent(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    pass

def main(script):
    resp = ReadFemResp()
    
if __name__ == '__main__':
    main(sys.argv)

def BiasPmf(pmf, label):
        new_pmf = pmf.Copy(label=label)
        
        for x, p in pmf.Items():
            new_pmf.Mult(x, x)
        new_pmf.Normalize()
        return new_pmf

pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')    
biased = BiasPmf(pmf, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()
biased.Mean()
pmf.Mean()


In this exercise the author is asking us to compute the Cohen's d as well as whether the first babies are lighter or heavier than others. My results indicate that the first babies are lighter than the other babies according to their means (7.2 lbs vs 7.3) although the first babies do have a larger variance. Our cohen d value was negative in this case with a value of -0.08867 as compared to the cohen d for the pregnancy length which was 0.02888. From what I understand anything less than a 0.20 Cohen d is a small effect. It looks like the larger differences in weights is what drove the Cohen d standard deviation to be larger for the weights. These standard deviations of around 0.1 are both indicative that the distributions of both birth lengths and weights of both the first and other babies are highly similar.



from __future__ import print_function

import math
import numpy as np

import nsfg
import thinkstats2
import thinkplot

#Here i used the code from the text to create Dataframes from which I would evaluate the means and variances
def MakeFrames():
    preg = nsfg.ReadFemPreg()

    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    assert len(live) == 9148
    assert len(firsts) == 4413
    assert len(others) == 4735

    return live, firsts, others
#this section caculates the means, std devs, and variances, assigns them to variables, and then uses the thinkstats2 Cohen effect function which i imported with thinkstats2 to calculate the Cohen d.
def Weightdiff(live, firsts, others):
    mean = live.totalwgt_lb.mean()
    var = live.totalwgt_lb.var()
    std = live.totalwgt_lb.std()

    print('Live mean total weight', mean)
    print('Live variance total weight', var)
    print('Live std total weight', std)
    

    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()
    
    print('Mean weight')
    print('First babies', mean1)
    print('Others', mean2)

    print('Variance in weight')
    print('First babies', var1)
    print('Others', var2)

    print('Difference in lbs', mean1 - mean2)

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)


def main(script):
    live, firsts, others = MakeFrames()
    Weightdiff(live, firsts, others)

if __name__ == '__main__':
    import sys
    main(sys.argv)


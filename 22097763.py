import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    """


    Returns
    -------
    data : TYPE
        DESCRIPTION.

    """
    data = np.genfromtxt('data3-2.csv', delimiter=',')
    return data


def generate_bargraph():
    """


    Returns
    -------
    xdst : TYPE
        DESCRIPTION.
    ydst : TYPE
        DESCRIPTION.
    wdst : TYPE
        DESCRIPTION.
    cdst : TYPE
        DESCRIPTION.
    oedge : TYPE
        DESCRIPTION.

    """

    data = read_data()
    ohist, oedge = np.histogram(data, bins=35)

    # calculate bin centre locations and bin widths
    xdst = (oedge[1:]+oedge[:-1])/2
    wdst = oedge[1:]-oedge[:-1]

    # normalise the distribution
    # ydist is a discrete PDF
    ydst = ohist/np.sum(ohist)

    # cumulative distribution
    cdst = np.cumsum(ydst)

    plt.figure(0, dpi=300)

    # Plot the PDF using bar graph
    plt.bar(xdst, ydst, width=0.8*wdst)
    plt.title("Salaries distribution in some European country", fontsize=16)
    # labelling
    plt.xlabel('salary', fontsize=15)
    plt.ylabel('Probability', fontsize=15)

    return xdst, ydst, wdst, cdst, oedge


def mean_function(xdst, ydst, wdst, cdst, data):
    """


    Parameters
    ----------
    xdst : TYPE
        DESCRIPTION.
    ydst : TYPE
        DESCRIPTION.
    wdst : TYPE
        DESCRIPTION.
    cdst : TYPE
        DESCRIPTION.
    data : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    xdst = xdst
    ydst = ydst
    wdst = wdst
    data = data
    cdst = cdst

    # finding the PDF mean
    xmean = np.sum(xdst*ydst)
    print("bins = 35")
    print("mean = ", data.mean())
    print("PDF mean = ", xmean)

    # plotting the mean
    text = ''' Mean value: {}'''.format(xmean.astype(int))
    plt.plot([xmean, xmean], [0.0, max(ydst)], c='red', label=text)


def distributions(xdst, ydst, wdst, cdst, data, oedge):
    """


    Parameters
    ----------
    xdst : TYPE
        DESCRIPTION.
    ydst : TYPE
        DESCRIPTION.
    wdst : TYPE
        DESCRIPTION.
    cdst : TYPE
        DESCRIPTION.
    data : TYPE
        DESCRIPTION.
    oedge : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    xdst = xdst
    ydst = ydst
    wdst = wdst
    cdst = cdst
    data = data

    '''find value X such that 0.33 of the distribution corresponds to
      values <X value
    '''
    indx = np.argmin(np.abs(cdst-0.33))
    xlow = oedge[indx]
    plt.bar(xdst[0:indx], ydst[0:indx], width=0.9*wdst[0:indx], color='green')
    text = ''' 33% of claims are below £{}'''.format(xlow.astype(int))
    plt.plot([xlow, xlow], [0.0, max(ydst)], c='black', label=text)

    plt.legend()


# all functions call from the source
xdst, ydst, wdst, cdst, oedge = generate_bargraph()
data = read_data()
mean_function(xdst, ydst, wdst, cdst, data)
distributions(xdst, ydst, wdst, cdst, data, oedge)
# save figure
plt.savefig("final_page.png", dpi=300)
plt.show()

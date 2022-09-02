import numpy as np
import sys
import time


def enumerate_progress(list, label=''):
    """Simple progress bar.

    """
    t0 = time.time()
    ni = len(list)
    for i, v in enumerate(list):
        yield i, v
        ppct = int(100. * (i - 1) / ni)
        cpct = int(100. * (i + 0) / ni)
        if cpct > ppct:
            dt = time.time() - t0
            dh = np.floor(dt / 3600.)
            dm = np.floor(np.mod(dt, 3600.) / 60.)
            ds = np.floor(np.mod(dt, 60))
            sys.stdout.write("\r [" + ('%02d:%02d:%02d' % (dh, dm, ds)) + "] " +
                             label + " " + int(10. * cpct / 100) * "-" + "> " + ("%02d" % cpct) + r"%")
            sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()




def pp2kk(ls):
    """Returns the normalisation to convert phi specrum into kappa spectrum
     
     :math: `C_L^{\kappa\kappa} = (L(L+1))^2 / 4 C_L^{\phi\phi}`
     
      """
    return ls**2*(ls+1)**2/4.


def kk2pp(ls):
    """Converts lensing convergence power spectrum into lensing potential power spectrum.
    """
    return cli(pp2kk(ls))

def cli(cl):
    """Array pseudo-inverse

    """
    clinv = np.zeros_like(cl)
    clinv[np.where(cl != 0.)] = 1. / cl[np.where(cl != 0.)]
    return clinv


import numpy as np
import itertools
from fishlib.utils import enumerate_progress



def get_gauss_cov(ells, dell, cls_fid, keys, cl_shot_noise, fsky = 0.363609919):
    """
    Get the Gaussian covariance for a set of Cls. Assumes no correlation between different ells.
    """
    cov_l = np.zeros([len(ells), len(keys), len(keys)])
    invcov_l = np.zeros([len(ells), len(keys), len(keys)])
    for il, l in enumerate_progress(ells):
#         print(l)
#         ncl = len(keys)
#         cov_l = np.zeros([ncl, ncl])

        for (idx1, key1), (idx2, key2) in itertools.combinations_with_replacement(enumerate(keys), 2):
            # print(key1, key2)
            probeA, probeB = key1.split('x')
            probeC, probeD = key2.split('x')

            cov_l[il, idx1, idx2] = 1. / (fsky * (2. * l + 1.) * dell[il]) \
                * (
                    (cls_fid['x'.join([probeA, probeC])][l] + cl_shot_noise['x'.join([probeA, probeC])]) *
                    (cls_fid['x'.join([probeB, probeD])][l] + cl_shot_noise['x'.join([probeB, probeD])]) +
                    (cls_fid['x'.join([probeA, probeD])][l] + cl_shot_noise['x'.join([probeA, probeD])]) *
                    (cls_fid['x'.join([probeB, probeC])][l] + cl_shot_noise['x'.join([probeB, probeC])])
            )

        # Get the symmetric matrix
        cov_l[il] = cov_l[il] + cov_l[il].T - np.diag(cov_l[il].diagonal())
#         cov_tot[il] = cov_l
        invcov_l[il] = np.linalg.inv(cov_l[il])
    return cov_l, invcov_l
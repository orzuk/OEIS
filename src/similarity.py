import numpy as np
from scipy import stats

from collections import Counter
from itertools import combinations

import data

__all__ = ["CommonItems", "XorLeastBits"]

class CommonItems(object):
    C = Counter()

    for name in data.sequences:
        C.update(data.sequences[name])

    TOTAL_ITEMS = np.sum(C.values())
    
    @staticmethod
    def count(s1, s2):
        """Simplest similarity score: number of common elements"""
        return len(set(s1) & set(s2))
    
    @classmethod
    def pval_given_singles(cls, s1, s2):
        """
        A slightly more complicated similarity score:
        how surprising is it to find those common elements, assuming the
        elements of all sequences are drawn from a single distribution 
        """
        common_items = set(s1) & set(s2)
        score = 0.0
        
        for item in common_items:
            score -= np.log2(1.0 * cls.C[item] / cls.TOTAL_ITEMS)
        
        return score
    
    @classmethod
    def find_seq_with_high_score(cls, max_appearances = 3, filter_duplicates = True):
        """
        Find sequences with high similarity score.
        """
        
        rare_values = {v for v in cls.C
                            if cls.C[v] >= 2 and cls.C[v] <= max_appearances}
        
        rare_values_dict = {v: set() for v in rare_values}
        
        for name in data.sequences:
            for value in (set(data.sequences[name]) & rare_values):
                rare_values_dict[value].add(name)
        
        if filter_duplicates:
            D = data.duplicates2
        else:
            D = set()
        
        pairs = set()
        high_scores = []
        
        for value in rare_values_dict:
            for n1, n2 in combinations(rare_values_dict[value], 2):
                if ((n1, n2) not in pairs) and ((n1, n2) not in D):
                    pairs.add((n1, n2))
                    score = cls.pval_given_singles(data.sequences[n2], data.sequences[n1])
                    high_scores.append((n1, n2, score))
        
        return sorted(high_scores, key = lambda a: a[2], reverse = True)

class XorLeastBits(object):
    @staticmethod
    def _xor(s1, s2):
        l = min(len(s1), len(s2))
        return (s1[:l] % 2) ^ (s2[:l] % 2)
    
    @staticmethod
    def _two_sided_binomial_test(k, n, p):
        p1 = -stats.binom.logsf(k - 1, n, p)
        p2 = -stats.binom.logcdf(k, n, p)
        
        return (max(p1, p2) / np.log(2)) - 1
    
    @classmethod
    def probability_of_1(cls, s1, s2):
        """
        Calculate the frequency of 1 in the xor of the lsb of the sequences.
        Note: both high (~1) and low (~0) values are surprising.
        """
        return cls._xor(s1, s2).mean()

    @classmethod
    def pval_asumming_uniform(cls, s1, s2):
        """
        return the pvalue of the distribution of the xor of the lsb.
        (two-sided test using binomial disribution (n, 0.5))
        
        This test ignores the original distributions, so that two sequences
        which are both all-odds or all-even will get high score
        """
        x = cls._xor(s1, s2)
        return cls._two_sided_binomial_test((x == 1).sum(), len(x), 0.5)
        
    @classmethod
    def pval_given_singles(cls, s1, s2):
        """
        return the pvalue of the distribution of the xor of the lsb.
        perform two-sided test using binomial disribution (n, p)), where p is 
        calculated from the original sequences.
        
        This test doesn't take into account the possibilty of two sequences
        with alternating lsb: 0,1,0,1,0,1,...
        """
        
        x = cls._xor(s1, s2)
        l = len(x)
        
        p1 = ((s1[:l] % 2) == 1).mean()
        p2 = ((s2[:l] % 2) == 1).mean()
        
        p = p1 * (1.0 - p2) + (1.0 - p1) * p2
        
        return cls._two_sided_binomial_test((x == 1).sum(), l, p)
    
    @classmethod
    def pval_given_pairs(cls, s1, s2):
        """
        return the pvalue of the distribution of the xor of the lsb.
        perform two-sided test using binomial disribution (n, p)), where p is 
        calculated from the original sequences.
        
        This test *does* take into account the possibilty of two sequences
        with alternating lsb: 0,1,0,1,0,1,...
        """
        x = cls._xor(s1, s2)
        l = len(x)
        l = l - (l % 2)
        x = x[:l]
        
        b1 = s1[:l] % 2
        b2 = s2[:l] % 2
        
        c1 = np.bincount(b1[::2] * 2 + b1[1::2], None, 4) / (l / 2.)
        c2 = np.bincount(b2[::2] * 2 + b2[1::2], None, 4) / (l / 2.)
        
        c1.shape = (2, 2)
        c2.shape = (2, 2)
        
        conv = np.fft.irfftn(np.fft.rfftn(c1) * np.fft.rfftn(c2))
        
        p = (conv[0, 1] + conv[1, 0] + 2 * conv[1, 1]) / 2.
        return cls._two_sided_binomial_test((x == 1).sum(), l, p)
        

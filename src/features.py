import numpy as np
from scipy import stats
from collections import OrderedDict
import os
import gzip

OLSRecord = [
    ('intercept', '<f8'),
    ('slope', '<f8'),
    ('rss', '<f8')
]

OLSRecordType = np.dtype((np.record, OLSRecord))

def OLS(X, Y):
    """perform OLS regression with intercept"""
    n = len(Y)
    X = np.c_[np.ones((n, 1)), np.arange(n)[:, None]]
    
    coefs, rss, rank, s = np.linalg.lstsq(X, Y)
    
    res = np.zeros(1, OLSRecordType)
    res["intercept"] = coefs[0]
    res["slope"] = coefs[1]
    res["rss"] = rss[0]
    
    return res

SimpleRecord = [
    ('mean', '<f8'),
    ('var', '<f8'),
    ('skewness', '<f8'),
    ('kurtosis', '<f8'),
    ('first', '<i8'),
    ('sign', '<f8'),
    ('zeros', '<f8'),
    ('harmonic_mean', '<f8'),
    ('geometric_mean', '<f8'),
    ('val_0mod2', '<f8'),
    ('val_1mod2', '<f8'),
    ('val_0mod3', '<f8'),
    ('val_1mod3', '<f8'),
    ('val_2mod3', '<f8'),
    ('val_0mod5', '<f8'),
    ('val_1mod5', '<f8'),
    ('val_2mod5', '<f8'),
    ('val_3mod5', '<f8'),
    ('val_4mod5', '<f8')
]

SimpleRecordType = np.dtype((np.record, SimpleRecord))

def create_simple_record(sequence):
    features = np.zeros(1, SimpleRecordType)
    
    features["mean"] = sequence.mean()
    features["var"] = sequence.var()
    features["skewness"] = stats.skew(sequence)
    features["kurtosis"] = stats.kurtosis(sequence)
    
    features["first"] = sequence[0]
    features["sign"] = np.sign(sequence).mean()
    features["zeros"] = (sequence == 0).mean()
    
    if (features["zeros"] == 0.0):
        features["harmonic_mean"] = stats.hmean(abs(sequence))
        features["geometric_mean"] = stats.gmean(abs(sequence))
    else:
        features["harmonic_mean"] = np.nan
        features["geometric_mean"] = np.nan
    
    for m in [2, 3, 5]:
        seqm = sequence % m
        for v in range(m):
            features["val_%dmod%d" % (v, m)] = (seqm == v).mean()
    
    return features

Record = [
    ('name', 'S7'),
    ('length', '<i8')
]
Record.extend(SimpleRecord)

for d in [1, 2, 3, 5]:
    for (n, t) in SimpleRecord:
        Record.append(("diff%d_%s" % (d, n), t))

for ols in ["ols", "log_ols", "log_log_ols"]:
    for (n, t) in OLSRecord:
        Record.append((ols + "_" + n, t))

for i in range(0, 101, 10):
    Record.append(('percentile%d' % i, '<i8'))

RecordType = np.dtype((np.record, Record))

def copy_record_with_prefix(dst, src, prefix = ""):
    for name in src.dtype.names:
        dst[prefix + name] = src[name]

def set_floats_to_nan(rec):
    for name, t in rec.dtype.descr:
        if t[1] == "f":
            rec[name] = np.nan

def create_record(name, sequence):
    
    features = np.zeros(1, RecordType)
    set_floats_to_nan(features)
    
    n = len(sequence)
    features["name"] = name
    features["length"] = n
    
    simple = create_simple_record(sequence)
    copy_record_with_prefix(features, simple)
    
    for d in [1, 2, 3, 5]:
        if n > d + 1:
            diff = sequence[d:] - sequence[:-d]            
            simple = create_simple_record(diff)
            copy_record_with_prefix(features, simple, "diff%d_" % d)
    
    if (n > 2):
        ols = OLS(np.arange(1, n + 1), sequence)
        copy_record_with_prefix(features, ols, "ols_")
    
    if (n > 2) and (features["zeros"] == 0):
        log_ols = OLS(np.arange(1, n + 1), np.log(abs(sequence)))
        copy_record_with_prefix(features, log_ols, "log_ols_")
        
        log_log_ols = OLS(np.log(np.arange(1, n + 1)), np.log(abs(sequence)))
        copy_record_with_prefix(features, log_log_ols, "log_log_ols_")
    
    percentiles_index = np.linspace(0, n - 1, 11).round().astype(int)
    percentiles = np.sort(sequence)[percentiles_index]
    for i in range(0, 11):
        features["percentile%d" % (10 * i)] = percentiles[i]
    
    return features

def create_features_file(names, sequences):
    """
    Creates a csv file with the features. It takes approximately
    20 minutes.
    """
    feature_array = np.zeros(len(names), RecordType)
    for i, name in enumerate(names):
       feature_array[i] = create_record(name, sequences[name])
    feature_array = np.rec.array(feature_array)
    gzip.open("data/features.bin.gz", "wb").write(feature_array.tostring())

def read_features_file():
    """reads the features"""
    return np.rec.fromstring(gzip.open(os.path.dirname(__file__) + "/../data/features.bin.gz").read(), dtype = RecordType)

def extract_features(features, choices):
    """ extracts an ndarray of the given features iterable
        features - a record array as constructed by create_features_file
        choices - an iterable containing the titles of the wanted features

        returns a slicing of features containing only the choices by the ORIGINAL order
        """
    return np.asarray([[rec[k] for k in choices] for rec in features])

    return features.choose(choices)
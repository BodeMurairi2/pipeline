#!/usr/bin/env python3
"""Module that creates a pd.DataFrame from a np.ndarray"""
import pandas as pd


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray with columns
    labeled A, B, C, ... in alphabetical order"""
    columns = [chr(ord('A') + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)

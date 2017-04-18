# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:32:23 2017

@author: Colin
"""

from sklearn.base import TransformerMixin, BaseEstimator
class ColSelector(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, df):
        return df[self.key]
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
class DataPipeline:
    def __init__(self, dataframe):
        self.df = dataframe
        self.scaler = StandardScaler()
    def clean_data(self):
        self.df = self.df.drop_duplicates().dropna()
        return self
    def normalize_features(self, columns):
        self.df[columns] = self.scaler.fit_transform(self.df[columns])
        return self
    def get_summary_stats(self):
        return self.df.describe()

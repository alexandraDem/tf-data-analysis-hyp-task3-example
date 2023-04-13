import pandas as pd
import numpy as np


chat_id = 433719125 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y:np.array) -> bool:
  from scipy.stats import ttest_ind
  pvalue = ttest_ind(x,y,equal_var=False).pvalue
  return True if pvalue < 0.03 else False

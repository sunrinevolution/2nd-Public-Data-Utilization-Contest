import tensorflow as tf 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# check tensorflow version
print(tf.__version__)

# 독립변수: 책 카테고리
# 종속변수: 개표 통계

X_data = pd.read_csv("./data/preprocessed_guro.csv") # preprocessed guro book reservation dataset
Y_data = pd.read_excel('./data/vote/지역구/1서울/개표상황(투표구별)_구로구.xlsx')

Y_data.columns
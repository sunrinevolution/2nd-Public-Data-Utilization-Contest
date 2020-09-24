from matplotlib.pyplot import title
from numpy.lib.function_base import sinc
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rc('font', family='D2Coding')

# 구로, 광주, 하남, 이천, 의정부, 양주

print("Matplotlib version", matplotlib.__version__)

gr_vote = pd.read_csv('./data/vote_preprocessed/vote_guro.csv') # 구로 투표 데이터
gj_vote = pd.read_csv('./data/vote_preprocessed/vote_gwangju.csv') # 광주 투표 데이터
hn_vote = pd.read_csv('./data/vote_preprocessed/vote_hanam.csv') # 하남 투표 데이터
ic_vote = pd.read_csv('./data/vote_preprocessed/vote_icheon.csv') # 이천 투표 데이터
ijb_vote = pd.read_csv('./data/vote_preprocessed/vote_uijeongbu.csv') # 의정부 투표 데이터
yj_vote = pd.read_csv('./data/vote_preprocessed/vote_yangju.csv') # 양주 투표 데이터

gr_vote.index = gr_vote['읍면동명']
gj_vote.index = gj_vote['읍면동명']
hn_vote.index = hn_vote['읍면동명']
ic_vote.index = ic_vote['읍면동명']
ijb_vote.index = ijb_vote['읍면동명']
yj_vote.index = yj_vote['읍면동명']

gr_vote = gr_vote.drop(columns=['읍면동명', '투표수', '선거인수'])
gj_vote = gj_vote.drop(columns=['읍면동명', '투표수', '선거인수'])
hn_vote = hn_vote.drop(columns=['읍면동명', '투표수', '선거인수'])
ic_vote = ic_vote.drop(columns=['읍면동명', '투표수', '선거인수'])
ijb_vote = ijb_vote.drop(columns=['읍면동명', '투표수', '선거인수'])
yj_vote = yj_vote.drop(columns=['읍면동명', '투표수', '선거인수'])

fig = plt.figure()

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(24, 12))

gr_explode = [0.03 for i in gr_vote.loc['합계']]
gj_explode = [0.03 for i in gj_vote.loc['합계']]
hn_explode = [0.03 for i in hn_vote.loc['합계']]
ic_explode = [0.03 for i in ic_vote.loc['합계']]
ijb_explode = [0.03 for i in ijb_vote.loc['합계']]
yj_explode = [0.03 for i in yj_vote.loc['합계']]

ax[0, 0].pie(list(gr_vote.loc['합계']), labels=gr_vote.columns, autopct='%1.2f', explode=gr_explode, radius=1.1)
ax[0, 1].pie(list(gj_vote.loc['합계']), labels=gj_vote.columns, autopct='%1.2f', explode=gj_explode, radius=1.1)
ax[0, 2].pie(list(hn_vote.loc['합계']), labels=hn_vote.columns, autopct='%1.2f', explode=hn_explode, radius=1.1)
ax[1, 0].pie(list(ic_vote.loc['합계']), labels=ic_vote.columns, autopct='%1.2f', explode=ic_explode, radius=1.1)
ax[1, 1].pie(list(ijb_vote.loc['합계']), labels=ijb_vote.columns, autopct='%1.2f', explode=ijb_explode, radius=1.1)
ax[1, 2].pie(list(yj_vote.loc['합계']), labels=yj_vote.columns, autopct='%1.2f', explode=yj_explode, radius=1.1)

ax[0, 0].set_title('구로구')
ax[0, 1].set_title('광주시')
ax[0, 2].set_title('하남시')
ax[1, 0].set_title('이천시')
ax[1, 1].set_title('의정부시')
ax[1, 2].set_title('양주시')

plt.show()
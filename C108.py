import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

dice_result=[]
df=pd.read_csv('ssdp.csv')
weight= df['Weight(Pounds)']
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

fig= ff.create_distplot([weight],['result'],show_hist=False)
fig.show()


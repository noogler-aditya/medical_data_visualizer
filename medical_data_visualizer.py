import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = df = pd.read_csv('medical_examination.csv')

# 2

df['overweight'] = (df['weight'] / ((df['height'] / 100)**2)).apply(lambda x: 1 if x > 25 else 0)

# 3

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6
    
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size().rename(columns={'size': 'total'})


    # 7
    

    fig = sns.catplot(x='variable', y='total', hue='cardio', col='value', kind='bar', data=df_cat)
    fig.set_axis_labels("variable", "total") 
    fig = fig.fig
    
    # 8

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))
    ]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(7, 7))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        fmt=".1f",
        vmax=0.3,  
        linewidths=0.5,
        square=True,
        cbar_kws={"shrink": 0.5},
        annot=True,
        center=0,
    )
    # 16
    fig.savefig('heatmap.png')
    return fig

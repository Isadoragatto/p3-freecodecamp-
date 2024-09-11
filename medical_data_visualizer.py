import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('medical_examination.csv')


df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = df['overweight'].apply(lambda x: 1 if x > 25 else 0)


df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

def draw_cat_plot():
    
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index().rename(columns={0: 'total'})

    
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    
    fig.savefig('catplot.png')

    
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    
    corr = df_heat.corr()

    
    mask = np.triu(np.ones_like(corr, dtype=bool))

    
    fig, ax = plt.subplots(figsize=(12, 8))

    
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', vmax=1, vmin=-1, center=0, square=True, linewidths=0.5)

    
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()
import pandas as pd

list = ['ルフィー', 'ゾロ', 'ナミ', 'サンジ', 'ウソップ']

df = pd.DataFrame(list, columns=["name"])

df.to_csv("source.csv")
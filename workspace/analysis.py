import pandas as pd

# 2014年のデータをつかって以下の問題に答えよ
## - - - - - - - - - - - - - - - - - - - - - -
# memorable code
# data = pd.read_csv("weather_2012_2014.csv")
# data['日付'] = pd.to_datetime(data['日付'])
# data = data[data['日付'] >= pd.to_datetime('2014-01-01')]

# noon = data['昼の天気'].value_counts()
# night = data['夜の天気'].value_counts()

# df = DataFrame({'昼の天気':noon, '夜の天気':night})
# df.plot(kind='bar', rot=0, title=u'天気の出現度数グラフ')


## 各都市の「昼の天気」と「夜の天気」について、各要素の出現度数について表にまとめよ
## 各都市の「昼の天気」と「夜の天気」について、各要素の出現割合を割合の積み上げ棒グラフとして書け
data = pd.read_csv("weather_2012_2014.csv")
data['日付'] = pd.to_datetime(data['日付'])
data = data[data['日付'] >= pd.to_datetime('2014-01-01')]
data1_2 = data

noon_data1_2 = data1_2
# CSV データのクロス集計をおこなう
noon_counts = crosstab(noon_data1_2['都市'], noon_data1_2['昼の天気'])
print(noon_counts)
noon_counts.plot(kind='bar', rot=0, title=u'都市ごとの昼の天気の出現度数グラフ')

# データを正規化する
noon_counts = noon_counts.div(noon_counts.sum(1), axis=0)
print(noon_counts)

# 積み上げ棒グラフでプロッティングする
noon_counts.plot(kind='bar', stacked=True, rot=0, title=u'都市ごとの昼の天気の割合積み上げグラフ')


night_data1_2 = data1_2

# CSV データのクロス集計をおこなう
night_counts = crosstab(night_data1_2['都市'], night_data1_2['夜の天気'])
print(night_counts)
night_counts.plot(kind='bar', rot=0, title=u'都市ごとの夜の天気の出現度数グラフ')

# データを正規化する
night_counts = night_counts.div(night_counts.sum(1), axis=0)
print(night_counts)

# 積み上げ棒グラフでプロッティングする
night_counts.plot(kind='bar', stacked=True, rot=0, title=u'都市ごとの夜の天気の割合積み上げグラフ')

## 2 組み合わせ
## - - - - - - - - - - - - - - - - - - - - - -
data['1日の天気'] = data['昼の天気'] + 'のち' + data['夜の天気']
# CSV データのクロス集計をおこなう
day_counts = crosstab(noon_data1_2['都市'], noon_data1_2['1日の天気'])
print(day_counts)

day_counts = day_counts.div(day_counts.sum(1), axis=0)
print(day_counts)

day_counts.plot(kind='bar', stacked=True, rot=0, title=u'都市ごとの天気の移り変わりの割合のグラフ')
# day_counts.plot(kind='pie', autopct='%.2f',figsize=(6,6),startangle=90)

day_counts_sapporo_pie_graph = pd.Series(day_counts.values[0], index=day_counts.columns.tolist(),name='札幌の天気の移り変わりの割合グラフ')
day_counts_sapporo_pie_graph.plot(kind='pie',autopct='%.2f',figsize=(6,6),startangle=90)

day_counts_tokyo_pie_graph = pd.Series(day_counts.values[1], index=day_counts.columns.tolist(),name='東京の天気の移り変わりの割合グラフ')
day_counts_tokyo_pie_graph.plot(kind='pie',autopct='%.2f',figsize=(6,6),startangle=90)

day_counts_fukuoka_pie_graph = pd.Series(day_counts.values[0], index=day_counts.columns.tolist(),name='福岡の天気の移り変わりの割合グラフ')
day_counts_fukuoka_pie_graph.plot(kind='pie',autopct='%.2f',figsize=(6,6),startangle=90)
plt.show()
plt.savefig("image.png")

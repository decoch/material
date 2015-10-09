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


## 下記の設問は、「数値要約」と「分布と傾向の把握」に関するスキルを確認するものである。
# 各都市について、「平均気温」の最小値、25%点、中央値、平均値、75%点、最大値 をそれぞれ求めよ。
data = pd.read_csv("weather_2012_2014.csv")

sapporo_data = data[data['都市'] == '札幌']
sapporo_temperature = sapporo_data['平均気温']
tokyo_data = data[data['都市'] == '東京']
tokyo_temperature = tokyo_data['平均気温']
fukuoka_data = data[data['都市'] == '福岡']
fukuoka_temperature = fukuoka_data['平均気温']

# 福岡
fukuoka_data.min()
print "1Q x:" + str(stats.scoreatpercentile(fukuoka_temperature, 25)) #第1四分位
print "Med x: " + str(numpy.median(fukuoka_temperature)) #中央値
print "3Q x:" + str(stats.scoreatpercentile(fukuoka_temperature, 75)) #第3四分位
fukuoka_data.max()
# 東京
tokyo_data.min()
print "1Q x:" + str(stats.scoreatpercentile(tokyo_temperature, 25)) #第1四分位
print "Med x: " + str(numpy.median(tokyo_temperature)) #中央値
print "3Q x:" + str(stats.scoreatpercentile(tokyo_temperature, 75)) #第3四分位
tokyo_data.max()
# 札幌
sapporo_data.min()
print "1Q x:" + str(stats.scoreatpercentile(sapporo_temperature, 25)) #第1四分位
print "Med x: " + str(numpy.median(sapporo_temperature)) #中央値
print "3Q x:" + str(stats.scoreatpercentile(sapporo_temperature, 75)) #第3四分位
sapporo_data.max()

# 各都市の平均気温の推移を比較すため、横軸を日付、縦軸を平均気温としてわかりや すくグラフ化せよ

df['日付'] = fukuoka_data['日付']
temperature_all = pd.DataFrame(
    {'日付': fukuoka_data['日付'],
    '福岡の平均気温':fukuoka_data['平均気温']
    }
)
tokyo_temperature.index = fukuoka_temperature.index
temperature_all['東京の平均気温'] = tokyo_temperature

sapporo_temperature.index = fukuoka_temperature.index
temperature_all['東京の平均気温'] = sapporo_temperature
temperature_all.plot()

temperature_all_box = []
temperature_all_box.append(temperature_all['福岡の平均気温'])
temperature_all_box.append(temperature_all['東京の平均気温'])
temperature_all_box.append(temperature_all['札幌の平均気温'])

data = []
data.append(temperature_all['福岡の平均気温'])
data.append(temperature_all['東京の平均気温'])
data.append(temperature_all['札幌の平均気温'])

fig = plt.figure()
ax = fig.add_subplot(111)

ax.grid() # グリッド線書いてるだけ
bp = ax.boxplot(data) # 箱ひげ図を書く
ax.set_ylim([-20, 40]) # y軸の範囲指定
ax.set_xticklabels(['Fukuoka','Tokyo', 'Sapporo']) # xlabelの設定
plt.title('Average Temperature')
plt.show()

plt.title('Violin Plot of Average Temperature')
plt.xlabel("都市")
plt.ylabel("温度")
violinplot(data, points=20,showmeans=True, showextrema=True, showmedians=True)





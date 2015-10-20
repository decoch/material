## install package (require only first)
##============================================
install.packages("MuMIn")
install.packages("ggplot2")
install.packages("dplyr")

## workspace setting
##============================================
library(MuMIn)
library(ggplot2)
library(dplyr)
first_data <- read.csv("../data/first_data.csv", encoding = "UTF-8", header = TRUE, stringsAsFactors = TRUE)

# Fukuoka Histgram
fukuoka_average_temperature <- first_data %>%
  select(city, average_temperature) %>%
  filter(city == "Fukuoka")
hist(fukuoka_average_temperature$average_temperature, main="fukuoka_average_temperature", xlab="temperature", col="red") # draw histgram
# sanction
# 結果の 'W' は本検定の検定統計量、'p-value'はp値を示す
# 有意水準が5%の評価などを行える
shapiro.test(fukuoka_average_temperature$average_temperature)

# Tokyo Histgram
tokyo_average_temperature <- first_data %>%
  select(city, average_temperature) %>%
  filter(city == "Tokyo")

hist(tokyo_average_temperature$average_temperature, main="tokyo_average_temperature", xlab="temperature", col="blue") # draw histgram
shapiro.test(fukuoka_average_temperature$average_temperature) # sanction

# T-test
# t.test(fukuoka_average_temperature$average_temperature,tokyo_average_temperature$average_temperature,var.equal=T)

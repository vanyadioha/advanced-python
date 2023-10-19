import pandas as pd

# Intro to pandas
# wd = pd.read_csv("./datasets/weather.csv")
# tl = wd["temp"].to_list()

# avg = sum(tl) / len(tl)
# pd_avg = wd.temp.mean()
# pd_max = wd.temp.max()

# max_temp_day = wd[wd.temp == pd_max]
# print(max_temp_day.conditions)

# Squirrel census
sd = pd.read_csv("./datasets/squirrel_census_2018.csv")
gray_sq = len(sd[sd["Primary Fur Color"] == "Gray"])
cinnamon_sq = len(sd[sd["Primary Fur Color"] == "Cinnamon"])
black_sq = len(sd[sd["Primary Fur Color"] == "Black"])


new_data = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Number": [black_sq, cinnamon_sq, gray_sq],
}

new_pd = pd.DataFrame(new_data)
new_pd.to_csv("./datasets/fur_color_count.csv")

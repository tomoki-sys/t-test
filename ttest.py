import scipy.stats as stats

# データ（例として、20個のサンプルデータを設定）
sample_data =[203., 197., 199., 206., 204., 190., 199., 194., 194., 197., 195.,202., 198., 195., 197., 196., 202., 193., 196., 190.]

# 帰無仮説: マヨネーズの内容量は200gより少ない
null_hypothesis_value = 200

# t検定を実行
t_stat, p_value = stats.ttest_1samp(sample_data, null_hypothesis_value)

# 結果を出力
print("t統計量:", t_stat)
print("p値:", p_value)

# p値を用いて帰無仮説の検定を行う
alpha = 0.05  # 有意水準を設定（通常は0.05）
if p_value < alpha:
    print("帰無仮説を棄却します。マヨネーズの内容量は200gより少なくなっている可能性があります。")
else:
    print("帰無仮説を採択します。マヨネーズの内容量は200gより少なくなっていないと言えます。")
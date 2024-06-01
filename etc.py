btc_price = price_df['BTC']
xrp_price = price_df['XRP']
sol_price = price_df['SOL']
doge_price = price_df['DOGE']
etc_price = price_df['ETC']
eth_price = price_df['ETH']

# 15분
btc_15m_price = btc_price.resample('15T').agg({'BTC':'last'})
xrp_15m_price = xrp_price.resample('15T').agg({'XRP':'last'})
sol_15m_price = sol_price.resample('15T').agg({'SOL':'last'})
doge_15m_price = doge_price.resample('15T').agg({'DOGE':'last'})
etc_15m_price = etc_price.resample('15T').agg({'ETC':'last'})
eth_15m_price = eth_price.resample('15T').agg({'ETH':'last'})
all_15m_list = [btc_15m_price, xrp_15m_price, sol_15m_price, doge_15m_price, etc_15m_price, eth_15m_price]

# 1시간
btc_1h_price = btc_price.resample('1H').agg({'BTC':'last'})
xrp_1h_price = xrp_price.resample('1H').agg({'XRP':'last'})
sol_1h_price = sol_price.resample('1H').agg({'SOL':'last'})
doge_1h_price = doge_price.resample('1H').agg({'DOGE':'last'})
etc_1h_price = etc_price.resample('1H').agg({'ETC':'last'})
eth_1h_price = eth_price.resample('1H').agg({'ETH':'last'})
all_1h_list = [btc_1h_price, xrp_1h_price, sol_1h_price, doge_1h_price, etc_1h_price, eth_1h_price]

# 4시간
btc_4h_price = btc_price.resample('4H').agg({'BTC':'last'})
xrp_4h_price = xrp_price.resample('4H').agg({'XRP':'last'})
sol_4h_price = sol_price.resample('4H').agg({'SOL':'last'})
doge_4h_price = doge_price.resample('4H').agg({'DOGE':'last'})
etc_4h_price = etc_price.resample('4H').agg({'ETC':'last'})
eth_4h_price = eth_price.resample('4H').agg({'ETH':'last'})
all_4h_list = [btc_4h_price, xrp_4h_price, sol_4h_price, doge_4h_price, etc_4h_price, eth_4h_price]

# 6시간
btc_6h_price = btc_price.resample('6H').agg({'BTC':'last'})
xrp_6h_price = xrp_price.resample('6H').agg({'XRP':'last'})
sol_6h_price = sol_price.resample('6H').agg({'SOL':'last'})
doge_6h_price = doge_price.resample('6H').agg({'DOGE':'last'})
etc_6h_price = etc_price.resample('6H').agg({'ETC':'last'})
eth_6h_price = eth_price.resample('6H').agg({'ETH':'last'})
all_6h_list = [btc_6h_price, xrp_6h_price, sol_6h_price, doge_6h_price, etc_6h_price, eth_6h_price]

# 8시간
btc_8h_price = btc_price.resample('8H').agg({'BTC':'last'})
xrp_8h_price = xrp_price.resample('8H').agg({'XRP':'last'})
sol_8h_price = sol_price.resample('8H').agg({'SOL':'last'})
doge_8h_price = doge_price.resample('8H').agg({'DOGE':'last'})
etc_8h_price = etc_price.resample('8H').agg({'ETC':'last'})
eth_8h_price = eth_price.resample('8H').agg({'ETH':'last'})
all_8h_list = [btc_8h_price, xrp_8h_price, sol_8h_price, doge_8h_price, etc_8h_price, eth_8h_price]

# 12시간
btc_12h_price = btc_price.resample('12H').agg({'BTC':'last'})
xrp_12h_price = xrp_price.resample('12H').agg({'XRP':'last'})
sol_12h_price = sol_price.resample('12H').agg({'SOL':'last'})
doge_12h_price = doge_price.resample('12H').agg({'DOGE':'last'})
etc_12h_price = etc_price.resample('12H').agg({'ETC':'last'})
eth_12h_price = eth_price.resample('12H').agg({'ETH':'last'})
all_12h_list = [btc_12h_price, xrp_12h_price, sol_12h_price, doge_12h_price, etc_12h_price, eth_12h_price]

# 일봉
btc_1d_price = btc_price.resample('1D').agg({'BTC':'last'})
xrp_1d_price = xrp_price.resample('1D').agg({'XRP':'last'})
sol_1d_price = sol_price.resample('1D').agg({'SOL':'last'})
doge_1d_price = doge_price.resample('1D').agg({'DOGE':'last'})
etc_1d_price = etc_price.resample('1D').agg({'ETC':'last'})
eth_1d_price = eth_price.resample('1D').agg({'ETH':'last'})
all_1d_list = [btc_1d_price, xrp_1d_price, sol_1d_price, doge_1d_price, etc_1d_price, eth_1d_price]

# 주봉
btc_1w_price = btc_price.resample('1W').agg({'BTC':'last'})
xrp_1w_price = xrp_price.resample('1W').agg({'XRP':'last'})
sol_1w_price = sol_price.resample('1W').agg({'SOL':'last'})
doge_1w_price = doge_price.resample('1W').agg({'DOGE':'last'})
etc_1w_price = etc_price.resample('1W').agg({'ETC':'last'})
eth_1w_price = eth_price.resample('1W').agg({'ETH':'last'})
all_1w_list = [btc_1w_price, xrp_1w_price, sol_1w_price, doge_1w_price, etc_1w_price, eth_1w_price]

plt.figure(figsize=(20, 15));

plt.subplot(6,2,1)
sns.histplot(btc_1h_price.pct_change(),kde=True, bins=30);
plt.title('1-hour btc return histogram')
plt.subplot(6,2,2)
plt.plot(btc_1h_price.pct_change());
plt.title('1-hour btc return graph')

plt.subplot(6,2,3)
sns.histplot(btc_4h_price.pct_change(),kde=True, bins=30);
plt.title('4-hour btc return histogram')
plt.subplot(6,2,4)
plt.plot(btc_4h_price.pct_change());
plt.title('4-hour btc return graph')

plt.subplot(6,2,5)
sns.histplot(btc_6h_price.pct_change(),kde=True, bins=30);
plt.title('6-hour btc return histogram')
plt.subplot(6,2,6)
plt.plot(btc_6h_price.pct_change());
plt.title('6-hour btc return graph')

plt.subplot(6,2,7)
sns.histplot(btc_12h_price.pct_change(),kde=True, bins=30);
plt.title('12-hour btc return histogram')
plt.subplot(6,2,8)
plt.plot(btc_12h_price.pct_change());
plt.title('12-hour btc return graph')

plt.subplot(6,2,9)
sns.histplot(btc_1d_price.pct_change(),kde=True, bins=30);
plt.title('1-day btc return histogram')
plt.subplot(6,2,10)
plt.plot(btc_1d_price.pct_change());
plt.title('1-day btc return graph')

plt.subplot(6,2,11)
sns.histplot(btc_1w_price.pct_change(),kde=True, bins=30);
plt.title('1-week btc return histogram')
plt.subplot(6,2,12)
plt.plot(btc_1w_price.pct_change());
plt.title('1-week btc return graph')

plt.tight_layout();

# Top 10 Correlation 구하는 코드
# top10_corr = corr_df.nlargest(10, 'corr').reset_index(drop=True)['corr']
# top10_corr.name = f'#{cnt}'
# cnt += 1
# correlation_df = pd.concat([correlation_df, top10_corr], axis=1)

# plt.figure(figsize=(20,10))
# plt.title('Top 10 Correlation')
# for i in range(10):
#     plt.plot(correlation_df.iloc[i], label=f'{i+1}');
#     plt.xticks(rotation=90)
# plt.grid(True);
# plt.ylabel('correlation');
# plt.xlabel('Rolling #');
# plt.legend();

import tushare as ts
import sys

df = ts.get_today_all()
path = sys.argv[1]
df.to_csv(path, encoding="utf8")
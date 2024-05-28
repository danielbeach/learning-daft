import daft
from daft import col
from datetime import datetime

t1 = datetime.now()
df = daft.read_csv("s3://confessions-of-a-data-guy/*.csv")
print(df.count().collect())

df = df.with_column("year", df["started_at"].dt.year())
df = df.with_column("month", df["started_at"].dt.month())
df = df.with_column("day", df["started_at"].dt.day())
df = df.groupby(["year", "month", "day", "member_casual"]).agg(col("member_casual").count().alias("count"))
df = df.sort(by=["year", "month", "day"])
print(df.collect())
t2 = datetime.now()
# print how long it took
print(t2 - t1)

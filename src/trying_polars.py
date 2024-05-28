import polars as pl
import pyarrow.dataset as ds
from datetime import datetime

t1 = datetime.now()
dset = ds.dataset("s3://confessions-of-a-data-guy/", format="csv")
lf = pl.scan_pyarrow_dataset(dset)

lf = lf.with_columns((pl.col("started_at").dt.year()).alias("year"))
lf = lf.with_columns((pl.col("started_at").dt.month()).alias("month"))
lf = lf.with_columns((pl.col("started_at").dt.day().alias("day")))

lf = lf.groupby(["year", "month", "day", "member_casual"]).agg(pl.col("member_casual").count().alias("count"))
lf = lf.sort(by=["year", "month", "day"])
print(lf.collect())
t2 = datetime.now()
# print how long it took
print(t2 - t1)


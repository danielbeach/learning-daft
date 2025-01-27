# learning-daft
Trying out Daft for Dataframes


Comparing Daft to Polars and other such things.

#### Build Docker
```
docker build \
  --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  --build-arg DATABRICKS_TOKEN=$DATABRICKS_TOKEN \
  --platform linux/amd64 \
  -t daftdelta .
```


from extract import extract
from transform import transform
from load import load
from pyspark.sql import SparkSession
 
spark = SparkSession.builder \
        .appName("ETLPipeline") \
        .config("spark.jars", "postgresql-42.7.4.jar") \
        .getOrCreate()
 
sql = "select * from orders"
df = extract(spark=spark, sql=sql)
orders_df, rfm_df = transform(df)
 
load(df=orders_df, table_name="orders")
load(df=rfm_df, table_name="rfm")
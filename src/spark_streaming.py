from time import sleep

from pyspark.sql import SparkSession
# Creating spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.csv("/home/atif/PycharmProjects/test/src/cereal.csv")
print(df.show())

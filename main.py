from pyspark.shell import spark
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType

schema = StructType(fields=[
    StructField("type", StringType()),
    StructField("name", StringType()),
    StructField("associations", StringType()),
])

df = spark.read.csv("data.csv", schema=schema, sep=",")
df.show()

res = df.filter(col('type') == 'product')
res.show()  # не совсем понятен вид исходного датафрейма

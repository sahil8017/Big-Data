# pyspark_matrix.py

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("MatrixMultiplication") \
    .getOrCreate()

sc = spark.sparkContext

# Matrix A
A = [
    (0, 0, 1),
    (0, 1, 2),
    (1, 0, 3),
    (1, 1, 4)
]

# Matrix B
B = [
    (0, 0, 5),
    (0, 1, 6),
    (1, 0, 7),
    (1, 1, 8)
]

# Create RDDs
rddA = sc.parallelize(A)
rddB = sc.parallelize(B)

# Map Step
mapped = rddA.cartesian(rddB) \
    .filter(lambda x: x[0][1] == x[1][0]) \
    .map(lambda x: (
        (x[0][0], x[1][1]),
        x[0][2] * x[1][2]
    ))

print("Mapped Values:")
print(mapped.collect())

# Reduce Step
result = mapped.reduceByKey(lambda a, b: a + b)

print("\nResult Matrix:")
for item in result.collect():
    print(item)

# Stop Spark
spark.stop()
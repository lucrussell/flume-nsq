from pyspark import SparkContext

sc = SparkContext()
text_file = sc.textFile("hdfs://127.0.0.1:8020/tmp/FlumeData.1534869925312")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print(counts.take(50))

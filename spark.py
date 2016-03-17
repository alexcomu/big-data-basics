# Simple example of a dummy usage
# usage: spark-submit spark.py
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WorkCount")
sc = SparkContext(conf=conf)

input = sc.textFile("PATH-TO-FILE") # src input
words = input.flatMap(lambda x: x.split()) # return list of words
wordCounts = words.countByValue() # spark function, counts each unique istance

for word, count in wordCounts.items():
	cleanWord = word.encode('ascii', 'ignore')
	if cleanWord:
		print cleanWord, count

# big-data-basics

Welcome to my introduction on Big Data Basics - **MapReduce / Hadoop**

Collection of theory and examples with Python.
Requirements: 

	- Python 2.7+
	- MRJob

# MapReduce / Hadoop introduction

**MapReduce**: Programming model for processing large datasets -> horizontal scaling over clusters of computers (invented by Google):

     - MAPPER :     Extract and organize information to unique keys
     - REDUCER:     Process all of the values for each key

**Hadoop**: Software than manages applications that run on a cluster:

     - Shared Files (HDFS)
     - Communication between computers (YARN)
     - Fault-tolerance -> duplicate data on multiple machines (manage backups and fails)


Example of concept:

Movie data set from https://movielans.org
From a raw dataset, **how many movies did each user seen?**

If we have a dataset like this:

| USERID | MOVIEID | Rating | Timestamp |
| -----  | ------- | ------ | --------- |
|   1    |  123    |   2    |     X     |
|   2    |  123    |   2    |     X     |
|   1    |  456    |   2    |     X     |
|   1    |  789    |   2    |     X     |
|   2    |  456    |   2    |     X     |

What can we do?

**Mapper**: Extract and organize what we care about -> Extract for each user (Key) the film seen (Value):

	[Key1: Value | Key2: Value | ...]
	[ 1: 123 | 2: 123 | 1: 456 | 1: 789 | 2: 789]

**Reducer**: Aggregate by key and do something, for example len(movies):

	[Key1: Value1, Value2 | Key2: value1 | ….]
	[1: 123, 456 , 789 | 2: 123, 789]

	len(movies) -> [1: 3 | 2: 2]


**How Hadoop Scales?**

Actors:

	- Data Source (For example Amazon s3)
	- Several PC used as mapper
	- Several PC used as reducer
	- Unique result

We can have different numbers of mapper and reducer, each mapper receives multiple line of data and then will send the result to a specific reducer that will handle the specific key.

# Hadoop Solutions

**Apache’s Hive**

Data warehouse built on Hadoop, **SQL-like queries**, allow MapReduce, can work with Amazon EMR, initially developed by Facebook.


**Apache's Pig**

Alternative for high level scripting. Runs on top of Hadoop, allows SQL-like queries (Pig Latin). Works with Amazon EMR, involves learning another language, initially developed by Yahoo.

**Apache's Spark**

An alternative to MapReduce, is becoming very popular. It uses Hadoop and is used by Twitter, Amazon, ...
Includes **built-in libraries** for machine learning (MLLib), SQL, Streaming and Graph Analysis.

Significantly faster than MapReduce:

“Run programs up to 100x faster than Hadoop MapReduce in memory, or 10x faster on disk.” - YMMV

Can be used with Scala / Java / Python / R, offers SQL queries. Works with HDFS, Cassandra, S3, Hbase, MongoDB and can Work with Elastic MapReduce.

     “Is what the cool kids are using!"



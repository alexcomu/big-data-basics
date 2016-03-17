# big-data-basics

Welcome to my introduction on Big Data Basics - **MapReduce / Hadoop**

Collection of theory and examples with Python.
Requirements: 

	- Python 2.7+
	- MRJob

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

If we have a list like this:

| USERID | MOVIEID | Rating | Timestamp |
| -----  | ------- | ------ | --------- |
|   1    |  123    |   2    |     X     |
|   2    |  123    |   2    |     X     |
|   1    |  456    |   2    |     X     |
|   1    |  789    |   2    |     X     |
|   2    |  456    |   2    |     X     |

What can we do?
Mapper: Extract and organize what we care about -> Extract for each user (Key) the film seen (Value):

	[Key1: Value | Key2: Value | ...]
	[ 1: 123 | 2: 123 | 1: 456 | 1: 789 | 2: 789]

Reducer: Aggregate by key and do something, for example len(movies):

	[Key1: Value1, Value2 | Key2: value1 | ….]
	[1: 123, 456 , 789 | 2: 123, 789]

	len(movies) -> [1: 3 | 2: 2]


from mrjob.job import MRJob

# example fot movielans.org database
# data structure:
# USERID | MOVIEID | Rating | Timestamp

class MoviesByUserCounter(MRJob):
	def mapper(self, key, line):
		(userID, movieID, rating, timestamp) = line.split('\t')
		yield userID, movieID

	def reducer(self, user, movies):
		numMovies = 0
		for movie in movies:
			numMovies = numMovies +1

		yield user, numMovies

if __name__ == '__main__':
	MoviesByUserCounter.run()

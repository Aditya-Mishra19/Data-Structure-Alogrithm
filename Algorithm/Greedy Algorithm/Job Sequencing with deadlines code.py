# data structure to store jobs info. Each job has an identifier,
# a deadline and profit associated with it
class Job:
	def __init__(self, taskID, deadline, profit):

		self.taskID = taskID
		self.deadline = deadline
		self.profit = profit


# schedule jobs to maximize profit
def scheduleJobs(jobs, T):

	# stores maximum profit that can be earned by scheduling jobs
	profit = 0

	# list to store used and unused slots info
	slot = [-1] * T

	# consider each job in decreasing order of their profits
	for job in jobs:
		# search for next free slot and dict the task to that slot
		for j in reversed(range(job.deadline)):
			if j < T and slot[j] == -1:
				slot[j] = job.taskID
				profit += job.profit
				break

	# print the scheduled jobs
	print("The Scheduled jobs are:", list(filter(lambda x: x != -1, slot)))

	# return total profit that can be earned
	return profit


if __name__ == '__main__':

	# List of given jobs. Each job has an identifier, a deadline and
	# profit associated with it
	jobs = [
		Job(1, 9, 15), Job(2, 2, 2),
		Job(3, 5, 18), Job(4, 7, 1),
		Job(5, 4, 25), Job(6, 2, 20),
		Job(7, 5, 8), Job(8, 7, 10),
		Job(9, 4, 12), Job(10, 3, 5)
	]

	# stores maximum deadline that can be associated with a job
	T = 15

	# arrange the jobs in decreasing order of their profits
	jobs.sort(key=lambda x: x.profit, reverse=True)

	# schedule jobs and calculate maximum profit
	print("Total Profit is:", scheduleJobs(jobs, T))

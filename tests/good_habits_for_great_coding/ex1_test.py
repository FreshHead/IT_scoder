from good_habits_for_great_coding import ex1
from tests import run_time_counter

# run_time_counter.print_single_run(ex1.exercise)

# run_time_counter.run_times(ex1.exercise, 10)

print("average time for default is: " + str(run_time_counter.getAverage(ex1.exercise, 10)))
print("average time for improved is: " + str(run_time_counter.getAverage(ex1.solution, 10)))

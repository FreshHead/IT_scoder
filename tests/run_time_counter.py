from time import clock


def print_single_run(func):
    start_time = clock()
    func()
    print('\n+===<RUN TIME>===+')
    print('|  %5f.2' % (clock() - start_time), 'seconds |')
    print('+==================+')


def getAverage(func, times=100):
    time_list = run_times(func, times)
    return sum(time_list) / times


def run_times(func, times):
    results = []
    for i in range(1, times):
        start_time = clock()
        func()
        results.append(clock() - start_time)
    return results

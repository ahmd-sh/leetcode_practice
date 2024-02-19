"""
When multiple tasks are executed on a single-threaded CPU, the tasks are scheduled based on the principle of pre-emption. When a higher-priority task arrives in the execution queue, then the lower-priority task is pre-empted, i.e. its execution is paused until the higher-priority task is complete.
There are n functions to be executed on a single-threaded CPU, with each function having a unique ID between 0 and n-1. Given an integer n, representing the number of functions to be executed, and an execution log as an array of strings, logs, of size m, determine the exclusive times of each of the functions. Exclusive time is the sum of execution times for all calls to a function. Any string representing an execution log is of the form (function_id}:{"start"|"end"): (timestamp), indicating that the function with ID = function_id, either starts or ends at a time identified by the timestamp value.
Note: While calculating the execution time of a function call, both the starting and ending times of the function call have to be included. The log of the form (function_id): (start): (timestamp) means that the running function is preempted at the beginning of timestamp second. The log of the form (function_id):(end): (timestamp) means that the function function_id is preempted after completing its execution at timestamp second i.e after timestamp second.
Example
Suppose n = 3, logs = ["0:start:0", "2:start:4", "2:end:5", "1:start:7", "1:end:10", "0:end:11"]

The total number of seconds allocated to functions 0, 1, and 2 are 6, 4, and 2 respectively. Hence the answer is [6, 4, 2].

getTotalExecution Time has the following parameters:
int n: the number of functions to be executed
string logs[m]: the execution logs of the different calls to the functions
Returns
int[n]: the execution time of all functions with IDs from 0 to n - 1.
Constraints
• 1 <= n <= 100
• 1 <= m <= 500
• O <= function_id < n
• 0 <= timestamp <= 3 * 10^3
• The timestamps are given in non-decreasing order.
• No two starting timestamps and no two ending timestamps are equal.
• Every function "start" call has a corresponding function "end" call.
"""

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'getTotalExecutionTime' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY logs
#
from collections import defaultdict


def getTotalExecutionTime(n, logs):
    hm = defaultdict(int)
    func_processing_stack = []
    prev_time = 0

    for log in logs:
        func_id, state, time = log.split(":")
        func_id, time = int(func_id), int(time)

        if state == "start":
            if func_processing_stack:
                hm[func_processing_stack[-1]] += time - prev_time
            func_processing_stack.append(func_id)
            prev_time = time

        else:
            hm[func_processing_stack.pop()] += time - prev_time + 1
            prev_time = time + 1

    return [hm[i] for i in range(n)]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = getTotalExecutionTime(n, logs)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()

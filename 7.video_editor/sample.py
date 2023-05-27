import time

# get the start time
st = time.time()
st_pr = time.process_time()

for i in range(10**5):
    print(f"{i*10}\n")


# get the end time
et_pr = time.process_time()
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

res = et_pr - st_pr
print('CPU Execution time:', res, 'seconds')


import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = range(5, 0, -1)
    futures = [executor.submit(do_something, sec) for sec in secs]
    #[print(future.result()) for future in futures]

    for f in concurrent.futures.as_completed(futures):
        print(f.result())







# threads = [threading.Thread(target=do_something, args=[1.5]) for _ in range(10)]
# [thread.start() for thread in threads]
# [thread.join() for thread in threads]

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
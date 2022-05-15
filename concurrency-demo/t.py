import threading
import multiprocessing
import requests
from typing import Callable
import time


def timeit(func: Callable[[], None]) -> Callable[[], None]:
	def wrapper(*args, **kwargs):
		start = time.time()
		func()
		print(f'total: {time.time() - start}')
	return wrapper


def make_list():
	print('running make_list')
	x = list(range(100_000_000))
	print('done')
	return x

def get_page(url: str):
	print('requesting: ' + url)
	res = requests.get(url)
	print('got result for ' + url)
	return res


@timeit
def test_threading():
	t1 = threading.Thread(target=get_page, args=(r'https://yahoo.com',))
	t2 = threading.Thread(target=get_page, args=(r'https://pypi.org',))

	# This actually gets executed somewhat sequentially as 
	# CPython's GIL prevents the thread switching.
	# t1 = threading.Thread(target=make_list)
	# t2 = threading.Thread(target=make_list)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

@timeit
def test_multiprocessing():
	# Each process is its own python instance, those do not depend 
	# on each other, and get executed separatly
	p1 = multiprocessing.Process(target=make_list)
	p2 = multiprocessing.Process(target=make_list)
	
	p1.start()
	p2.start()

	p1.join()
	p2.join()

if __name__ == '__main__':
	test_threading()
	test_multiprocessing()
	print('Done')
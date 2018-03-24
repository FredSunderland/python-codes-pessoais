#coding: utf-8
import _thread, time

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n -2)

def test_fib(n):
    print("Fib de %d: %d" %  (n, fib(n)) )

def run_fibs_com_threads():
    _thread.start_new_thread(test_fib, (35,))
    _thread.start_new_thread(test_fib, (30,))
    _thread.start_new_thread(test_fib, (10,))
    time.sleep(10)

run_fibs_com_threads()

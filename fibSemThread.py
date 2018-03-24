#coding: utf-8
import _thread

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n -2)

def test_fib(n):
    print("Fib de %d: %d" %  (n, fib(n)) )

def run_fibs():
    test_fib(35)
    test_fib(30)
    test_fib(10)

run_fibs()

import time
from functools import wraps

#used for one-shot test
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
           (function.func_name, str(t1-t0))
        )
        #return result, float(t1-t0)
        return result
        
    return function_timer

#used for loop time test
def time_logging(times = 1):
    
    def func_timer(function):
        @wraps(function)
        def function_timer(*args, **kwargs):
            print('processing......')
            t0 = time.time()
            for _ in range(times):
                result = function(*args, **kwargs)
            t1 = time.time()
            print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1-t0))
            )
            print ("Average time running %s: %s seconds" %
                           (function.func_name, str((t1-t0) / times))
                       )            
            #return result, float(t1-t0)
            return result 
            
        return function_timer
    
    return func_timer

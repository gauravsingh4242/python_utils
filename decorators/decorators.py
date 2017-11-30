import time


def retry_decorator(retry_count, timeout):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            if retry_count <= 0:
                raise IOError("retry_count should be greater than 0")
            for _ in range(retry_count):
                response = original_function(*args, **kwargs)
                if response.status_code/100 == 2:
                    break
                else:
                    print response.status_code
                    time.sleep(timeout)
            return response
        return wrapper_function
    return decorator_function


def timer(original_function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} took {} sec for execution'.format(original_function.__name__, t2))
        return result
    return wrapper

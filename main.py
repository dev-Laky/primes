from math import sqrt
import time

def timeit(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = (end_time - start_time)*10**3
        return result, f"{total_time} ms"
    return timeit_wrapper

class Primes:
    def __init__(self, r: int):
        self.r = r # range of calc primes
        self.nums = []
        self.no_primes = []
        self.primes = []

        # start engine
        self.gen_nums()
        self.fill_no_primes()
        self.del_primes()

    def gen_nums(self):
        self.nums = list(range(2, self.r+1))
        # for i in range(2, self.r+1):
        #     self.nums.append(i)
    
    def get_nums(self):
        return self.nums

    def get_no_primes(self):
        return self.no_primes

    def get_primes(self):
        return self.primes  

    def fill_no_primes(self):
        for num in self.nums:
            if num >= sqrt(self.r):
                continue
            if num in self.no_primes:
                continue
            for num_comp in self.nums:
                if not num < num_comp:
                    continue
                if num_comp in self.no_primes:
                    continue
                if num_comp % num == 0:
                    self.no_primes.append(num_comp)


    def del_primes(self):
        self.primes = sorted(list((set(self.nums) - set(self.no_primes))))

        # for num in self.nums:
        #     if not num in self.no_primes:
        #         self.primes.append(num)
        

if __name__ == "__main__":
    @timeit
    def run():
        return Primes(1000).get_primes()
    print(run())


# def timeit():
#     def wrapperFunction():
        
    
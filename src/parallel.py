import math
import multiprocessing as mp
from scraper import getCount, crawl

if __name__ == '__main__':
    pages = math.ceil(int(getCount())/20)
    pool = mp.Pool(processes=4)
    results = [pool.apply_async(crawl, args=(x,)) for x in range(1,pages+1)]
    output = [p.get() for p in results]
    print(output)
        

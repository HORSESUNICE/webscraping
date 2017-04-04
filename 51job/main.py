from multiprocessing import Pool
from datafunction import urls
from datafunction import get_url

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_url,urls)
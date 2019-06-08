import stream_twitter
import mongo_to_sql
import credentials_var as cred

import multiprocessing, time, timeout_decorator

if __name__ == '__main__':
    # keyword = ["tokopedia", "tokopediacare"]
    # limit = 100
    # stream_twitter.stream(keyword, limit)

    # keyword = ["bukalapak"]
    # limit = 100
    # stream_twitter.stream(keyword, limit)

    # t = time.time()
    #
    # limit = 50
    # time_limit = 5
    #
    # keyword1 = ["tokopedia", "tokopediacare"]
    # p1 = multiprocessing.Process(target=stream_twitter.stream, args=(keyword1, limit))
    #
    # keyword2 = ["bukalapak", "bukabantuan"]
    # p2 = multiprocessing.Process(target=stream_twitter.stream, args=(keyword2, limit))
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()
    #
    # print("Took", time.time() - t)

    # mongo_to_sql.mongo_to_sql(cred.find_unprocessed)
    mongo_to_sql.mongo_to_sql(cred.find_all)

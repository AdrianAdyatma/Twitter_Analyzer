import credentials_var as cred
import time


def reset():
    cred.sqlCursor.execute(
        'SELECT tweet_id, keyword, weight, text FROM tb_tweet WHERE NOT validation = 0')

    for item in cred.sqlCursor.fetchall():
        sql = 'UPDATE tb_tweet SET validation =' \
              '(%s) WHERE tweet_id = (%s)'
        val = (0, item[0])
        cred.sqlCursor.execute(sql, val)
        cred.sqlDb.commit()


def give_val():
    cred.sqlCursor.execute(
        'SELECT tweet_id, keyword, weight, text FROM tb_tweet '
        'WHERE validation = 0 AND keyword = "Joko Widodo" AND NOT user_location = "" AND NOT weight = 0')

    for item in cred.sqlCursor.fetchall():
        print("\n========= id:", item[0])
        print("==== keyword:", item[1])
        print("====== bobot:", item[2])
        print("\n", item[3])

        valid = input("\nMasukkan nilai : ")
        print("Hasil :", valid)

        sql = 'UPDATE tb_tweet SET validation =' \
              '(%s) WHERE tweet_id = (%s)'
        val = (valid, item[0])
        cred.sqlCursor.execute(sql, val)
        cred.sqlDb.commit()

        time.sleep(1)


if __name__ == '__main__':
    # reset()
    give_val()
    pass

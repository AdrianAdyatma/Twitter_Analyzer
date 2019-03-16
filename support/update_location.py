import credentials_var as cred


def update_location(coll):
    count = 1

    for element in list(coll):

        user_id = int(element['user']['id_str'])
        user_location = element['user']['location']

        try:
            sql = 'UPDATE tb_user SET user_location =' \
                  '(%s) WHERE user_id = (%s)'
            val = (user_location, user_id)
            cred.sqlCursor.execute(sql, val)
            cred.sqlDb.commit()
        except:
            print(user_id, "export user to sql error")
        else:
            count += 1

        try:
            sql = 'UPDATE tb_tweet SET user_location =' \
                  '(%s) WHERE user_id = (%s)'
            val = (user_location, user_id)
            cred.sqlCursor.execute(sql, val)
            cred.sqlDb.commit()
        except:
            print(user_id, "export user to sql error")
        else:
            count += 1

    # Count data processed
    print(count)


update_location(cred.find_all)

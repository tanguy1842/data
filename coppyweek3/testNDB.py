import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                    password="DALxnq41229",
                                    host="node1429-tanguy.app.ruk-com.cloud",
                                    port="11008",
                                    database="postgres")
    connection.autocommit = True
    cursor = connection.cursor()
    sql = '''CREATE database TestDB'''
    cursor.execute(sql)
    print("Database created successfully.........")
except (Exception,psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL",error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
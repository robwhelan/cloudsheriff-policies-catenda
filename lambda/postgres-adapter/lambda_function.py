import psycopg2
import boto3

try:
    connection = psycopg2.connect(user = "cloudjanitorz",
                                  password = "cloudjanitorz",
                                  host = "cloudjanitorpolicies.c3cnrieiquqk.us-east-1.rds.amazonaws.com",
                                  port = "5432",
                                  database = "cloudjanitorpolicies")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

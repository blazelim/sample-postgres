import psycopg2
from connection import config

def insert_vendor(vendor_name):
    #insert a new vendor into the vendors table
    sql = """INSERT INTO vendors(vendor_name)
            VALUES(%s) RETURNING vendor_id;"""
    
    conn = None
    vendor_id = None
    try:
        # read db configuration
        params = config()

        #connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        #create a new cursor
        cur = conn.cursor()
        #execute the insert statement
        cur.execute(sql, (vendor_name,))
        #get the generated ID back
        vendor_id=cur.fetchone()[0]
        #commit the change to the database
        conn.commit()
        #close the communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return vendor_id

def insert_vendor_list(vendor_list):
    # insert multiple vendors into the vendor table 

    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None

    try:
        #read database configureations
        params = config()
        #connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        #create a new cursor
        cur = conn.cursor()
        #execute the INSERT statement
        cur.executemany(sql,vendor_list)
        #commit the changes to the database
        conn.commit()
        #close the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


from setup import *

def load(df, table_name):
    try:
        rows_imported = 0
        print(f"importing {df.count()} rows ... for table {table_name}")
        df.write.mode("overwrite") \
            .format("jdbc") \
            .option("url", target_url) \
            .option("user", USER_ID_TARGET) \
            .option("password", PWD) \
            .option("driver", DRIVER) \
            .option("dbtable", table_name) \
            .save()
        print("Data imported successful")
        rows_imported += df.count()

    except Exception as e:
        print("Data load error: " + str(e))
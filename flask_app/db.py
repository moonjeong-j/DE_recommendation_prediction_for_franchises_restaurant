import sqlite3
import pandas as pd

#sqlite로 CP1.db데이터를 데이터 프레임으로 리턴하는 함수
def data_load_sqlite():
    import sqlite3
    import pandas as pd 
    conn=sqlite3.connect("CP1.db")
    c=conn.cursor()
    c.execute("SELECT * from brand_all")
    result = c.fetchall()
    c.close()
    conn.close()
    df_result =pd.DataFrame(result, columns=['index','brand', 'category', 'cost', 'year', 'debt_ratio', 'profit', 'fairness', 'growth', 'stability'])
    return df_result

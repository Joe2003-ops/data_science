# %%
# importing neccessary libraries
import pandas as pd
import sqlite3

# %%
# connecting to the database using sqlite3 and creating a connection object conn
conn=sqlite3.connect('data.sqlite')

# %%
df_tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(df_tables)

# %%
pd.read_sql("SELECT * FROM products;", conn)

# %%
pd.read_sql("SELECT productLine, COUNT(*) as count FROM products GROUP BY productLine ORDER BY count DESC;", conn)

# %%
pd.read_sql("SELECT productLine, AVG(buyPrice) as avgPrice FROM products GROUP BY productLine ORDER BY avgPrice DESC;", conn)

# %%
pd.read_sql("SELECT productLine, MIN(MSRP)AS minMSRP, MAX(MSRP) AS maxMSRP FROM products GROUP BY productLine;", conn)

# %%
pd.read_sql("SELECT productLine, MIN(MSRP)AS minMSRP, MAX(MSRP) AS maxMSRP FROM products WHERE MSRP>50 GROUP BY productLine;", conn)

# %%
pd.read_sql("SELECT productLine, MIN(MSRP)AS minMSRP, MAX(MSRP) AS maxMSRP, AVG(MSRP) AS avgMSRP FROM products GROUP BY productLine HAVING avgMSRP>50;", conn)

# %%
pd.read_sql("SELECT productLine, AVG(buyPrice) AS avgPrice, AVG(MSRP) AS avgMSRP FROM products WHERE MSRP>=50 GROUP BY productLine HAVING avgPrice>=50 ORDER BY avgPrice ASC;", conn)

# %%
conn.close()



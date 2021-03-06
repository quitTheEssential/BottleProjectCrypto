#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import sqlite3
from query import query

def ranking_f(got_login):
    try:
        query('drop view v_ranking')
    except:
        pass
    
    query("""create view v_ranking as select u.username, sum( distinct w.value) as portfolio_value, (sum( distinct w.value)-10000)/10000 as return_rate ,count(distinct t.trans_id) as No_of_transactions , (sum( distinct w.value)-10000) as Net_profit from wallets w  left join users u on u.user_id = w.user_id   left join transactions t on t.user_id = u.user_id where strftime("%Y-%m-%d %H:%M:%S",w.createddate) = strftime("%Y-%m-%d %H:%M:%S",(select max(ww.createddate) from wallets ww) ) and u.username is not null and t.crypto_symbol != "USD"  group by u.username order by 2 desc""")
    ranking = query('select * from v_ranking') 
#     df_ranking = pd.DataFrame(ranking, columns = ['Username', 'Portfolio Value', 'Return Rate', 'No. of Transactions', 'Net Profit']).to_html(justify= "justify", classes = "table table-striped table-hover", index = True)
    df_ranking = []
    df_ranking.append(['Username', 'Portfolio Value', 'Return Rate', 'No. of Transactions', 'Net Profit'])
    for elem in ranking:
        result = []
        for ele in elem:
            try:
                result.append(round(ele,4))
            except:  
                result.append(ele)
        df_ranking.append(result)
    return(df_ranking)


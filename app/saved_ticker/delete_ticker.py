from utils.connect_db import connect_db

def delete_ticker(ticker):

    userdb = connect_db()
    cursor = userdb.cursor()

    cursor.execute("DELETE FROM saved_ticker WHERE ticker=%s", (ticker,))
    userdb.commit()
    userdb.close()
    return True
      

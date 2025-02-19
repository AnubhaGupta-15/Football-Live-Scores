#mysql -uroot -p -h 34.89.52.12 --ssl-ca=server-ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem
#mysql -uroot -p -h 34.135.62.220 --ssl-ca=server-ca.pem --ssl-cert=client-cert.pem --ssl-key=client-key.pem
import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'password123',
    'host': '34.69.163.119',
    'database': 'footballdb'
    # 'client_flags': [ClientFlag.SSL],
    # 'ssl_ca':'C:/Users/samto/Documents/Python Scripts/web_app/website/templates/server-ca (2).pem',
    # 'ssl_cert':'C:/Users/samto/Documents/Python Scripts/web_app/website/templates/client-cert (2).pem',
    # 'ssl_key':'C:/Users/samto/Documents/Python Scripts/web_app/website/templates/client-key (2).pem',
    # 'database':'testdatabase'
}

# now we establish our connection
cnxn = mysql.connector.connect(**config)

mycursor = cnxn.cursor()
mycursor.execute("DESCRIBE Users")
for x in mycursor:
    print(x)
#2 mycursor.execute("CREATE TABLE User (name VARCHAR(50),email VARCHAR(60), password VARCHAR(60), UserID int PRIMARY KEY AUTO_INCREMENT)")

#1 mycursor.execute("CREATE DATABASE Footballdatabase")

# # cnxn.close()
# mycursor.execute("INSERT INTO User (name,email,password) VALUES (%s,%s,%s)",("sam","samtob22@gmail.com","password123"))
# cnxn.commit()
# for x in mycursor:
#     print(x)
# mycursor.execute("SELECT * FROM User")

# mycursor.execute("DELETE FROM User")
# cnxn.commit()

# mycursor.execute("SELECT * FROM User")
# for x in mycursor:
#     print(x)
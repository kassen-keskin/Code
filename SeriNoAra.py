import pyodbc

# MSSQL veritabanı bağlantı bilgileri
server = 'DELLBURO\JTLWAWI'
database = 'Mandant_2'
username = 'sa'
password = 'kassenberlin'

# Bağlantı stringi
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Bağlantıyı aç
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Kullanıcıdan input al
input_string = input("Lütfen sorgulamak istediğiniz değeri girin: ")

# SQL sorgusu
query = f"select * from [Mandant_2].[Custom].[SeriNo] with(nolock) where ArtikelSeriNo = ?"



# Sorguyu çalıştır ve sonuçları al
cursor.execute(query, input_string)
rows = cursor.fetchall()

# Sonuçları yazdır
for row in rows:
    print(row)

# Bağlantıyı kapat
cursor.close()
conn.close()
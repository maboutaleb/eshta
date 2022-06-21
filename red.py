import psycopg2


conn = psycopg2.connect(dbname="dap", user="mahmoud_aboutaleb", password="q38EzWarrA2E",port="5439",host="dap-redshift-proxy.prod.aws.chotel.com",sslmode="verify-full")
#conn = psycopg2.connect(dbname="dev", user="awsuser", password="Hamoudizizo1",port="5439",host="redshift-cluster-1.cwdimei3c0rm.us-west-1.redshift.amazonaws.com")

#conn = pyodbc.connect('Driver={Amazon Redshift};Server=redshift-cluster-1.cwdimei3c0rm.us-west-1.redshift.amazonaws.com;UID=awsuser;PWD=Hamoudizizo1;Database=dev')
#conn = pyodbc.connect('DSN=testodbc1;PWD=Hamoudizizo1')
cursor = conn.cursor()
cursor.execute("select top 10 * from big_public_local.prd_comprehensive_consumed_view pccv")
#cursor.execute("select * from users;")
row = cursor.fetchone()
print(row)
cursor.close()
conn.close()
from database import connect

def index():
  connect.mycursor.execute("SELECT * FROM companies limit 1")
  result = connect.mycursor.fetchall()
  return result

def update(company):
  sql = "UPDATE companies SET name = %s, address = %s WHERE id = %s"
  val = (company['name'], company['address'], company['id'])
  connect.mycursor.execute(sql, val)
  connect.mydb.commit()
  print('Company information updated!')
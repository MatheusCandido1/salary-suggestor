from database import connect

def store(name, address):
  sql = "INSERT INTO candidates (name, address) VALUES (%s, %s)"
  val = (name, address)
  connect.mycursor.execute(sql, val)
  connect.mydb.commit()
  
  print(connect.mycursor.rowcount, "candidate saved.")

def index():
  connect.mycursor.execute("SELECT * FROM candidates")
  result = connect.mycursor.fetchall()
  return result

def show(id):
  sql = "SELECT * FROM candidates WHERE id = %s"
  val = (id,)
  connect.mycursor.execute(sql, val)
  result = connect.mycursor.fetchone()
  return result

def update(candidate):
  sql = "UPDATE candidates SET name = %s, address = %s WHERE id = %s"
  val = (candidate['name'], candidate['address'], candidate['id'])
  connect.mycursor.execute(sql, val)
  connect.mydb.commit()

  print(connect.mycursor.rowcount, "candidate updated.")
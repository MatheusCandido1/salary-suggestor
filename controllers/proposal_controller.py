from database import connect

def store(date, candidate_id, job_title, salary, status):
  sql = "INSERT INTO proposals (date, candidate_id, job_title, salary, status) VALUES (%s, %s, %s, %s, %s)"
  val = (date, candidate_id, job_title, salary, status)
  connect.mycursor.execute(sql, val)
  connect.mydb.commit()
  
  print(connect.mycursor.rowcount, "proposal saved.")

def index():
  connect.mycursor.execute("SELECT * FROM proposals")
  result = connect.mycursor.fetchall()
  return result

def show(id):
  sql = "SELECT * FROM proposals WHERE id = %s"
  val = (id,)
  connect.mycursor.execute(sql, val)
  result = connect.mycursor.fetchone()
  return result

def update(proposal):
  sql = "UPDATE proposals SET date = %s, job_title = %s, salary = %s, status = %s WHERE id = %s"
  val = (proposal['date'], proposal['job_title'], proposal['salary'], proposal['status'], proposal['id'])
  connect.mycursor.execute(sql, val)
  connect.mydb.commit()

  print(connect.mycursor.rowcount, "proposal updated.")
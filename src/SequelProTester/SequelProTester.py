class SequelProTester(object):

ROBOT_LIBRARY_SCOPE = 'GLOBAL'

def __init__(self):
self.connection = None

def SequelProConnect(self,hosts,username,pswd,database,charsets):
# Connect to the database
                  connection = pymysql.connect(host=hosts,
                              user=username,
                              password=pswd,
                              db=database,
                              charset=charsets,
                              cursorclass=pymysql.cursors.DictCursor)

    
def SequelProSelectStatment(self,command1):
# Runs Select Statement in Sequel Pro database
   cur = self.connection.cursor()
   cur.execute(command1)
   result = cur.fetchone()
   print(result)
   return result
   connection.close()

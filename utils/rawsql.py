from database import SessionLocal, DB_URL
from sqlalchemy.dialects import postgresql, mysql
from termcolor import colored

class RawSQL():

    def __init__(self, statement):
        self.statement = statement
        
    @property
    def session(self):
        with SessionLocal() as session:
            return session
    
    @property
    def parse(self):
        if DB_URL.split(':')[0] == 'postgresql':
            return colored(' '+str(self.statement.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True})),'blue')
        if DB_URL.split(':')[0] == 'mysql':
            return colored(' '+str(self.statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True})),'blue')
        
    def run(self):
        session = self.session
        try:
            if self.parse.split(' ')[1].lower() == 'select':
                result = session.execute(self.statement)
                return result.scalars().all()
            if self.parse.split(' ')[1].lower() == 'delete':
                session.execute(self.statement)
                session.commit()
                return True
        finally:
            session.close()


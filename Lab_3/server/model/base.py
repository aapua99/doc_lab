from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mssql://DESKTOP-CQ2IQMT\MSSQLSERVER02/lab_db?driver=SQL Server?Trusted_Connection=yes")
conn = engine.connect()
Session = sessionmaker(bind=engine)
print(engine.table_names())
Base = declarative_base()
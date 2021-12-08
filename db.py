from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# postgresql://USUARIOBD:CONTRASEÑA@localhost/NOMBREBD
# conn = create_engine("postgresql://postgres:saimons98@localhost/votaciones")
conn = create_engine("postgresql://sd_final:sd_final@localhost/votaciones")

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
#engine 

DATABASEINFO = "postgresql+psycopg://postgres:1381Arian1381@localhost/firstcompletesicialmedia"

ENGINe = create_engine(DATABASEINFO)
#session =  Session()
sessionarianfirsttry=sessionmaker(autoflush=False,bind=ENGINe,expire_on_commit=False)

def gt_db():
    db = sessionarianfirsttry()
    try: 
        yield db
    finally:
        db.close()

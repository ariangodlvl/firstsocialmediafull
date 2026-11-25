from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
#engine 
from config import coonfig
#databasename , port, databasepassword , databaseusername , databasehost

DATABASEINFO = f"postgresql+psycopg://{coonfig.databaseusername}:{coonfig.databasepassword}{coonfig.databasehost}/{coonfig.databasename}"

ENGINe = create_engine(DATABASEINFO)
#session =  Session()
sessionarianfirsttry=sessionmaker(autoflush=False,bind=ENGINe,expire_on_commit=False)

def gt_db():
    db = sessionarianfirsttry()
    try: 
        yield db
    finally:
        db.close()

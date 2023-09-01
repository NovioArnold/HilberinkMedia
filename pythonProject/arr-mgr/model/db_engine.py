from sqlalchemy import create_engine

engine = create_engine('sqlite:///arr-mgr/model/arr-mgr.db', echo=True)

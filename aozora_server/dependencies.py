from aozora_data.db.db_rdb import DB


async def get_db(db_url="sqlite:///./aozora.db"):
    db = DB(db_url)
    try:
        yield db
    finally:
        db.db.close()

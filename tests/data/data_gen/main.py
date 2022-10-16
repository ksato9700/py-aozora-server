import os

from aozora_data.db.db_rdb import DB
from aozora_data.importer.csv_importer import import_from_csv
from aozora_data.importer.pid_importer import import_from_pid

CSV_URL = "https://www.aozora.gr.jp/index_pages/list_person_all_extended_utf8.zip"
PID_URL = "http://reception.aozora.gr.jp/widlist.php?page=1&pagerow=-1"

DB_URL = "sqlite:///./tests/data/test.db"


def main():
    db = DB(DB_URL)
    if CSV_URL:
        import_from_csv(CSV_URL, db, 150)

    if PID_URL:
        import_from_pid(PID_URL, db)


if __name__ == "__main__":
    main()

from io import BytesIO, StringIO
from zipfile import ZipFile

import requests
from aozora_data.db.db_rdb import DB
from aozora_data.importer.csv_importer import import_from_csv
from aozora_data.importer.pid_importer import import_from_pid

CSV_URL = "https://www.aozora.gr.jp/index_pages/list_person_all_extended_utf8.zip"
PID_URL = "http://reception.aozora.gr.jp/widlist.php?page=1&pagerow=-1"

DB_URL = "sqlite:///./tests/data/test.db"

DB_SIZE = 180


def main():
    db = DB(DB_URL)

    resp = requests.get(CSV_URL)
    resp.raise_for_status()

    with ZipFile(BytesIO(resp.content)) as zipfile:
        csv_rows = zipfile.read(zipfile.namelist()[0]).decode("utf-8-sig").split("\n")

    csv_stream = StringIO()
    csv_stream.writelines((line + "\n" for line in csv_rows[: DB_SIZE + 1]))
    csv_stream.writelines((line + "\n" for line in csv_rows if "あいびき" in line))

    csv_stream.seek(0)
    import_from_csv(csv_stream, db)
    import_from_pid(PID_URL, db)


if __name__ == "__main__":
    main()

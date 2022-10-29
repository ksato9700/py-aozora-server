from aozora_server.dependencies import get_db
from aozora_server.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


async def get_db_test():
    return await get_db("sqlite:///./tests/data/test.db").__anext__()


app.dependency_overrides[get_db] = get_db_test


def test_books():
    resp = client.get("/books")
    assert resp.status_code == 200
    assert len(resp.json()) == 100


def test_book_by_id():
    resp = client.get("/books/123")
    assert resp.status_code == 200
    book = resp.json()
    assert book == {
        "book_id": 123,
        "title": "大川の水",
        "title_yomi": "おおかわのみず",
        "title_sort": "おおかわのみす",
        "subtitle": "",
        "subtitle_yomi": "",
        "original_title": "",
        "first_appearance": "「心の花」1914（大正3）年4月",
        "ndc_code": "NDC 914",
        "font_kana_type": "新字新仮名",
        "copyright": False,
        "release_date": "1999-01-11",
        "last_modified": "2014-09-17",
        "card_url": "https://www.aozora.gr.jp/cards/000879/card123.html",
        "base_book_1": "羅生門・鼻・芋粥",
        "base_book_1_publisher": "角川文庫、角川書店",
        "base_book_1_1st_edition": "1950（昭和25）年10月20日",
        "base_book_1_edition_input": "1985（昭和60）年11月10日改版38版",
        "base_book_1_edition_proofing": "1985（昭和60）年11月10日改版38版",
        "base_book_1_parent": "",
        "base_book_1_parent_publisher": "",
        "base_book_1_parent_1st_edition": "",
        "base_book_2": "",
        "base_book_2_publisher": "",
        "base_book_2_1st_edition": "",
        "base_book_2_edition_input": "",
        "base_book_2_edition_proofing": "",
        "base_book_2_parent": "",
        "base_book_2_parent_publisher": "",
        "base_book_2_parent_1st_edition": "",
        "input": "j.utiyama",
        "proofing": "かとうかおり",
        "text_url": "https://www.aozora.gr.jp/cards/000879/files/123_ruby_1199.zip",
        "text_last_modified": "2004-03-15",
        "text_encoding": "ShiftJIS",
        "text_charset": "JIS X 0208",
        "text_updated": 2,
        "html_url": "https://www.aozora.gr.jp/cards/000879/files/123_15167.html",
        "html_last_modified": "2004-03-15",
        "html_encoding": "ShiftJIS",
        "html_charset": "JIS X 0208",
        "html_updated": 0,
    }

    ## book_id doesn't exists
    resp = client.get("/books/10")
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Book not found"}


def test_book_by_title():
    resp = client.get("/books", params={"title": "吾輩は猫である"})
    assert resp.status_code == 200
    books = resp.json()
    assert len(books) == 1

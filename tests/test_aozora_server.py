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
    assert len(resp.json()) == 4


def test_book_by_id():
    resp = client.get("/books/10002")
    assert resp.status_code == 200
    book = resp.json()
    assert book == {
        "book_id": 10002,
        "title": "title_02",
        "title_yomi": "title_yomi_02",
        "title_sort": "title_sort_02",
        "subtitle": "subtitle_02",
        "subtitle_yomi": "subtitle_yomi_02",
        "original_title": "original_title_02",
        "first_appearance": "first_appearance_02",
        "ndc_code": "ndc_code_02",
        "font_kana_type": "font_kana_type_02",
        "copyright": True,
        "release_date": "1988-07-03",
        "last_modified": "2022-09-03",
        "card_url": "https://example.com/data_02",
        "base_book_1": "base_book_1_02",
        "base_book_1_publisher": "base_book_1_publisher_02",
        "base_book_1_1st_edition": "base_book_1_1st_edition_02",
        "base_book_1_edition_input": "base_book_1_edition_input_02",
        "base_book_1_edition_proofing": "base_book_1_edition_proofing_02",
        "base_book_1_parent": "base_book_1_parent_02",
        "base_book_1_parent_publisher": "base_book_1_parent_publisher_02",
        "base_book_1_parent_1st_edition": "base_book_1_parent_1st_edition_02",
        "base_book_2": "base_book_2_02",
        "base_book_2_publisher": "base_book_2_publisher_02",
        "base_book_2_1st_edition": "base_book_2_1st_edition_02",
        "base_book_2_edition_input": "base_book_2_edition_input_02",
        "base_book_2_edition_proofing": "base_book_2_edition_proofing_02",
        "base_book_2_parent": "base_book_2_parent_02",
        "base_book_2_parent_publisher": "base_book_2_parent_publisher_02",
        "base_book_2_parent_1st_edition": "base_book_2_parent_1st_edition_02",
        "input": "input_02",
        "proofing": "proofing_02",
        "text_url": "https://example.com/02.txt",
        "text_last_modified": "2020-03-03",
        "text_encoding": "text_encoding_02",
        "text_charset": "text_charset_02",
        "text_updated": 3,
        "html_url": "https://example.com/02.html",
        "html_last_modified": "2022-03-03",
        "html_encoding": "html_encoding_02",
        "html_charset": "html_charset_02",
        "html_updated": 2,
    }

    ## book_id doesn't exists
    resp = client.get("/books/200")
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Book not found"}

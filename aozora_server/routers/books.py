from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def read_books(adb=Depends(get_db), title: str | None = None):
    query = {}
    if title:
        query = {"title": title}
    return adb.get_books(query)


@router.get("/{book_id}")
async def read_book_by_id(book_id: int, adb=Depends(get_db)):
    book = adb.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

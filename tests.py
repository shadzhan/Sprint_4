import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_similar_books(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

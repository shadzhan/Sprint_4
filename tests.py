import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize(
        'book_name, expected_result',
        [
            ('Война и мир', True),
            ('', False),
            ('Закат Российской империи или новые приключения неуловимых мстителей', False),
        ]
    )
    def test_add_new_book(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.books_genre) == expected_result



    def test_add_new_book_add_similar_books(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1



    def test_set_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Восточный экспресс')
        collector.set_book_genre('Восточный экспресс', 'Детективы')
        assert collector.get_book_genre('Восточный экспресс') == 'Детективы'


    def test_set_book_genre_of_nonexisting_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Домоводство', 'Фантастика')
        assert collector.get_book_genre('Домоводство') is None

    def test_set_book_genre_incorrect_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пётр первый')
        collector.set_book_genre('Пётр первый', 'Исторический роман')
        assert collector.get_book_genre('Пётр первый') == ''

    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Капитан Немо')
        collector.set_book_genre('Капитан Немо', 'Фантастика')
        assert collector.get_book_genre('Капитан Немо') == 'Фантастика'

    def test_get_book_genre_of_nonexisting_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Забияка') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.add_new_book('Отчуждение')
        collector.set_book_genre('Мгла', 'Ужасы')
        collector.set_book_genre('Отчуждение', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Мгла', 'Отчуждение']

    def test_get_books_for_children_with_no_age_limit(self):
        collector = BooksCollector()
        collector.add_new_book('Небылицы')
        collector.set_book_genre('Небылицы', 'Сказки')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_age_limit(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная история')
        collector.set_book_genre('Ужасная история', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Голова профессора Доуля')
        collector.add_book_in_favorites('Голова профессора Доуля')
        assert collector.get_list_of_favorites_books() == ['Голова профессора Доуля']

    def test_add_book_in_favorites_same_books(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Голова профессора Доуля')
        collector.add_book_in_favorites('Голова профессора Доуля')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Белая ночь')
        collector.add_book_in_favorites('Белая ночь')
        collector.delete_book_from_favorites('Белая ночь')
        assert collector.get_list_of_favorites_books() == []

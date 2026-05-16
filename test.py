import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_default_books_genre_empty_object(self, collector):
        assert collector.get_books_genre() == {}
    
    def test_default_favorites_empty_object(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_default_genre_list(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_default_genre_age_rating_list(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    @pytest.mark.parametrize('name', ['', 'Г' * 41])
    def test_add_new_book_invalid_name_not_added(self, collector, name):
         collector.add_new_book(name)
         assert collector.get_books_genre() == {}

    def test_add_new_book_duplicate_name_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_not_existing_book_not_set(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    def test_get_book_genre_not_existing_book(self, collector):
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    def test_get_books_with_specific_genre_valid_genre_find_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_genre_invalid_genre_not_find(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []
    
    def test_get_books_with_specific_genre_two_books_with_genre_get_all(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби', 'Гарри Поттер и философский камень']

    def test_get_books_with_specific_genre_not_existing_book_not_set(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == []
    
    def test_get_books_genre_valid_books_get_object(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_genre_no_books_get_empty_object(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_genre_invalid_book_not_set(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_valid_book_get_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_get_books_for_children_book_with_age_restriction_not_get_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_no_books_get_empty_list(self, collector):
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_book_with_invalid_genre_not_get_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert collector.get_books_for_children() == []

    def test_books_for_children_book_not_existing_book_not_set(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_for_children() == []

    def test_books_for_children_added_two_book_get_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби', 'Гарри Поттер и философский камень']

    def test_add_book_in_favorites_valid_book_add_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_not_existing_book_not_add_book(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_book_added_once(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1
    
    def test_delete_book_from_favorites_valid_book_delete_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_existing_book_not_delete_book(self, collector):
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и философский камень']

    def test_get_list_of_favorites_books_valid_books_get_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Гарри Поттер и философский камень']

    def test_get_list_of_favorites_books_no_books_get_empty_list(self, collector):
        assert collector.get_list_of_favorites_books() == []

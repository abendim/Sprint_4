# Тесты для BooksCollector


## Список тестов

1. `test_add_new_book_add_two_books` — добавление двух книг, коллекция содержит 2 элемента
2. `test_add_new_book_valid_name` — книга с валидным именем добавлена в коллекцию
3. `test_add_new_book_invalid_name_not_added` — книга с пустым именем или именем длиннее 40 символов не добавляется
4. `test_add_new_book_duplicate_name_not_added` — дублирующаяся книга не добавляется повторно
5. `test_set_book_genre_valid_genre` — жанр из списка успешно устанавливается книге
6. `test_set_book_genre_invalid_genre_not_set` — жанр не из списка не устанавливается
7. `test_set_book_genre_not_existing_book_not_set` — жанр не устанавливается несуществующей книге
8. `test_get_book_genre_not_existing_book` — получение жанра несуществующей книги возвращает `None`
9. `test_get_books_with_specific_genre_valid_genre_find_book` — книга с установленным жанром найдена
10. `test_get_books_with_specific_genre_invalid_genre_not_find` — книги с несуществующим жанром не найдены
11. `test_get_books_with_specific_genre_two_books_with_genre_get_all` — две книги с одним жанром возвращаются обе
12. `test_get_books_with_specific_genre_not_existing_book_not_set` — книга без добавления в коллекцию не найдена по жанру
13. `test_get_books_genre_valid_books_get_object` — возвращается словарь с книгой и её жанром
14. `test_get_books_genre_no_books_get_empty_object` — пустая коллекция возвращает пустой словарь
15. `test_get_books_genre_invalid_book_not_set` — книга без добавления не попадает в коллекцию
16. `test_get_books_for_children_valid_book_get_book` — книга без возрастного ограничения попадает в список
17. `test_get_books_for_children_book_with_age_restriction_not_get_book` — книга с жанром «Ужасы» не попадает в детский список
18. `test_get_books_for_children_no_books_get_empty_list` — пустая коллекция возвращает пустой список
19. `test_get_books_for_children_book_with_invalid_genre_not_get_book` — книга с невалидным жанром не попадает в детский список
20. `test_books_for_children_book_not_existing_book_not_set` — несуществующая книга не попадает в детский список
21. `test_books_for_children_added_two_book_get_list` — две книги без ограничений возвращаются обе
22. `test_add_book_in_favorites_valid_book_add_book` — книга успешно добавлена в избранное
23. `test_add_book_in_favorites_not_existing_book_not_add_book` — несуществующая книга не добавляется в избранное
24. `test_add_book_in_favorites_book_added_once` — одна и та же книга добавляется в избранное только один раз
25. `test_delete_book_from_favorites_valid_book_delete_book` — книга успешно удалена из избранного
26. `test_delete_book_from_favorites_not_existing_book_not_delete_book` — удаление несуществующей книги не затрагивает другие книги в избранном
27. `test_get_list_of_favorites_books_valid_books_get_list` — две книги в избранном возвращаются списком
28. `test_get_list_of_favorites_books_no_books_get_empty_list` — пустое избранное возвращает пустой список


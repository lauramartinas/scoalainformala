import contextlib

# class just_some_exceptions:
#     def __init__(self):
#         self.dictionary = {'Brand': 'Volkswagen', 'Model':'Polo'}
# #
#     def __enter__(self):
#         return self.dictionary
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         try:
#             dict_model = dict['Model']
#             print(dict_model)
#             dict_year = dict['Year']
#             print(dict_year)
#         except KeyError as cheie:
#             print('The key', cheie,'is NOT in dictionary!')
#         finally:
#             return
#
# with just_some_exceptions() as dict:
#     print('*' * 30)
#     print(dict)

# class just_some_exceptions:
#
#     def __init__(self):
#         self.list = [3,'g', 7, 'k', 9, 14, 'a']
#
#     def __enter__(self):
#         return self.list
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#
#         error_message = ''
#
#         try:
#             print(list[1])
#         except IndexError as eroare:
#             print(eroare)
#             error_message = 'The index number is NOT in list'
#         finally:
#             if error_message:
#                 print(error_message)
#
# with just_some_exceptions() as list:
#     print('The list:', list)

#test eroare index

# class just_some_exceptions:
#
#     def __init__(self):
#         self.list = [3,'g', 7, 'k', 9, 14, 'a']
#
#     def __enter__(self):
#         return self.list
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#
#         error_message = ''
#
#         try:
#             print(list[10])
#         except IndexError as eroare:
#             print(eroare)
#             error_message = 'The index number is NOT in list'
#         finally:
#             if error_message:
#                 print(error_message)
#
# with just_some_exceptions() as list:
#     print('The list:', list)

# @contextlib.contextmanager
#
# def just_some_exceptions():
#
#     dict = {'Brand': 'Volkswagen', 'Model': 'Polo'}
#     yield
#
#     error_message = ''
#
#     try:
#         dict_model = dict['Model']
#         print(dict_model)
#         dict_year = dict['Year']
#         print(dict_year)
#     except KeyError as cheie:
#         print('The key', cheie,'is NOT in dictionary!')
#     finally:
#         if error_message:
#             print(error_message)
#
# with just_some_exceptions() as dict:
#     print('-' * 30)

# @contextlib.contextmanager
#
# def just_some_exceptions():
#     list = [3,'g', 7, 'k', 9, 14, 'a']
#     yield
#
#     print(list)
#     error_message = ''
#
#     try:
#         print(list[1])
#     except IndexError as eroare:
#         print(eroare)
#         error_message = 'The index number is NOT in list'
#     finally:
#         if error_message:
#             print(error_message)
#
# with just_some_exceptions() as list:
#     print()

#test eroare index

# @contextlib.contextmanager
#
# def just_some_exceptions():
#     list = [3,'g', 7, 'k', 9, 14, 'a']
#     yield
#
#     print(list)
#     error_message = ''
#
#     try:
#         print(list[10])
#     except IndexError as eroare:
#         print(eroare)
#         error_message = 'The index number is NOT in list'
#     finally:
#         if error_message:
#             print(error_message)
#
# with just_some_exceptions() as list:
#     print()

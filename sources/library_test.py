import unittest
import library as l



class Test(unittest.TestCase):

    books = []
    obj = l.Library()
    def test_add_book(self):
        book = self.obj.add_book('Python')
        self.books.append('Python')
        self.assertEqual(book,self.books)
        print(book)
        print(self.books)

    def test_display_book(self):
        b = self.obj.display_books()
        if self.books:
            self.assertEqual(b,self.books)
        else:
            self.assertEqual(b,False)

    def test_lend_book(self):  # Request for a book
        flag = self.obj.lend_book("Python")
        if 'Python' in self.books:
            self.books.remove('Python')
            self.assertEqual(flag,True)
        else:
            print('Book is not in library')



if __name__ == '__main__':
    unittest.main()

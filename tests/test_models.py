
import unittest

from notebook import db

class Notebook_models_TestCase(unittest.TestCase):

    def setUp(self):
        self.library_definitions = (
            ('Library of Alexandria', 'library-of-alexandria',
            'an ancient library of importance which was destroyed by fire '+\
            'For more information check out the wikipedia link: '+\
            'http://en.wikipedia.org/wiki/Library_of_Alexandria'),
            ('The Library of Congress', 'the-library-of-congress',
                'no description'),
        )
        

        self.db = db.Connection(db.MEMORY_DATABASE_URI, debug=False)

    def tearDown(self):
        pass

    def create_library(self, libdef):
        """ creates a new library from the given library definition"""
        self.db.soup.libraries.insert(title = libdef[0], slug = libdef[1],
                description = libdef[2])
        return self.db.soup.libraries.filter_by(slug = libdef[1])

    def create_book(self, bookdef, library):
        """creates a new book from the book definition in the given library"""
        rec = self.db.soup.books.insert(library_id = library.library_id, slug=bookdef[1],
                title = bookdef[0])
        return rec


    def test_library(self):
        """Tests actions on libraries"""
        # title, slug, description
       #print 'dir libraries:'
        #print dir(self.db.tables.libraries)
        for i in self.library_definitions:
            self.db.soup.libraries.insert(title=i[0], slug=i[1], 
                    description=i[2])
        
        recs = self.db.soup.libraries.all()
        assert len(recs) == len(self.library_definitions)


    def test_books(self):

        # create a library and add books
        a_library = self.library_definitions[0]
        self.db.soup.libraries.insert(title=a_library[0], 
                slug=a_library[1],
                description=a_library[2])
        my_library = self.db.soup.libraries.filter_by(
                slug=a_library[1]).one()
        print my_library.slug
        bookdef = (
            'a little book', 'a-little-book'
                )
        rec = self.create_book(bookdef, my_library)
        print 'type = ', type(rec)
        print 'dir = ', dir(rec)
    
    
    def test_pages(self):
       pass 


import unittest

from restnotes import db

class Restnotes_models_TestCase(unittest.TestCase):

    def setUp(self):
        self.libraries = (
            ('Library of Alexandria', 'library-of-alexandria',
            'an ancient library of importance which was destroyed by fire '+\
            'For more information check out the wikipedia link: '+\
            'http://en.wikipedia.org/wiki/Library_of_Alexandria'),
            ('The Library of Congress', 'the-library-of-congress',
                'no description'),
        )
        

        self.db = db.Connection(db.MEMORY_DATABASE_URI, debug=True)

    def tearDown(self):
        pass

    def test_library(self):
        """Tests creating, read, update, delete library"""
        # title, slug, description
       #print 'dir libraries:'
        #print dir(self.db.tables.libraries)
        for i in self.libraries:
            self.db.soup.libraries.insert(title=i[0], slug=i[1], 
                    description=i[2])
        
        recs = self.db.soup.libraries.all()
        assert len(recs) == len(self.libraries)
        
    def test_books(self):

        # create a library and add books
        a_library = self.libraries[0]
        self.db.soup.libraries.insert(title=a_library[0], 
                slug=a_library[1],
                description=a_library[2])
        my_library = self.db.soup.libraries.filter_by(
                slug=a_library[1]).one()
        print my_library.slug


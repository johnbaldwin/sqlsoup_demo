# -*- coding: utf-8 -*-
"""
Database module
"""
from collections import namedtuple
from sqlalchemy import schema, types, MetaData
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import mapper
import sqlsoup


restnotes_tables = namedtuple('restnotes_tables', 
    'libraries books pages media')

# This is used for unit testing
MEMORY_DATABASE_URI = 'sqlite:///:memory:'

def define_tables(metadata):
    """ Create table definitions. This is used for allowing SQLSoup to 
        perform its autodiscover on a SQLite memory database instance.

        The tables defined below are 'bare-bones' intended to illustrate
        the core concepts of this project

        Types to add: create date, modify date, owner,
        authorizations, tags, history (revision control)
    """
    # TODO: Refactor from hardcoding to resource file and expand to list
    # of column parameters for each table
    library_table = schema.Table('libraries', metadata,
        schema.Column('library_id', types.Integer, primary_key = True),
        schema.Column('slug', types.String(80), nullable = False,
            unique = True),
        schema.Column('title', types.String(120), default = u''),
        schema.Column('description', types.String(240), default = u''),
        )
    book_table = schema.Table('books', metadata,
        schema.Column('book_id', types.Integer, primary_key = True),
        schema.Column('library_id', types.Integer, 
            schema.ForeignKey('libraries.library_id'), nullable = False),
        schema.Column('slug', types.String(80)),
        schema.Column('title', types.String(120), default = u''),
        schema.Column('description', types.String(240), default = u''),
        )
    page_table = schema.Table('pages', metadata,
        schema.Column('page_id', types.Integer, primary_key = True),
        schema.Column('book_id', types.Integer, 
            schema.ForeignKey('books.book_id'), nullable = False),
        schema.Column('slug', types.String(80)),
        schema.Column('mimetype', types.String(80), nullable = False),
        schema.Column('body', types.Text),
        )

    media_table = schema.Table('media', metadata,
        schema.Column('media_id', types.Integer, primary_key = True),
        schema.Column('library_id', types.Integer, 
            schema.ForeignKey('libraries.library_id'), nullable = False),
        schema.Column('data', types.Binary),
        )

    return restnotes_tables(library_table, book_table, 
        page_table, media_table)
    


class Connection(object):
    """
    Provides database connection and SQLSoup instantiation
    """

    def __init__(self, database_uri, **kwargs):
        self.database_uri = database_uri

        self.debug = kwargs.get('debug', False)
        if not isinstance(self.debug, bool):
            errmsg = 'restnotes.db.Connection debug parameter must be '+\
                    'a bool'
            raise ValueError(errmsg)

        self.engine = create_engine(self.database_uri, echo=self.debug)
        self.metadata = MetaData(self.engine)

        # If running with a memory database instance, need to define the tables
        if self.database_uri == MEMORY_DATABASE_URI:
            self.table_definitionss = define_tables(self.metadata)
        
        self.metadata.create_all(self.engine)
        self.soup = sqlsoup.SQLSoup(self.engine)


        

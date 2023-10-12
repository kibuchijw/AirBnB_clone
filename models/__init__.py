#!/usr/bin/python3
"""Module that initializes a FileStorage instance for the application.
1. It imports the FileStorage class from file_storage.py.
2. Creates an instance of FileStorage and assigns it to 'storage'.
3. Calls the 'reload()' method on 'storage' to initialize it.
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

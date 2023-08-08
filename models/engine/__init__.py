#!/usr/bin/python3
"""Initializes the packages"""

"""importation of filestorage from engine in models"""
from models.engine.file_storage import FileStorage

"""instance of class file storage interface"""
storage = FileStorage()

"""Reloads file storage with latest version of packages that are available"""
storage.reload()

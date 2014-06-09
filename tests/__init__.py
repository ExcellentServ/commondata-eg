from os.path import join
from unittest import TestCase
import doctest


class DocTests(TestCase):

    def test_docs(self):
        doctest.testfile(join('..', "README.rst"), encoding="utf-8")

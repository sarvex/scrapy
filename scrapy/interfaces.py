from zope.interface import Interface

class ISpiderManager(Interface):

    def from_settings(self):
        """Returns an instance of the class for the given settings"""

    def load(self):
        """Returns the Spider class for the given spider name. If the spider
        name is not found, it must raise a KeyError."""

    def list():
        """Return a list with the names of all spiders available in the
        project"""

    def find_by_request(self):
        """Returns the list of spiders names that can handle the given request"""

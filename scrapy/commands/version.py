from __future__ import print_function
import sys
import platform

import twisted

import scrapy
from scrapy.command import ScrapyCommand


class Command(ScrapyCommand):

    def syntax(self):
        return "[-v]"

    def short_desc(self):
        return "Print Scrapy version"

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("--verbose", "-v", dest="verbose", action="store_true",
            help="also display twisted/python/platform info (useful for bug reports)")

    def run(self, args, opts):
        if opts.verbose:
            import lxml.etree
            lxml_version = ".".join(map(str, lxml.etree.LXML_VERSION))
            libxml2_version = ".".join(map(str, lxml.etree.LIBXML_VERSION))
            print(f"Scrapy  : {scrapy.__version__}")
            print(f"lxml    : {lxml_version}")
            print(f"libxml2 : {libxml2_version}")
            print(f"Twisted : {twisted.version.short()}")
            print("Python  : %s" % sys.version.replace("\n", "- "))
            print(f"Platform: {platform.platform()}")
        else:
            print(f"Scrapy {scrapy.__version__}")

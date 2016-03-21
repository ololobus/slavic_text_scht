#!/usr/bin/env python
# coding=utf-8
# @description Simple TEI reach *.xml files parser.
# @author Alexey Kondratov

import sys
# import codecs

from xml.sax import make_parser, handler


class TEIContentHandler(handler.ContentHandler):

    def __init__(self):
        self.text = ''

        self.current_tag = None
        self.prev_tag = None

    def startElement(self, tag, attrs):
        self.prev_tag = self.current_tag
        self.current_tag = tag

        if tag == 'w':
            self.text += ' '

    def endElement(self, tag):
        pass

    def characters(self, content):
        if self.current_tag == 'orig':
            self.text += content.strip()
        elif self.current_tag == 'c':
            self.text += content.strip()

    def endDocument(self):
        print(self.text)


def TEIParser(path):
    # I don't know why but default 'open' behaviour is better to handle diferent encodings.
    # source = codecs.open(path, 'r', encoding='utf8')
    source = open(path, 'r')

    tei_parser = make_parser()

    tei_parser.setFeature(handler.feature_external_ges, False)
    tei_parser.setFeature(handler.feature_namespaces, False)  # Turn off namepsaces
    tei_parser.setFeature(handler.feature_namespace_prefixes, False)

    tei_parser.setContentHandler(TEIContentHandler())

    tei_parser.parse(source)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TEIParser(sys.argv[1])
    else:
        print('Please, pass the path to an xml file')

#-*- coding: utf-8 -*-
"""
Module to convert table of contents of PDF file to mindmap format.

@author     Lucas Koelman
@date       20/02/2018

@see        https://github.com/pdfminer/pdfminer.six/blob/master/tools/dumppdf.py
@see        https://github.com/xmindltd/xmind-sdk-python/blob/master/example.py
"""

# standard library
import sys, os, re
import xml.etree.ElementTree as etree
try:
    import cStringIO as io # Python 2
except (ImportError, ModuleNotFoundError):
    import io # Python 3
import dumppdf

import xmind
from xmind.core.topic import TopicElement


def toc_to_xmind(outfp, pdf_filename):
    """
    Convert table of contents of given PDF file to XMind document.
    """
    out_str = io.StringIO()
    dumppdf.dumpoutline(out_str, pdf_filename, [], set())

    # Parse XML
    toc_xml = out_str.getvalue()
    out_str.close() # no 'with' statement possible
    root_elem = etree.fromstring(toc_xml)

    # Convert XML to XMind document
    xwb = xmind.load(outfp) # load an existing file or create a new workbook if nothing is found

    # Create XMind workbook
    s1 = xwb.getPrimarySheet()
    s1.setTitle(os.path.split(pdf_filename)[-1])
    root_topic = s1.getRootTopic()
    root_topic.setTitle("Contents")

    # Transform each XML node into a mindmap node
    topic_stack = [root_topic] # length will always equal depth/level during traversal
    prev_level = 0
    for node in root_elem.iter(): # depth-first traversal
        if 'level' not in node.attrib:
            continue # irrelevant node
        node_level = int(node.attrib['level'])
        
        # Create topic for this node
        topic = TopicElement(ownerWorkbook=xwb)
        title = re.sub(r"^[a-zA-Z]'(.*)'$", r'\1', node.attrib['title'])
        topic.setTitle(title)
        
        # Add it to the topic tree
        level_difference = node_level - prev_level
        for _ in range(-level_difference+1): # negative yields empty list
            topic_stack.pop()
        topic_stack[-1].addSubTopic(topic)
        topic_stack.append(topic)
        prev_level = node_level

    xmind.save(xwb)


def main(argv):
    """
    Run conversion tool from command line.
    """
    import getopt
    def usage():
        print ('usage: %s -o outfile.xmind pdf_file.pdf' % argv[0])
        return 100
    try:
        (opts, args) = getopt.getopt(argv[1:], 'o:')
    except getopt.GetoptError:
        return usage()
    if not args:
        return usage()

    dopts = dict(opts)
    outfp = dopts['-o']
    pdf_filename = args[0]
    toc_to_xmind(outfp, pdf_filename)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
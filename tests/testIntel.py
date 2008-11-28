#!/usr/bin/env python
#
#   hostmap
#
#   Author:
#    Alessandro `jekil` Tanasi <alessandro@tanasi.it>
#
#   License:
#    This program is private software; you can't redistribute it and/or modify
#    it. All copies, included printed copies, are unauthorized.
#    
#    If you need a copy of this software you must ask for it writing an
#    email to Alessandro `jekil` Tanasi <alessandro@tanasi.it>


import sys
sys.path.append("../")

import unittest
from lib.common import *
from lib.intel import *



class testIntel(unittest.TestCase):
    """
    Tests the host intelligence controller
    @license: Private licensing
    @author: Alessandro Tanasi
    @contact: alessandro@tanasi.it
    """

    def setUp(self):
        self.intel = Host("127.0.0.1")
        
    def testSetHostname(self):
        host = "abc.antani.com"
        self.intel.hostname = host
        self.assertEqual(self.intel.hostname, host)

    def testSetHost(self):
        # Add one
        self.assertEqual(self.intel.setHost("a.a"), True)
        # Add two
        self.assertEqual(self.intel.setHost("b.a"), True)
        self.assertEqual(self.intel.setHost("b.a"), False)
        
    def testSetDomain(self):
        # Add one
        self.assertEqual(self.intel.setDomain("a.a"), True)
        # Add two
        self.assertEqual(self.intel.setDomain("b.a"), True)
        self.assertEqual(self.intel.setDomain("b.a"), False)
    
        
        
if __name__ == '__main__':
    unittest.main()
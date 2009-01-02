#!/usr/bin/env python
#
#   hostmap
#
#   Author:
#    Alessandro `jekil` Tanasi <alessandro@tanasi.it>
#
#   License:
#
#    This file is part of hostmap.
#
#    hostmap is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    hostmap is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with hostmap.  If not, see <http://www.gnu.org/licenses/>.

"""
Configuration file. Some environment variables can be changed here.
@license: Private licensing
@author: Alessandro Tanasi
@contact: alessandro@tanasi.it
"""

# Version specific
VERSION = "0.1"
CODENAME = "ghironda"

# Dictionaries settings
HOSTLISTLITE = "dictionaries/hostnames-lite.txt"
HOSTLISTCUSTOM = "dictionaries/hostnames-custom.txt"
HOSTLISTFULL = "dictionaries/hostnames-full.txt"

# Plugins settings
PLUGINDIR = "discovery"

# HTTP ports
HTTP_PORTS = [80, 443, 8080]
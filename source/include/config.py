#!/usr/bin/env python

# Enable debug output. Prints lots of information about internal workings.
# Note: Debug output is very noisy and should not be used in production.
DEBUG = False

# From which directory should Uforia start to scan?
# Example: STARTDIR = '/home/user/' 
STARTDIR = '/home/TESTDATA/'

# Should Uforia attempt to detect and run additional modules for each
# of the fond files/filetypes? If so, where should Uforia find the
# modules to handle those files?
# Note: You should not normally have to modify this!
# Example: ENABLEMODULES = True
# Example: MODULEDIR = './modules/'
ENABLEMODULES = False
MODULEDIR = './modules/'

# Database configuration. The name should match the handler providing
# the appropriate Database class with setup() and store() methods.
# Example: DBTYPE = 'mysql'
DATABASEDIR = './databases/'
DBTYPE = 'mysql'
DBHOST = 'localhost'
DBUSER = 'uforia'
DBPASS = 'uforia'
DBNAME = 'uforia'

# Should Uforia TRUNCATE/DROP any existing tables? Setting this to False
# can be useful when you want to add additional evidence items on an
# already-examined filesystem
TRUNCATE = True

# How many processes should be parsing files at the same time?
# Note: This is a tradeoff between CPU power and disk I/O. More workers
# means higher CPU utilization, but disk I/O might become a limiting factor.
# Conversely: less workers might mean optimal disk I/O, but your CPU might
# be sitting idle...
# Example: CONSUMERS = 2
CONSUMERS = 1

# How many modules should be processing a file at the same time?
# Note: This is a tradeoff between CPU power and disk I/O. More workers
# means higher CPU utilization, but disk I/O might become a limiting factor.
# Conversely: less workers might mean optimal disk I/O, but your CPU might
# be sitting idle...
# Example: MODULES = 1
MODULES = 1

# ADVANCED CONFIGURATION, FOR EXPERTS ONLY

# Tune the filesystem block reads
# Example: CHUNKSIZE = 65536
CHUNKSIZE = 65536

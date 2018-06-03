#!/usr/bin/env python3
# 

import psycopg2
import datetime

DBNAME = "news"

def q1():
  """Return 3 most popular articles, most popular first"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select * from q1;")
  return c.fetchall()
  db.close()

def q2():
  """Return 3 most popular authors, most popular first"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select * from q2;")
  return c.fetchall()
  db.close()

def q3():
  """Return days where > 1 percent of requests led to errors"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select * from q3;")
  return c.fetchall()
  db.close()

def outputReports():
  '''Print out reports in plain text'''

  topThreeArticles =  q1()
  print 'Top 3 articles:'
  for a in topThreeArticles:
      article = a[0]
      views = a[1]
      print '"%s" - %s views' % (article,str(views))

  topThreeAuthors =  q2()
  print '\nTop authors:'
  for a in topThreeAuthors:
      author = a[0]
      views = a[1]
      print '"%s" - %s views' % (author,str(views))

  errorRate =  q3()
  print '\nDays with over 1% Errors:'
  for d in errorRate:
      day = d[0]
      errorPercent =d[1]
      print '"%s" - %s%% errors' % (day,str(errorPercent))
  
if __name__ == '__main__':
  outputReports()
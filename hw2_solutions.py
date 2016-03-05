"""
Columbia W4111 Intro to databases
Homework 2
Data Analysis and Relational Algebra
eugene wu 2015
"""

from collections import *
import pdb

def load_data(file_path):
  """
  This method reads the dataset, and returns a list of rows.
  Each row is a list containing the values in each column.
  """
  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]

def q1(data):
  """
  @param data the output of load_data()
  @return the number of  distinct types of items (by `description` attribute) in this dataset
  """
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)

  ret = set()
  for row in data:
    ret.add(row[15])
  return len(ret) - 1

def q2(data):
  """
  @param data the output of load_data()
  @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
  """
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)

  ret = set()
  for row in data:
    ret.add(row[13])
  return len(ret) - 1

def q3(data):
  """
  @param data the output of load_data()
  @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  d = defaultdict(lambda: 0)
  for row in data[1:]:
    d[row[2]] += int(row[20])

  return sorted(d.items(), key=lambda p: p[1])[-1][0]

def q4(data):
  """
  @param data the output of load_data()
  @return The value of the `description` attribute of the most sold item from the store from q3()
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  storeid = q3(data)
  d = defaultdict(lambda: 0)

  for row in data[1:]:
    if row[2] == storeid:
      d[row[15]] += int(row[20])
 
  return sorted(d.items(), key=lambda p: p[1])[-1][0]

def q5(data):
  """
  Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` “TEQUILA”
  @param data the output of load_data()
  @return The value of the `zipcode` attribute with the most sales in “TEQUILA” category
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  category = “TEQUILA”
  d = defaultdict(lambda: 0)

  for row in data[1:]:
    if row[11] == category:
      d[row[6]] += int(row[20])

  return sorted(d.items(), key=lambda p: p[1])[-1][0]

if __name__ == '__main__':
  import click

  @click.command(help="Run the queries on the csv file")
  @click.argument('FILE_PATH')
  def run(file_path):
    data = load_data(file_path)
    print q1(data)
    print q2(data)
    print q3(data)
    print q4(data)
    print q5(data)

  run()
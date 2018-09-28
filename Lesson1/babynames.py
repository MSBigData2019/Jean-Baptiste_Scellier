#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'rU')
  # 'line' sert a stocker les lignes une par une
  line = f.next()
  # on se rend a la ligne contenant l'annee
  # elle ressemble a cela : '      &nbsp; <input type="text" name="year" id="yob" size="4" value="1990">'
  while(line[32:43] != 'name="year"'):
    line = f.next()
  year = line[-7:-3]
  # ensuite on se rend aux lignes contenant les prenoms
  # elles ressemblent a cela : '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>'
  while(line[:18] != '<tr align="right">'):
    line = f.next()
  # on stocke les 1000 prenoms dans une liste
  names = [year]
  for i in range(1000):
    # on coupe la ligne en 4 et on ne prend pas les '</td>' a la fin de chaque morceau
    pieces = line.split('<td>')
    rank = pieces[1][:-5]
    boy = pieces[2][:-5]
    girl = pieces[3][:-6]
    names += [boy + ' ' + rank, girl + ' ' + rank]
    line = f.next()
    # Il faut sauter 2 lignes pour le fichier 2008
    if(len(line) < 10):
      line = f.next()
  # on trie par ordre alphabetique (l'annee reste en top position)
  names = sorted(names)
  f.close()
  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for arg in args:
    text = extract_names(arg)
    text = '\n'.join(text) + '\n'
    f = open(arg + '.summary', 'w')
    f.write(text)
    f.close()
  
if __name__ == '__main__':
  main()


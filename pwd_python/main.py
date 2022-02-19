from __future__ import unicode_literals
import sys
import questionary
from add import add
from delete import delete
from search import search
from update import update
from see import see
from int_search import search_int

resposta = questionary.select(
    'What do you want to do?',
    choices=[
        'Add a Entry',
        'Search for a Entry',
        'Search by ID',
        'See All Entries',
        'Update a Entry',
        'Delete a Entry',
        'Exit'
            ]).ask()

if resposta == 'Add a Entry':
    add()
if resposta == 'Search for a Entry':
    search()
if resposta == 'Search by ID':
    search_int()
if resposta == 'See All Entries':
    see()
if resposta == 'Update a Entry':
    update()
if resposta == 'Delete a Entry':
    delete()
if resposta == 'Exit':
    sys.exit()

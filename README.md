# code-katas

## Autocomplete kata
Autocomplete - a callable Python class which implements autocomplete functionality. The class takes a list of words to be a vocabulary as an argument on initialization. It also accepts a max_completions argument, which controls the maximum number of suggested completions for a given string. By default, max_completions = 5.

The input to the call method for the class is the string the user has typed. When called, this class returns a list of at most max_completions suggested words. If there are more available completions than allowed, 5 random ones are returned. If there are no completions available, an empty list is returned.

### How to use:
```
$pip install -e ./
$python
>>> from autocomplete import Autocomplete
>>> vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
>>> complete_me = AutoCompleter(vocabulary, max_completions=4)
>>> complete_me('f')
['fix', 'fax', 'fit', 'fist']
>>> complete_me('fi')
['fix', 'fit', 'fist', 'finch']
>>> complete_me('fin')
['finch', 'final', 'finial']
>>> complete_me('finally')
[]
```

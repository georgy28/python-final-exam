# Multiple choice questions

My comments on a few ambiguous questions.

### How do we remove an element from a list?
```python
    list.delete()
    list.remove()
    list.remove(-1)
    list.delete(-1)
```

list.remove(-1) is correct if -1 exists in a list
list.remove() without an argument is wrong, but with one argument is correct (ok throws error if it does not exit in the list)
The other 2 choices are wrong anyway

So I think that the phrasing of the question is a bit problematic. The unambiguous way would be to ask: How do we remove element x from a list? Providing the choice: list.remove(x)

I finally decided to choose list.remove() as my answer because I assumed that the question was asking us to identify the correct method in general because "an element" was used when phrasing it.

### Which of the following best describes inheritance?

"Allows for implementation of elegant software that is well designed and easily modified"

The above is also a reason why we use inheritance but I assumed that the question was about definition so the 1st choice was more relevant.
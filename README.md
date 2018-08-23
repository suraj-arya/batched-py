# batched-py



A short utility decorator to run a function in batched set of arguments

## how to use

import the decorator and decorate any function like this

```python
   
   from batched import batched
   @batched(batch_size=10)
   def run_in_batch(data, arg1, arg2, kwarg1=value1):
       print data
       return true

```

then call the function run_in_batch with more than 10 items in a list and it will be called automatically in batches of 10

```python

   run_in_batch(data, a, b)

```


* Free software: MIT license
* Documentation: https://batched.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

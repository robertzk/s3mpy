# A dead-simple S3 interface for Python

Storing Python objects to persist across multiple sessions can be useful for a 
variety of reasons. Storing them on Amazon's S3 is even better, since they
become universally accessible.

To store Python objects to S3 from your REPL (and easily share your objects
with others), set your `AWS_ACCESS_KEY` and `AWS_SECRET_ACCESS_KEY` 
environment variables to their appropriate values, and set `S3_BUCKET`
to the name of the bucket you would like to use for the interface.

Assuming you have installed the module in this repo, you can then execute

```python
from s3mpy.mailman import Mailman
s3read = Mailman.s3read
s3store = Mailman.s3store
```

and enjoy dead-simple storing and loading of Python objects:

```
>>> s3store({'a': 1, 'b': 2}, 'foo/bar')
30
>>> s3read('foo/bar')
{'a': 1, 'b': 2}
```


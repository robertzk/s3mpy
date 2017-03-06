# A dead-simple S3 interface for Python

Storing Python objects to persist across multiple sessions can be useful for a 
variety of reasons. Storing them on Amazon's S3 is even better, since they
become universally accessible.

To store Python objects to S3 from your REPL (and easily share your objects
with others), set your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` 
environment variables to their appropriate values, and set `S3_BUCKET`
to the name of the bucket you would like to use for the interface.


## Installation

Assuming you have installed the module in this repo, you can then execute

```python
from s3mpy import mailman
m = mailman.Mailman()
m.store("test_value", "test_key")
m.read("test_key")
> 'test_value'
```

You'll also have to set the following in your `~/.bash_profile` and make sure it's sourced:

```
export AWS_ACCESS_KEY_ID=YOURACCCESSKEY
export AWS_SECRET_ACCESS_KEY=YOURSECRETKEY
export S3_BUCKET=bucketname
```

Enjoy dead-simple storing and loading of Python objects!

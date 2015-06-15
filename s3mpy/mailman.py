from pickle import dump, load
from os import tempnam, remove
from boto.s3.bucket     import Bucket
from boto.s3.connection import S3Connection
from boto.s3.key        import Key

class Mailman:

    def __init__(self, conn, bucket):
        """
        Create an S3MPY mailman, responsible for storing an reading Python
        objects from S3 keys.
        """

        if type(conn) != S3Connection:
            raise TypeError("Please specify an S3Connection.")

        if type(bucket) == str:
            bucket = Bucket(conn, bucket)

        if type(bucket) != Bucket:
            raise TypeError("Please specify a Bucket object.")

        self._conn   = conn
        self._bucket = bucket

    def store(self, obj, key):
        """
        Store a (pickled) Python object to the specified S3 key.

        Return the number of characters stored as an integer.
        """

        if type(key) == str:
            key = Key(self._bucket, key)

        if type(key) != Key:
            raise TypeError("Please specify a valid Key.")

        tempfile     = tempnam()
        file_pointer = open(tempfile, "wb")
        dump(obj, file_pointer)
        file_pointer.close()

        length = key.set_contents_from_filename(tempfile)
        remove(tempfile)

        return length

    def read(self, key):
        """
        Read a (pickled) Python object from the specified S3 key.

        Return the Python object that was pickled to S3.
        """

        if type(key) == str:
            key = Key(self._bucket, key)

        if type(key) != Key:
            raise TypeError("Please specify a valid Key.")

        tempfile = tempnam()
        key.get_contents_to_filename(tempfile)

        file_pointer = open(tempfile, "r")
        object = load(file_pointer)
        file_pointer.close()

        remove(tempfile)

        return object


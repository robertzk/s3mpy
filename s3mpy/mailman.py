from pickle import dump, load
import os
from boto.s3.bucket     import Bucket
from boto.s3.connection import S3Connection
from boto.s3.key        import Key

class Mailman(object):

    def __init__(self, conn = S3Connection(os.environ.get("AWS_ACCESS_KEY_ID"), os.environ.get("AWS_SECRET_ACCESS_KEY")), bucket = os.environ.get("S3_BUCKET")):
        """
        Create an S3MPY mailman, responsible for storing an reading Python
        objects from S3 keys.
        """

        if type(bucket) == str:
            if type(conn) != S3Connection:
                raise TypeError("Please specify an S3Connection.")

            bucket = Bucket(conn, bucket)

        if type(bucket) != Bucket:
            raise TypeError("Please specify a Bucket object.")

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

        tempfile     = os.tempnam()
        file_pointer = open(tempfile, "wb")
        dump(obj, file_pointer)
        file_pointer.close()

        length = key.set_contents_from_filename(tempfile)
        os.remove(tempfile)

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

        tempfile = os.tempnam()
        key.get_contents_to_filename(tempfile)

        file_pointer = open(tempfile, "r")
        object = load(file_pointer)
        file_pointer.close()

        os.remove(tempfile)

        return object


    @staticmethod
    def s3read(s3key, bucket = Bucket(S3Connection(os.environ.get("AWS_ACCESS_KEY_ID"), os.environ.get("AWS_SECRET_ACCESS_KEY")), os.environ.get("S3_BUCKET"))):
        """
        Read a Python object from a given S3 key. Note that the bucket will by
        default by selected as the S3_BUCKET environment variable from
        the account with access key and secret access key environment
        variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, respectively.

        Only use this function if those variables are set.
        """
        return Mailman(bucket).read(s3key)

    @staticmethod
    def s3store(obj, s3key, bucket = Bucket(S3Connection(os.environ.get("AWS_ACCESS_KEY_ID"), os.environ.get("AWS_SECRET_ACCESS_KEY")), os.environ.get("S3_BUCKET"))):
        """
        Store a Python object to a given S3 key. Note that the bucket will by
        default by selected as the S3_BUCKET environment variable from
        the account with access key and secret access key environment
        variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY, respectively.

        Only use this function if those variables are set.
        """
        return Mailman(bucket).store(obj, s3key)


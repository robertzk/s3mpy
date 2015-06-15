from boto.s3.bucket     import Bucket
from boto.s3.connection import S3Connection

class Mailman:

    def __init__(self, conn, bucket):
        """
        Create an S3MPY mailman, responsible for storing an reading Python
        objects from S3 keys
        """

        if type(conn) != S3Connection:
            raise TypeError("Please specify an S3Connection.")

        if type(bucket) == str:
            bucket = Bucket(conn, bucket)

        if type(bucket) != Bucket:
            raise TypeError("Please specify a Bucket object.")

        self._conn   = conn
        self._bucket = bucket

    

#!/usr/bin/env python3
""" 0. Regex-ing
"""

import re
import os
from typing import List
import logging
import mysql.connector

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ to filter the datum
      - '[^{separator}]+' matches while there is not a seperator
    """
    for f in fields:
        message = re.sub(fr'{f}=[^{separator}]+', f' {f}={redaction}', message)
    return message


def get_logger() -> logging.Logger:
    """
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    return mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', default=''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', default='localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME', default='root'))


def main():
    """ main
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    columns = tuple( [d[0] for d in cursor.description] )
    logger = get_logger()

    for user in cursor:
        resultstring = str(zip(columns, user))
        logger.log(logging.INFO, resultstring)


if __name__ == "__main__":
    main()

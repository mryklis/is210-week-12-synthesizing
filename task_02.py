#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom exception class"""


class CustomError(Exception):
    """CustomError subclassed to Exception"""

    def __init__(self, msg, cause):
        """constructor for customerror

        Args:
            msg (str): error message
            cause (str): reason for error

        Returns:
            cause (str): reason for error

        Example:
            >>> myerr = CustomError('whoops!', cause = 'scewed up!')
            >>> print myerr.cause
            scewed up!
        """

        Exception.__init__(self, msg)
        self.cause = cause

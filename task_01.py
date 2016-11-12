#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module declares exception classes"""


class BaseError(Exception):
    """BaseError class extended to Exception"""
    pass


class StringError(BaseError, TypeError):
    """StringError class extended to BaseError and TypeError"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError class extended to BaseError and TypeError"""
    pass


class NonZeroError(NumberError):
    """NonZeroError extended to NumberError"""
    pass

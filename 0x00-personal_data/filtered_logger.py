#!/usr/bin/env python3
"""
Module to filter sensitive data fields in log messages by
obfuscating their values.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate the values of specified fields in a log message.

    Args:
        fields (List[str]): Fields to redact.
        redaction (str): Replacement string.
        message (str): Log message.
        separator (str): Field separator.

    Returns:
        str: Message with redacted fields.
    """
    escaped_sep = re.escape(separator)
    joined_fields = '|'.join(fields)
    pattern = r'({})=([^{sep}]*)'.format(joined_fields, sep=escaped_sep)
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

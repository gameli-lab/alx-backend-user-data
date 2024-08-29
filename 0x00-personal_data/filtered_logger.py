#!/usr/bin/env python3
"""
    Module containing filtered_logger function
"""

import re


def filter_datum(fields: list,
                 redaction: str, message: str, separator: str) -> str:
    """
        Returns the log message obfuscated
    """
    pattern = f'({"|".join([f"{field}=[^{separator}]*"
                            for field in fields])})'
    return re.sub(pattern,
                  lambda m: f'{m.group(0).split("=")[0]}={redaction}', message)

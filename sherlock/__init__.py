"""Sherlock: Hunt down social media accounts by username.

This package provides tools to search for usernames across many social
networks and report the results.
"""

__version__ = "0.15.0"
__author__ = "Sherlock Project"
__license__ = "MIT"

from sherlock.sherlock import sherlock, SherlockFuturesSession

__all__ = ["sherlock", "SherlockFuturesSession", "__version__"]

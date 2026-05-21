"""Sherlock Result Module

This module defines the result types and structures used when checking
usernames across social networks.
"""

from enum import Enum


class QueryStatus(Enum):
    """Represents the status of a username query on a social network."""

    CLAIMED = "Claimed"       # Username is taken/exists on the platform
    AVAILABLE = "Available"   # Username is available/does not exist
    UNKNOWN = "Unknown"       # Could not determine status (e.g., rate limited)
    ILLEGAL = "Illegal"       # Username is not allowed on this platform

    def __str__(self):
        return self.value


class QueryResult:
    """Stores the result of a username query for a single social network.

    Attributes:
        username (str): The username that was queried.
        site_name (str): The name of the social network.
        site_url_user (str): The URL to the user's profile (if it exists).
        status (QueryStatus): The status of the query.
        query_time (float): Time taken for the query in seconds.
        context (str | None): Additional context or error message, if any.
    """

    def __init__(
        self,
        username: str,
        site_name: str,
        site_url_user: str,
        status: QueryStatus,
        query_time: float = 0.0,
        context: str = None,
    ):
        self.username = username
        self.site_name = site_name
        self.site_url_user = site_url_user
        self.status = status
        self.query_time = query_time
        self.context = context

    def __str__(self):
        status_str = str(self.status)
        if self.context:
            return (
                f"[{status_str}] {self.site_name}: {self.site_url_user} "
                f"({self.context})"
            )
        return f"[{status_str}] {self.site_name}: {self.site_url_user}"

    def __repr__(self):
        return (
            f"QueryResult(username={self.username!r}, "
            f"site_name={self.site_name!r}, "
            f"status={self.status!r}, "
            f"query_time={self.query_time:.2f}s)"
        )

    def to_dict(self) -> dict:
        """Serialize the result to a dictionary.

        Returns:
            dict: A dictionary representation of this result.
        """
        return {
            "username": self.username,
            "site_name": self.site_name,
            "site_url_user": self.site_url_user,
            "status": str(self.status),
            "query_time": round(self.query_time, 3),
            "context": self.context,
        }

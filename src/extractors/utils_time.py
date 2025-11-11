from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

ISO_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def utcnow_iso() -> str:
    """
    Return the current UTC time formatted as an ISO 8601 string with 'Z' suffix.
    """
    return datetime.now(timezone.utc).strftime(ISO_FORMAT)

def parse_iso(dt_str: str) -> Optional[datetime]:
    """
    Parse an ISO 8601-like timestamp into a timezone-aware datetime.

    Returns None if parsing fails.
    """
    if not dt_str:
        return None

    try:
        if dt_str.endswith("Z"):
            return datetime.strptime(dt_str, ISO_FORMAT).replace(tzinfo=timezone.utc)

        # Fallback: let fromisoformat try if format slightly differs
        dt = datetime.fromisoformat(dt_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None

def humanize_timedelta(from_dt: datetime, to_dt: Optional[datetime] = None) -> str:
    """
    Return a short human readable difference, e.g. '5m', '2h', '3d'.
    """
    to_dt = to_dt or datetime.now(timezone.utc)
    delta = to_dt - from_dt
    seconds = int(delta.total_seconds())

    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds // 60}m"
    if seconds < 86400:
        return f"{seconds // 3600}h"
    return f"{seconds // 86400}d"
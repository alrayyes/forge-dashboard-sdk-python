from enum import StrEnum

class ActionErrorCode(StrEnum):
    ALREADY_CLOSED = "already_closed"
    ALREADY_MERGED = "already_merged"
    BEHIND = "behind"
    BLOCKED_BY_PROTECTION = "blocked_by_protection"
    CHECKS_FAILING = "checks_failing"
    CHECKS_PENDING = "checks_pending"
    CONFLICT = "conflict"
    NOT_MERGEABLE = "not_mergeable"
    PERMISSION = "permission"
    RATE_LIMITED = "rate_limited"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

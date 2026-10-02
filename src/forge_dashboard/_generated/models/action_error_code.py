from enum import StrEnum

class ActionErrorCode(StrEnum):
    ALREADY_CLOSED = "already_closed"
    ALREADY_MERGED = "already_merged"
    ALREADY_UP_TO_DATE = "already_up_to_date"
    AUTO_MERGE_NOT_ALLOWED = "auto_merge_not_allowed"
    BEHIND = "behind"
    BLOCKED_BY_PROTECTION = "blocked_by_protection"
    CHECKS_FAILING = "checks_failing"
    CHECKS_PENDING = "checks_pending"
    CONFLICT = "conflict"
    NOT_MERGEABLE = "not_mergeable"
    PERMISSION = "permission"
    RATE_LIMITED = "rate_limited"
    READY_TO_MERGE = "ready_to_merge"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

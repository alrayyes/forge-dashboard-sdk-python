from enum import StrEnum

class AllowedActionBlockedCode(StrEnum):
    ALREADY_UP_TO_DATE = "already_up_to_date"
    BEHIND = "behind"
    BLOCKED_BY_PROTECTION = "blocked_by_protection"
    CHECKS_FAILING = "checks_failing"
    CHECKS_PENDING = "checks_pending"
    CONFLICT = "conflict"
    NOT_MERGEABLE = "not_mergeable"
    STACKED = "stacked"

    def __str__(self) -> str:
        return str(self.value)

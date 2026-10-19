from enum import StrEnum

class CheckState(StrEnum):
    AWAITING_APPROVAL = "awaiting_approval"
    CANCELLED = "cancelled"
    FAILURE = "failure"
    QUEUED = "queued"
    RUNNING = "running"
    SKIPPED = "skipped"
    SUCCESS = "success"
    TIMED_OUT = "timed_out"

    def __str__(self) -> str:
        return str(self.value)

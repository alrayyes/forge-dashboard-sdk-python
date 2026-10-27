from enum import StrEnum

class CheckConclusion(StrEnum):
    CANCELLED = "cancelled"
    FAILURE = "failure"
    SKIPPED = "skipped"
    SUCCESS = "success"
    TIMED_OUT = "timed_out"

    def __str__(self) -> str:
        return str(self.value)

from enum import StrEnum

class MainBranchStatus(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    NONE = "none"
    PASSED = "passed"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)

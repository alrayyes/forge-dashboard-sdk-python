from enum import StrEnum

class RateLimitSeverity(StrEnum):
    EXCEEDED = "exceeded"
    LOW = "low"
    OK = "ok"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)

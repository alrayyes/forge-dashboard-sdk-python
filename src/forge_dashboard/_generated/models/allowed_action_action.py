from enum import StrEnum

class AllowedActionAction(StrEnum):
    AUTO_MERGE = "auto_merge"
    CLOSE = "close"
    DEPENDABOT_REBASE = "dependabot_rebase"
    DEPENDABOT_RECREATE = "dependabot_recreate"
    MERGE = "merge"
    RENOVATE_REBASE = "renovate_rebase"
    RERUN_CHECKS = "rerun_checks"
    UPDATE_BRANCH = "update_branch"

    def __str__(self) -> str:
        return str(self.value)

"""Implementation of Rule L060."""

from typing import Optional

from sqlfluff.core.parser.segments.raw import CodeSegment
from sqlfluff.core.rules.base import BaseRule, LintFix, LintResult, RuleContext
from sqlfluff.core.rules.doc_decorators import document_fix_compatible


@document_fix_compatible
class Rule_L060(BaseRule):
    """Use ``COALESCE`` instead of ``IFNULL`` or ``NVL``.

    | **Anti-pattern**
    | ``IFNULL`` or ``NVL`` are used to fill ``NULL`` values.

    .. code-block:: sql

        SELECT ifnull(foo, 0) AS bar,
        FROM baz;

        SELECT nvl(foo, 0) AS bar,
        FROM baz;

    | **Best practice**
    | Use ``COALESCE`` instead.
    | ``COALESCE`` is universally supported,
    | whereas Redshift doesn't support ``IFNULL``
    | and BigQuery doesn't support ``NVL``.
    | Additionally ``COALESCE`` is more flexible
    | and accepts an arbitrary number of arguments.

    .. code-block:: sql

        SELECT coalesce(foo, 0) AS bar,
        FROM baz;

    """

    def _eval(self, context: RuleContext) -> Optional[LintResult]:
        """Use ``COALESCE`` instead of ``IFNULL`` or ``NVL``."""
        # We only care about function names.
        if context.segment.name != "function_name_identifier":
            return None

        # Check if the function is ``IFNULL`` or ``NVL`` and create appropriate fix.
        if context.segment.raw_upper == "IFNULL":
            fix = LintFix.replace(
                context.segment,
                [
                    CodeSegment(
                        raw="COALESCE",
                        name="function_name_identifier",
                        type="function_name_identifier",
                    )
                ],
            )
            return LintResult(anchor=context.segment, fixes=[fix], description="Use 'COALESCE' instead of 'IFNULL'.")
        elif context.segment.raw_upper == "NVL":
            fix = LintFix.replace(
                context.segment,
                [
                    CodeSegment(
                        raw="COALESCE",
                        name="function_name_identifier",
                        type="function_name_identifier",
                    )
                ],
            )
            return LintResult(anchor=context.segment, fixes=[fix], description="Use 'COALESCE' instead of 'NVL'.")
        else:
            return None

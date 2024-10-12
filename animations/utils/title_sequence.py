import manim as mn
from animations.style import color, text
from animations.utils.type_utils import not_none


class TitleSequence:
    """
    Displays a sequence of titles in a step-by-step animation.
    """

    def __init__(
        self, add_numbers: bool = True, default_color: color.Color = color.FOREGROUND
    ) -> None:
        self._add_numbers = add_numbers
        self._default_color = default_color
        self._number = 1

    def reset(self) -> None:
        """
        Resets the class. Allows the same title_sequence to be used across multiple animations.
        """
        self._number = 1

    def next(self, title: str, color: color.Color | None = None) -> mn.Animation:
        """
        Returns an animation which displays the given title (or transitions from the previous title).
        """
        text = self._make_text(title, self._default_color if color is None else color)
        self._number += 1
        if self._number == 2:
            self._first = text
            return not_none(mn.Write(self._first, run_time=0.75))
        else:
            return not_none(mn.Transform(self._first, text, run_time=0.75))

    def _make_text(self, title: str, color: color.Color) -> mn.Text:
        prefix = str(self._number) + ". " if self._add_numbers else ""
        return mn.Text(
            prefix + title, font_size=text.FontSize.LARGE, color=color
        ).to_corner(mn.UP + mn.LEFT)

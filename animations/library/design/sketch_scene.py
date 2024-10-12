from abc import ABC
from typing import Any
import manim as mn

from library.design import sketch
from library.style import animation


class Scene(mn.Scene, ABC):
    """A base class for a scene displaying a sketch."""

    CONSTRAINT_DELAY = 0.5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._static_mobjects: list[sketch.Base] = []

    def introduce(self, *mobjects: sketch.Base):
        """Introduces mobjects to the scene by calling create.

        The mobjects are also scheduled for removal at the end of the scene.
        """
        self._static_mobjects.extend(mobjects)
        self.play(mn.AnimationGroup(
            *[mn.Create(mobject) for mobject in mobjects]))
        self.wait(self.CONSTRAINT_DELAY)

    def run_group(self, *animation: mn.Animation | Any):
        """Runs the given animations in succession with a short delay."""
        self.play(mn.Succession(*animation))
        self.wait(self.CONSTRAINT_DELAY)

    def tear_down(self):
        self.wait(animation.END_DELAY - self.CONSTRAINT_DELAY * 2)

        self.play(
            mn.AnimationGroup(
                *[mn.Uncreate(mobject) for mobject in self._static_mobjects]
            )
        )
        self.wait(self.CONSTRAINT_DELAY * 1.5)

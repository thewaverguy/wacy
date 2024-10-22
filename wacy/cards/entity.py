from typing import List

from h2o_wave import Q, ui
from h2o_wave.ui import Command
from spacy import displacy
from spacy.tokens import Doc

from .base import BaseCard


class EntitySettingsCard(BaseCard):
    """
    Card for handling settings of spaCy's entity visualizer.
    """
    def __init__(
        self,
        name: str = 'entity_settings',
        box: str = 'entity_settings',
        choice_ents: list = None,
        select_ents: list = None,
        title: str = 'Entity Settings',
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            choice_ents: List of entity choices
            select_ents: List of selected entities
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.choice_ents = choice_ents
        self.select_ents = select_ents
        self.title = title
        self.commands = commands

    def to_displacy_options(self):
        """
        Get spaCy displacy's options.

        Returns:
            dict: Dictionary of displacy options
        """
        return {
            'ents': self.select_ents
        }

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        entity_choices = [ui.choice(name=str(x), label=str(x)) for x in self.choice_ents]

        card = ui.form_card(
            box=self.box,
            items=[
                ui.picker(
                    name='select_ents',
                    label='Entities',
                    choices=entity_choices,
                    values=self.select_ents,
                    trigger=True
                )
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card


class EntityVisualizerCard(BaseCard):
    """
    Card for handling visualization of spaCy's entity visualizer.
    """
    def __init__(
        self,
        name: str = 'entity_visualizer',
        box: str = 'entity_visualizer',
        doc: Doc = None,
        options: dict = None,
        title: str = 'Entity Visualizer',
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            doc: spaCy's Doc object of text
            options: Displacy options
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.doc = doc
        self.options = options
        self.title = title
        self.commands = commands

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        dependency_html = displacy.render(self.doc, style='ent', options=self.options)

        card = ui.form_card(
            box=self.box,
            items=[
                ui.text(content=dependency_html)
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card

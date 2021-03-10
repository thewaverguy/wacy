from typing import List

from h2o_wave import Q, ui
from h2o_wave.ui import Command
from spacy.tokens import Doc

from .base import BaseCard
from ..utils import defaults


class TokenAttributesCard(BaseCard):
    """
    Card for handling table of token attributes.
    """
    def __init__(
        self,
        name: str = 'token_attributes',
        box: str = 'token_attributes',
        doc: Doc = None,
        token_attributes: List[str] = None,
        title: str = None,
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            doc: spaCy's Doc object of text
            token_attributes: Token attributes
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.doc = doc
        self.token_attributes = token_attributes if token_attributes is not None else defaults.TOKEN_ATTRIBUTES
        self.title = title
        self.commands = commands

    def get_wave_table_columns(self):
        """
        Get columns for attributes table.

        Returns:
            list: List of Wave table columns
        """
        return [ui.table_column(
            name='token' if x == 'text' else str(x),
            label=str(x),
            sortable=True,
            filterable=True,
            searchable=True if x == 'text' else False,
            link=False
        ) for x in self.token_attributes]

    def get_wave_table_rows(self):
        """
        Get rows for attributes table.

        Returns:
            list: List of Wave table rows
        """
        return [ui.table_row(
            name=str(i),
            cells=[str(getattr(token, attr)) for attr in self.token_attributes]
        ) for i, token in enumerate(self.doc)]

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        card = ui.form_card(
            box=self.box,
            items=[
                ui.table(
                    name='table_tokens',
                    columns=self.get_wave_table_columns(),
                    rows=self.get_wave_table_rows()
                )
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card

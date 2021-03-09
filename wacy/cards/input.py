from typing import List

from h2o_wave import Q, ui
from h2o_wave.ui import Command

from .base import BaseCard
from ..utils import defaults


class InputModelCard(BaseCard):
    """
    Class for handling spaCy model selection.
    """
    def __init__(
        self,
        name: str = 'input_model',
        box: str = 'input_model',
        input_models: List[str] = None,
        input_model: str = defaults.INPUT_MODEL,
        title: str = None,
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            input_models: List of available spaCy models
            input_model: Selected spaCy model
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.input_models = input_models if input_models is not None else defaults.INPUT_MODELS
        self.input_model = input_model
        self.title = title
        self.commands = commands

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        model_choices = [ui.choice(name=str(x), label=str(x)) for x in self.input_models]

        card = ui.form_card(
            box=self.box,
            items=[
                ui.dropdown(
                    name='input_model',
                    label='Select model',
                    value=self.input_model,
                    choices=model_choices,
                    trigger=True
                )
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card


class InputTextCard(BaseCard):
    """
    Class for handling text to analyze.
    """
    def __init__(
        self,
        name: str = 'input_text',
        box: str = 'input_text',
        input_text: str = defaults.INPUT_TEXT,
        title: str = None,
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            input_text: Entered text
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.input_text = input_text
        self.title = title
        self.commands = commands

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        card = ui.form_card(
            box=self.box,
            items=[
                ui.textbox(name='input_text', label='Enter text to analyze', value=self.input_text, multiline=True),
                ui.button(name='analyze_text', label='Analyze', primary=True)
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card

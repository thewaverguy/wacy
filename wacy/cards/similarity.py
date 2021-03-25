from typing import List

from h2o_wave import Q, data, ui
from h2o_wave.ui import Command
from spacy.tokens import Doc

from .base import BaseCard


class SimilaritySettingsCard(BaseCard):
    """
    Card for handling settings of visualizing text similarity.
    """
    def __init__(
        self,
        name: str = 'similarity_settings',
        box: str = 'similarity_settings',
        doc_1: Doc = None,
        doc_2: Doc = None,
        color: str = 'mediumseagreen',
        title: str = 'Similarity Settings',
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            doc_1: spaCy's Doc object of text 1
            doc_2: spaCy's Doc object of text 2
            color: Color of icons
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.doc_1 = doc_1
        self.doc_2 = doc_2
        self.color = color
        self.title = title
        self.commands = commands

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        text_similarity = self.doc_1.similarity(self.doc_2)

        card = ui.form_card(
            box=self.box,
            items=[
                ui.textbox(name='input_text_1', label='Text 1', value=str(self.doc_1), multiline=True),
                ui.textbox(name='input_text_2', label='Text 2', value=str(self.doc_2), multiline=True),
                ui.buttons(
                    items=[
                        ui.button(name='compare_text', label='Compare', primary=True)
                    ]
                ),
                ui.stats(
                    items=[
                        ui.stat(
                            label='Tokens 1',
                            value=f'{len(self.doc_1)}',
                            icon='TextField',
                            icon_color=self.color
                        ),
                        ui.stat(
                            label='Tokens 2',
                            value=f'{len(self.doc_2)}'
                        )
                    ]
                ),
                ui.stats(
                    items=[
                        ui.stat(
                            label='Sentences 1',
                            value=f'{len(list(self.doc_1.sents))}',
                            icon='TextBox',
                            icon_color=self.color
                        ),
                        ui.stat(
                            label='Sentences 2',
                            value=f'{len(list(self.doc_2.sents))}'
                        )
                    ]
                ),
                ui.stats(
                    items=[
                        ui.stat(
                            label='Overall Similarity',
                            value=f'{round(text_similarity * 100)}%',
                            icon='VennDiagram',
                            icon_color=self.color
                        )
                    ]
                )
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card


class SimilarityVisualizerCard(BaseCard):
    """
    Card for handling visualization of text similarity.
    """
    def __init__(
        self,
        name: str = 'similarity_visualizer',
        box: str = 'similarity_visualizer',
        doc_1: Doc = None,
        doc_2: Doc = None,
        color: str = 'mediumseagreen',
        title: str = 'Similarity Visualizer',
        commands: List[Command] = None
    ):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
            doc_1: spaCy's Doc object of text 1
            doc_2: spaCy's Doc object of text 2
            color: Color of plots
            title: Title of card
            commands: Commands of card
        """
        super().__init__(name, box)

        self.doc_1 = doc_1
        self.doc_2 = doc_2
        self.color = color
        self.title = title
        self.commands = commands

    def get_token_similarity_visualization(self):
        """
        Get similarity visualization at token level.

        Returns:
            ui.visualization: Similarity visualization plot
        """
        rows = []

        for token_1 in self.doc_1:
            for token_2 in self.doc_2:
                rows.append((str(token_1), str(token_2), round(float(token_1.similarity(token_2)), 2)))

        return ui.visualization(
            plot=ui.plot([ui.mark(
                type='point',
                x='=token_1',
                y='=token_2',
                size='=similarity',
                shape='circle',
                fill_color=self.color
            )]),
            data=data(
                fields=['token_1', 'token_2', 'similarity'],
                rows=rows,
                pack=True
            )
        )

    def get_sentence_similarity_visualization(self):
        """
        Get similarity visualization at sentence level.

        Returns:
            ui.visualization: Similarity visualization plot
        """
        rows = []

        for sent_1 in self.doc_1.sents:
            for sent_2 in self.doc_2.sents:
                rows.append((str(sent_1), str(sent_2), round(float(sent_1.similarity(sent_2)), 2)))

        return ui.visualization(
            plot=ui.plot([ui.mark(
                type='point',
                x='=sent_1',
                y='=sent_2',
                size='=similarity',
                shape='circle',
                fill_color=self.color
            )]),
            data=data(
                fields=['sent_1', 'sent_2', 'similarity'],
                rows=rows,
                pack=True
            )
        )

    async def render(self, q: Q):
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        card = ui.form_card(
            box=self.box,
            items=[
                ui.label(label='Token Similarity'),
                self.get_token_similarity_visualization(),
                ui.label(label='Sentence Similarity'),
                self.get_sentence_similarity_visualization()
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card

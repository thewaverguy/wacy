from typing import List

import spacy
from spacy import displacy
from h2o_wave import Q, ui
from h2o_wave.ui import Command

from .base import BaseCard


class DependencySettingsCard(BaseCard):
    def __init__(
        self,
        name: str = 'dependency_settings',
        box: str = 'dependency_settings',
        fine_grained: bool = False,
        add_lemma: bool = False,
        collapse_punct: bool = True,
        collapse_phrases: bool = False,
        compact: bool = False,
        color: str = 'green',
        bg: str = 'white',
        font: str = 'Arial',
        offset_x: int = 50,
        arrow_stroke: int = 2,
        arrow_width: int = 9,
        arrow_spacing: int = 11,
        word_spacing: int = 45,
        word_distance: int = 175,
        title: str = 'Dependency Settings',
        commands: List[Command] = None
    ):
        super().__init__(name, box)

        self.fine_grained = fine_grained
        self.add_lemma = add_lemma
        self.collapse_punct = collapse_punct
        self.collapse_phrases = collapse_phrases
        self.compact = compact
        self.color = color
        self.bg = bg
        self.font = font
        self.offset_x = offset_x
        self.arrow_stroke = arrow_stroke
        self.arrow_width = arrow_width
        self.arrow_spacing = arrow_spacing
        self.word_spacing = word_spacing
        self.word_distance = word_distance
        self.title = title
        self.commands = commands

    def to_displacy_options(self):
        return {
            'fine_grained': self.fine_grained,
            'add_lemma': self.add_lemma,
            'collapse_punct': self.collapse_punct,
            'collapse_phrases': self.collapse_phrases,
            'compact': self.compact,
            'color': self.color,
            'bg': self.bg,
            'font': self.font,
            'offset_x': self.offset_x,
            'arrow_stroke': self.arrow_stroke,
            'arrow_width': self.arrow_width,
            'arrow_spacing': self.arrow_spacing,
            'word_spacing': self.word_spacing,
            'word_distance': self.word_distance
        }

    async def render(self, q: Q):
        card = ui.form_card(
            box=self.box,
            items=[
                ui.toggle(name='fine_grained', label='Fine Grained', value=self.fine_grained, trigger=True),
                ui.toggle(name='add_lemma', label='Add Lemma', value=self.add_lemma, trigger=True),
                ui.toggle(name='collapse_punct', label='Merge Punctuation', value=self.collapse_punct, trigger=True),
                ui.toggle(name='collapse_phrases', label='Merge Phrases', value=self.collapse_phrases, trigger=True),
                ui.toggle(name='compact', label='Compact', value=self.compact, trigger=True),
                ui.inline(items=[
                    ui.textbox(name='color', label='Visualizer Color', value=self.color, trigger=True),
                    ui.textbox(name='bg', label='Background Color', value=self.bg, trigger=True)
                ]),
                ui.inline(items=[
                    ui.textbox(name='font', label='Font', value=self.font, trigger=True),
                    ui.textbox(name='offset_x', label='Offset-X', value=str(self.offset_x), trigger=True)
                ]),
                ui.inline(items=[
                    ui.textbox(
                        name='arrow_stroke',
                        label='Arrow Stroke',
                        value=str(self.arrow_stroke),
                        suffix='px',
                        trigger=True
                    ),
                    ui.textbox(
                        name='arrow_width',
                        label='Arrow Width',
                        value=str(self.arrow_width),
                        suffix='px',
                        trigger=True
                    ),
                    ui.textbox(
                        name='arrow_spacing',
                        label='Arrow Spacing',
                        value=str(self.arrow_spacing),
                        suffix='px',
                        trigger=True
                    )
                ]),
                ui.inline(items=[
                    ui.textbox(
                        name='word_spacing',
                        label='Word Spacing',
                        value=str(self.word_spacing),
                        suffix='px',
                        trigger=True
                    ),
                    ui.textbox(
                        name='word_distance',
                        label='Word Distance',
                        value=str(self.word_distance),
                        suffix='px',
                        trigger=True
                    )
                ])
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card


class DependencyVisualizerCard(BaseCard):
    def __init__(
        self,
        name: str = 'dependency_visualizer',
        box: str = 'dependency_visualizer',
        doc: spacy.tokens.Doc = None,
        options: dict = None,
        title: str = 'Dependency Visualizer',
        commands: List[Command] = None
    ):
        super().__init__(name, box)

        self.doc = doc
        self.options = options
        self.title = title
        self.commands = commands

    async def render(self, q: Q):
        dependency_html = displacy.render(self.doc, style='dep', options=self.options)

        card = ui.form_card(
            box=self.box,
            items=[
                ui.text(content=dependency_html)
            ],
            title=self.title,
            commands=self.commands
        )

        q.page[self.name] = card

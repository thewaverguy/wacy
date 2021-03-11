from h2o_wave import Q, ui, copy_expando
from spacy import load as spacyload

from ...cards import (
    InputModelCard, InputTextCard,
    EntitySettingsCard, EntityVisualizerCard,
    DependencySettingsCard, DependencyVisualizerCard,
    TokenAttributesCard
)
from ...utils import defaults


class BaseApp:
    _META_CARD = defaults.META_CARD
    _HEADER_CARD = defaults.HEADER_CARD
    _FOOTER_CARD = defaults.FOOTER_CARD
    _INPUT_MODEL_CARD = InputModelCard()
    _INPUT_TEXT_CARD = InputTextCard()
    _ENTITY_SETTINGS_CARD = EntitySettingsCard()
    _ENTITY_VISUALIZER_CARD = EntityVisualizerCard()
    _DEPENDENCY_SETTINGS_CARD = DependencySettingsCard()
    _DEPENDENCY_VISUALIZER_CARD = DependencyVisualizerCard()
    _TOKEN_ATTRIBUTES_CARD = TokenAttributesCard()

    def __init__(
        self,
        meta_card: ui.MetaCard = None,
        header_card: ui.HeaderCard = None,
        footer_card: ui.FooterCard = None,
        input_model_card: InputModelCard = None,
        input_text_card: InputTextCard = None,
        entity_settings_card: EntitySettingsCard = None,
        entity_visualizer_card: EntityVisualizerCard = None,
        dependency_settings_card: DependencySettingsCard = None,
        dependency_visualizer_card: DependencyVisualizerCard = None,
        token_attributes_card: TokenAttributesCard = None
    ):
        self.meta_card = meta_card if meta_card is not None else self._META_CARD
        self.header_card = header_card if header_card is not None else self._HEADER_CARD
        self.footer_card = footer_card if footer_card is not None else self._FOOTER_CARD
        self.input_model_card = input_model_card if input_model_card is not None else self._INPUT_MODEL_CARD
        self.input_text_card = input_text_card if input_text_card is not None else self._INPUT_TEXT_CARD
        self.entity_settings_card = entity_settings_card if entity_settings_card is not None else \
            self._ENTITY_SETTINGS_CARD
        self.entity_visualizer_card = entity_visualizer_card if entity_visualizer_card is not None else \
            self._ENTITY_VISUALIZER_CARD
        self.dependency_settings_card = dependency_settings_card if dependency_settings_card is not None else \
            self._DEPENDENCY_SETTINGS_CARD
        self.dependency_visualizer_card = dependency_visualizer_card if dependency_visualizer_card is not None else \
            self._DEPENDENCY_VISUALIZER_CARD
        self.token_attributes_card = token_attributes_card if token_attributes_card is not None else \
            self._TOKEN_ATTRIBUTES_CARD

    async def serve(self, q: Q) -> None:
        if not q.client.client_initialized:
            await self._initialize_client(q)
            q.client.client_initialized = True
        elif q.args.input_model:
            copy_expando(q.args, q.client)
            await self._load_model(q)
            await self._process_text(q)
            await self._update_all_cards(q)
        elif q.args.analyze_text:
            copy_expando(q.args, q.client)
            await self._process_text(q)
            await self._update_all_cards(q)
        elif q.args.select_ents:
            copy_expando(q.args, q.client)
            await self._update_entity_cards(q)
        elif any([q.args.fine_grained, q.args.add_lemma, q.args.collapse_punct, q.args.collapse_phrases,
                  q.args.compact, q.args.color, q.args.bg, q.args.font, q.args.offset_x, q.args.arrow_stroke,
                  q.args.arrow_width, q.args.arrow_spacing, q.args.word_spacing, q.args.word_distance]):
            copy_expando(q.args, q.client)
            await self._update_dependency_cards(q)

    async def _initialize_client(self, q: Q):
        q.client.input_models = self.input_model_card.input_models
        q.client.input_model = self.input_model_card.input_model

        await self._load_model(q)

        q.client.input_text = self.input_text_card.input_text

        await self._process_text(q)

        q.page['meta'] = self.meta_card
        q.page['header'] = self.header_card
        q.page['footer'] = self.footer_card

        q.client.select_ents = list(q.client.model.get_pipe('ner').labels)

        q.client.fine_grained = self.dependency_settings_card.fine_grained
        q.client.add_lemma = self.dependency_settings_card.add_lemma
        q.client.collapse_punct = self.dependency_settings_card.collapse_punct
        q.client.collapse_phrases = self.dependency_settings_card.collapse_phrases
        q.client.compact = self.dependency_settings_card.compact
        q.client.color = self.dependency_settings_card.color
        q.client.bg = self.dependency_settings_card.bg
        q.client.font = self.dependency_settings_card.font
        q.client.offset_x = self.dependency_settings_card.offset_x
        q.client.arrow_stroke = self.dependency_settings_card.arrow_stroke
        q.client.arrow_width = self.dependency_settings_card.arrow_width
        q.client.arrow_spacing = self.dependency_settings_card.arrow_spacing
        q.client.word_spacing = self.dependency_settings_card.word_spacing
        q.client.word_distance = self.dependency_settings_card.word_distance

        await self._update_all_cards(q)

    @staticmethod
    async def _load_model(q: Q):
        q.client.model = spacyload(q.client.input_model)

    @staticmethod
    async def _process_text(q: Q):
        q.client.doc = q.client.model(q.client.input_text)

    async def _update_all_cards(self, q: Q):
        await self._update_input_cards(q)
        await self._update_entity_cards(q)
        await self._update_dependency_cards(q)
        await self._update_token_cards(q)

        await q.page.save()

    async def _update_input_cards(self, q: Q):
        self.input_model_card.input_model = q.client.input_model
        await self.input_model_card.render(q)

        self.input_text_card.input_text = q.client.input_text
        await self.input_text_card.render(q)

    async def _update_entity_cards(self, q: Q):
        self.entity_settings_card.choice_ents = list(q.client.model.get_pipe('ner').labels)
        self.entity_settings_card.select_ents = q.client.select_ents
        await self.entity_settings_card.render(q)

        self.entity_visualizer_card.doc = q.client.doc
        self.entity_visualizer_card.options = self.entity_settings_card.to_displacy_options()
        await self.entity_visualizer_card.render(q)

    async def _update_dependency_cards(self, q: Q):
        self.dependency_settings_card.fine_grained = q.client.fine_grained
        self.dependency_settings_card.add_lemma = q.client.add_lemma
        self.dependency_settings_card.collapse_punct = q.client.collapse_punct
        self.dependency_settings_card.collapse_phrases = q.client.collapse_phrases
        self.dependency_settings_card.compact = q.client.compact
        self.dependency_settings_card.color = q.client.color
        self.dependency_settings_card.bg = q.client.bg
        self.dependency_settings_card.font = q.client.font
        self.dependency_settings_card.offset_x = int(q.client.offset_x)
        self.dependency_settings_card.arrow_stroke = int(q.client.arrow_stroke)
        self.dependency_settings_card.arrow_width = int(q.client.arrow_width)
        self.dependency_settings_card.arrow_spacing = int(q.client.arrow_spacing)
        self.dependency_settings_card.word_spacing = int(q.client.word_spacing)
        self.dependency_settings_card.word_distance = int(q.client.word_distance)
        await self.dependency_settings_card.render(q)

        self.dependency_visualizer_card.doc = q.client.doc
        self.dependency_visualizer_card.options = self.dependency_settings_card.to_displacy_options()
        await self.dependency_visualizer_card.render(q)

    async def _update_token_cards(self, q: Q):
        self.token_attributes_card.doc = q.client.doc
        await self.token_attributes_card.render(q)

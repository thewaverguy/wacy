from h2o_wave import Q, ui


class BaseCard(object):
    """
    Base class for WaCy cards.
    """
    def __init__(self, name: str, box: str):
        """
        Class initialization.

        Args:
            name: Name of card
            box: Box of card
        """
        self.name = name
        self.box = box

    async def render(self, q: Q) -> None:
        """
        Render card in Wave.

        Args:
            q: Wave server
        """
        q.page[self.name] = ui.form_card(box=self.box, items=[])

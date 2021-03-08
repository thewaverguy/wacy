from h2o_wave import Q, ui


class BaseCard(object):
    def __init__(self, name, box):
        self.name = name
        self.box = box

    async def render(self, q: Q):
        q.page[self.name] = ui.form_card(box=self.box, items=[])

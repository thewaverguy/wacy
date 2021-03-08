from h2o_wave import Q, main, app

from wacy.apps import BaseApp

wacy_app = BaseApp()


@app('/wacy')
async def serve(q: Q) -> None:
    """
    App's serving function.

    Args:
        q: Wave server query
    """
    await wacy_app.serve(q)

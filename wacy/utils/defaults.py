from h2o_wave import ui

INPUT_MODELS = ['en_core_web_sm', 'en_core_web_md']
INPUT_MODEL = 'en_core_web_sm'
INPUT_TEXT = 'Matthew Honnibal and Ines Montani are the founders of Explosion'

META_CARD = ui.meta_card(
    box='',
    title='WaCy',
    layouts=[
        ui.layout(
            breakpoint='xs',
            zones=[
                ui.zone(name='header'),
                ui.zone(name='main', zones=[
                    ui.zone(name='input_row', direction='row', zones=[
                        ui.zone(name='input_model', size='30%'),
                        ui.zone(name='input_text', size='70%')
                    ]),
                    ui.zone(name='dependency_row', direction='row', zones=[
                        ui.zone(name='dependency_settings', size='30%'),
                        ui.zone(name='dependency_visualizer', size='70%')
                    ]),
                    ui.zone(name='entity_row', direction='row', zones=[
                        ui.zone(name='entity_settings', size='30%'),
                        ui.zone(name='entity_visualizer', size='70%')
                    ])
                ]),
                ui.zone(name='footer')
            ]
        )
    ]
)

HEADER_CARD = ui.header_card(
    box='header',
    title='WaCy',
    subtitle='Powering spaCy with Wave',
    icon='WavingHand'
)

FOOTER_CARD = ui.footer_card(
    box='footer',
    caption='(c) 2021 <b>TheWaverGuy</b> - <i>Data is bulletproof</i>'
)

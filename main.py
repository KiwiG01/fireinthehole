from ursina import *

app = Ursina(title="fire in da hole", icon="fith.ico")

window.exit_button.disable()
window.fps_counter.disable()
window.entity_counter.disable()
window.collider_counter.disable()

app.run()
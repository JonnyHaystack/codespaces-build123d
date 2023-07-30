#%%
from build123d import *
from ocp_vscode import show_all, show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)

#%%

with BuildPart() as p:
    with BuildSketch() as p_sk:
        Rectangle(5, 5)
    extrude(amount=5)

show_all()

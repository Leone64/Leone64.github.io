import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.io import fits

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from dustmaps.edenhofer2023 import Edenhofer2023Query
import dustmaps.edenhofer2023

import sys
sys.path.append("/home/leone/Documents/Uni/Bachelor/Project/")
import FuncDef as fd
from importlib import reload
reload(fd)

import itertools

from jinja2 import Template


#savefolder = "../PlotlyTesting/savedplots/website/"

data = fd.load_data("cloud-data.csv")
FACTOR = 1653

xrange = [-1250, 1250]
yrange = [-1250, 1250]
zrange = [-625, 625]
xf = np.arange(xrange[0], xrange[1], 17)
yf = np.arange(xrange[0], xrange[1], 17)
zf = np.arange(xrange[0], xrange[1], 17)
print(len(xf)*len(yf)*len(zf))

xf, yf, zf = np.meshgrid(xf, yf, zf)

dust_dist = fd.query_region(xf, yf, zf)


dust_vol = go.Volume(
    x=xf.flatten(),
    y=yf.flatten(),
    z=zf.flatten(),
    value=dust_dist,
    isomin=2e-4,
    isomax=1e-2,
    opacity=0.15,
    opacityscale=[[0, 0.4], [1,0.75]],
    surface_count=10,
    colorscale="Greys",
    showscale=False,
    visible=True,
    name = "E+ [E]",
    showlegend=True,
)

sun = go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    mode="markers",
    marker=dict(
        size=2,
        color="yellow"
    ),
    name = "Sun",
    showlegend=True,
)

xscale = (xrange[1] - xrange[0]) / (zrange[1] - zrange[0])
yscale = (yrange[1] - yrange[0]) / (zrange[1] - zrange[0])

layout = go.Layout(
    template="plotly_white",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    scene=dict(
        aspectmode="manual",
        aspectratio=dict(x=xscale, y=yscale, z=1),
        xaxis=dict(range=xrange, title=dict(text="X [pc]", font_size=30)),
        yaxis=dict(range=yrange, title=dict(text="Y [pc]", font_size=30)),
        zaxis=dict(range=zrange, title=dict(text="Z [pc]", font_size=30)),
        #camera=dict(
        #    up=dict(x=0, y=1, z=0),
        #    eye=dict(x=0, y=0, z=3.7),
        #),
    ),
    width= 1000,
    height=1000,
    font=dict(
        size=14,
        color="black",
    ),
)

fig = go.Figure(data=[sun], layout=layout)
#fig["data"][0]["showlegend"] = False
fig.add_trace(dust_vol)


output_path = r"dust.md"
template_path = r"plot_blank.md"


plotly_jinja_data = {"fig": fig.to_html(include_plotlyjs = "cdn", full_html=False)}

with open(output_path, "w", encoding="utf-8") as output_file:
    with open(template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))
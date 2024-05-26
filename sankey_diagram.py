import plotly.graph_objects as go
import urllib, json
import urllib.request
import streamlit as st                                           

st.title("Pakistan Energy Balance")

#st.subheader("#RethinkingIndus")

data ={
    "data": [
        {
            "type": "sankey",
            "domain": {
                "x": [
                    0,
                    1
                ],
                "y": [
                    0,
                    1
                ]
            },
            "orientation": "h",
            "valueformat": ".3f",
            "valuesuffix": "MTOe",
            "node": {
                "pad": 15,
                "thickness": 15,
                "line": {
                    "color": "black",
                    "width": 0.5
                },
                "label": [
                    "Oil Prod",
                    "Oil Imp",
                    "Oil Product Imp",
                    "Coal prod",
                    "Coal imp",
                    "Bio/waste Prod",
                    "Electricity imp",
                    "solar/wind",
                    "Hydro",
                    "Nuclear prod",
                    "Refineries",
                    "Other transformation",
                    "Power Station",
                    "Power Loses",
                    "Exports",
                    "Bunkers",
                    "Own use",
                    "Industry",
                    "Transport",
                    "Other",
                    "Non-energy",
                    "Gas Prod",
                    "Gas imp",
                    "Total Oil",
                    "Total Coal",
                    "Total Gas",
                    "Total Electricity"              
                      ],
                "color": [
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(0, 128, 0, 0.5)",         #bio/waste
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(0, 0, 128, 0.8)", #hydro
                    "rgba(23, 190, 207, 0.8)",
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(207, 0, 15, 1)", #powerlosses
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",]
            },
            "link": {
                "source": [
                    0,1,2,10,23,23,23,23,23,23,23,23,
                    21,22,25,25,25,25,25,25,
                    3,4,24,24,
                    5,5,5,
                    8,7,9,
                    6,12,
                    12,
                   26,26,26

                ],
                "target": [
                    10,10,23,23,12,17,18,19,20,14,15,16,
                    25,25,12,17,18,19,20,16,
                    24,24,17,12,
                    12,17,19
                    ,12,12,12
                    ,26,26
                    ,13,
                   16,17,19
                    
                   
                ],
                "value": [
                   4.29,
6.284,
10.17,
9.55,
2.87,
1.23,
14.17,
1.42,
0.29,
0.33,
0.29,
0.27,
21.32,
7.73,
7.7,
5.67,
1.03,
7.98,
3.8,
0.13,
3.18,
10.17,
6.95,
6.32,
0.24,
4.07,
32.58,
2.92,
0.32,
3,
2.2,
11.46,
11.94,
0.23,
2.2,
7.06,

                    
                    ],
                "color": [
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)"
                    ,
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)",
                    "rgba(0,0,96,0.2)"
                ],
                "label": [
                    "stream 1",
                    "",
                    "",
                    "",
                    "stream 1",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ]
            }
        }],
    "layout": {
        "title": {"text": "Energy forecast for 2050, UK — Department of Energy & Climate Change<br>Imperfect copy of <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock's example</a><br>with numerous <a href='https://plotly.com/javascript/'>Plotly</a> features"},
        "width": 1118,
        "height": 772,
        "font": {
            "size": 10
        },
        "updatemenus": [
            {
                "y": 1,
                "buttons": [
                    {
                        "label": "Light",
                        "method": "relayout",
                        "args": [ "paper_bgcolor", "white" ]
                    },
                    {
                        "label": "Dark",
                        "method": "relayout",
                        "args": [ "paper_bgcolor", "black"]
                    }
                ]
            },
            {
                "y": 0.9,
                "buttons": [
                    {
                        "label": "Thick",
                        "method": "restyle",
                        "args": [ "node.thickness", 15 ]
                    },
                    {
                        "label": "Thin",
                        "method": "restyle",
                        "args": [ "node.thickness", 8]
                    }
                ]
            },
            {
                "y": 0.8,
                "buttons": [
                    {
                        "label": "Small gap",
                        "method": "restyle",
                        "args": [ "node.pad", 15 ]
                    },
                    {
                        "label": "Large gap",
                        "method": "restyle",
                        "args": [ "node.pad", 20]
                    }
                ]
            },
            {
                "y": 0.7,
                "buttons": [
                    {
                        "label": "Snap",
                        "method": "restyle",
                        "args": [ "arrangement", "snap" ]
                    },
                    {
                        "label": "Perpendicular",
                        "method": "restyle",
                        "args": [ "arrangement", "perpendicular"]
                    },
                    {
                        "label": "Freeform",
                        "method": "restyle",
                        "args": [ "arrangement", "freeform"]
                    },
                    {
                        "label": "Fixed",
                        "method": "restyle",
                        "args": [ "arrangement", "fixed"]
                    }
                ]
            },
            {
                "y": 0.6,
                "buttons": [
                    {
                        "label": "Horizontal",
                        "method": "restyle",
                        "args": [ "orientation", "h" ]
                    },
                    {
                        "label": "Vertical",
                        "method": "restyle",
                        "args": [ "orientation", "v"]
                    }
                ]
            }
        ]
    }
}
# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat = ".3f",
    valuesuffix = "Mtoe",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])

#fig.update_layout(title_text="Pakistan Energy Balance 2020",
#                  font_size=10)
st.write(fig)
#fig.show()
#fig.write_html("energy_flows.html")
#st.image("logo.png", width=100)
st.markdown("Developed by Haris Mushtaq")
st.text("")

#!/usr/bin/env python

import streamlit as st
import json

chips = ["NREGA ASSETS: Land restoration",
    "NREGA ASSETS: Off-farm livelihood assets",
    "NREGA ASSETS: Irrigation farms",
    "NREGA ASSETS: Plantations",
    "NREGA ASSETS: Soil and Water Conservation",
    "NREGA ASSETS: Community assets",
    "NREGA ASSETS: Unidentified",
    "Admin Boundaries",
    "LULC",
    "CLART",
    "Surface Water Bodies",
    "Settlement Layer",
    "Well",
    "Drainage Lines",
    "Well Depth",
    "MWS Fortnightly",
    "Recharge Structure Layer",
    "Irrigation Works Layer",
    "Water Structure: Farm Pond",
    "Water Structures: Percolation Tank",
    "Water Structures: Canal",
    "Water Structures: Check Dam",
    "Water Structures: Gully plugs",
    "Water Structures: Drainage/Soakage Channels",
    "Water Structures: Recharge pits",
    "Water Structures: Soakage pits",
    "Water Structures: Trench cum bund"
]

columns = ["Home Screen",
    "Groundwater",
    "Surface Waterbodies",
    "Agriculture",
    "Livelihood",
    "Resource Mapping"
]

@st.cache_resource
def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {
            "selected_chips": chips,
            "column_chips": {column: [] for column in columns}
        }
    except json.JSONDecodeError:
        data = {
            "selected_chips": chips,
            "column_chips": {column: [] for column in columns}
        }
    return data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

data = load_data()


def render_chips():
    data["selected_chips"] = st.multiselect("Available Layers", chips, default=data["selected_chips"], key="chip_multiselect")

def render_columns():
    for column in columns:
        selected_column_chips = st.multiselect(f"Select layers for {column}:", data["selected_chips"], default=data["column_chips"][column], key=f"column_selectbox_{column}")
        data["column_chips"][column] = selected_column_chips

    for column, chips in data["column_chips"].items():
        st.subheader(column)
        for chip in chips:
            st.write(f"- {chip}")

def main():
    st.title("Assign Layers to respective screens")

    # Render the chips
    render_chips()
    render_columns()
    save_data(data)

if __name__ == "__main__":
    main()

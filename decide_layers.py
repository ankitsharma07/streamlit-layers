#!/usr/bin/env python

import streamlit as st

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


def render_chips():
    selected_chips = st.multiselect("Available Layers", chips, default=chips, key="chip_multiselect")
    return selected_chips


def render_columns(selected_chips):
    column_chips = {column: [] for column in columns}

    for column in columns:
        selected_column_chips = st.multiselect(f"Select layers for {column}:", selected_chips, key=f"column_selectbox_{column}")
        column_chips[column] = selected_column_chips
        
    for column, chips in column_chips.items():
        st.subheader(column)
        for chip in chips:
            st.write(f"- {chip}")

def main():
    st.title("Assign Layers to respective screens")

    # Render the chips
    selected_chips = render_chips()

    # Render the columns
    column_width = 1.0 / len(columns)  # Calculate the width of each column
    column_containers = []

    for column in columns:
        column_container = st.expander(column, expanded=True)
        column_containers.append(column_container)

    # Render the column contents
    for column, column_container in zip(columns, column_containers):
        with column_container:
            selected_column_chips = st.multiselect(f"Select layers for {column}:", selected_chips, key=f"column_multiselect_{column}")
            for chip in selected_column_chips:
                st.write(f"- {chip}")


if __name__ == "__main__":
    main()

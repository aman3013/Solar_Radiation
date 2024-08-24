import streamlit as st

def report():
    st.title("Solar Energy Analysis Report")
    st.write("This report provides an overview of the solar energy potential in Benin, Sierra Leone, and Togo.")

    tab1, tab2, tab3 = st.tabs(["Introduction", "Methodology", "Recommendation"])

    with tab1:
        st.write("## Introduction")
        st.write("The goal of this analysis is to compare the solar energy potential in Benin, Sierra Leone, and Togo. The analysis focuses on the Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI) values for each location.")

    with tab2:
        st.write("## Methodology")
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Data Analysis Steps")
            st.write("* Loaded historical climate data for each location")
            st.write("* Calculated mean GHI, DNI, and DHI values for each location")
            st.write("* Resampled data to daily intervals")
        with col2:
            st.write("### Visualization Tools")
            st.write("* Used bar charts to compare mean GHI, DNI, and DHI values across locations")
            st.write("* Used line plots to visualize daily mean GHI, DNI, and DHI values over time")

    with tab3:
        st.write("## Recommendation")
        st.write("Based on the analysis, the following conclusions can be drawn:")
        st.write("### GHI (Global Horizontal Irradiance)")
        st.write("* Benin (Malanville) has the highest average GHI (240.56 W/m²), followed closely by Togo (Dapaong) (230.56 W/m²).")
        st.write("* Sierra Leone (Bumbuna) has the lowest average GHI (201.96 W/m²).")
        st.write("### DNI (Direct Normal Irradiance)")
        st.write("* Benin (Malanville) again has the highest average DNI (167.19 W/m²), with Togo (Dapaong) being the second highest (151.26 W/m²).")
        st.write("* Sierra Leone (Bumbuna) has the lowest average DNI (116.38 W/m²).")
        st.write("### Conclusion")
        st.write("* Benin (Malanville) appears to be the best suited for solar radiation selection, with the highest mean values for both GHI and DNI, which are crucial for solar power generation.")
        st.write("* Togo (Dapaong) is also a strong candidate, with only slightly lower solar radiation values.")
        st.write("* Sierra Leone (Bumbuna), while still viable, has the lowest mean values for both GHI and DNI, making it less favorable compared to the other two locations.")

report()
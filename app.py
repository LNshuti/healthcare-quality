import streamlit as st 
import pandas as pd

def main():
    st.set_page_config(layout="wide")
    st.title('**Healthcare Quality Measures** between hospitals and across states in the United States')

    st.write(
        '''
        We track the following six measures of healthcare quality : 

        1. Mortality - Death rate for heart attack patients
        2. Safety of Care - Serious complications
        3. Readmission - 30-day readmission rate for heart attack patients
        4. Patient Experience - Patient experience survey results
        5. Effectiveness of Care - Timeliness of care for heart attack patients
        6. Timeliness of Care - Timeliness of care for heart attack patients
        '''
    )

    # Read data
    data = pd.read_csv('data/Hospital_Service_Area_2021.csv')

    # Display data
    st.dataframe(data)

    # Add selectbox for the measures
    # measures = [
    #     'Mortality', 
    #     'Safety of Care', 
    #     'Readmission', 
    #     'Patient Experience', 
    #     'Effectiveness of Care',
    #     'Timeliness of Care'
    # ]
    # measure = st.selectbox("Select a measure to view:", measures)

    # # Filter data based on selected measure
    # filtered_data = data[data['Measure'] == measure]

    # # Display filtered data
    # st.dataframe(filtered_data)

if __name__ == "__main__":
    main()

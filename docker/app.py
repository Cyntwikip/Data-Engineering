import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Height-Weight Visualizer")

# Description of the data source
st.write("""
This app visualizes data from a public S3 bucket containing height and weight measurements. 
The dataset is sourced from [FSU's public datasets](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv) 
and includes 200 samples of height (in inches) and weight (in pounds).
""")

# Public S3 bucket URL (example: a CSV file)
S3_URL = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

# Load the data from the S3 bucket
@st.cache_data
def load_data(url):
    """Fetch data from a public S3 bucket and preprocess it."""
    try:
        # Load the data
        data = pd.read_csv(url)
        
        # Preprocess: Trim quotes from column names
        data.columns = data.columns.str.strip().str.replace('"', '').str.replace("'", "")
        
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Display the data
st.write("Fetching data from the public S3 bucket...")
data = load_data(S3_URL)

if data is not None:
    # Data Preview and Data Summary in two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Data Preview")
        st.dataframe(data)

    with col2:
        st.write("### Data Summary")
        st.write(data.describe())

    # Visualization: Histogram
    st.write("### Visualization: Histogram")
    numeric_columns = data.select_dtypes(include=['float', 'int']).columns
    numeric_columns = [col for col in numeric_columns if col != 'Index']  # Exclude index column
    column_to_plot = st.selectbox("Select a column for the histogram:", numeric_columns)
    if column_to_plot:
        fig, ax = plt.subplots()
        ax.hist(data[column_to_plot], bins=20, color='skyblue', edgecolor='black')
        ax.set_title(f"Histogram of {column_to_plot}")
        ax.set_xlabel(column_to_plot)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Visualization: Scatter Plot
    st.write("### Visualization: Scatter Plot")
    default_x = "Weight" if "Weight" in numeric_columns else numeric_columns[0]
    default_y = "Height" if "Height" in numeric_columns else numeric_columns[1]
    x_axis = st.selectbox("Select X-axis:", numeric_columns, index=numeric_columns.index(default_x))
    y_axis = st.selectbox("Select Y-axis:", numeric_columns, index=numeric_columns.index(default_y))
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis], alpha=0.7, color='green')
        ax.set_title(f"Scatter Plot of {y_axis} vs {x_axis}")
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)
else:
    st.error("Failed to load data. Please check the S3 URL.")
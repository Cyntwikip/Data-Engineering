## Introduction to Streamlit
Streamlit is an open-source Python library that allows you to create interactive web applications for data visualization and machine learning. It is designed to be simple and intuitive, enabling developers to turn Python scripts into shareable web apps with minimal effort.

This guide is based on the official Streamlit tutorial: [https://docs.streamlit.io/get-started/tutorials/create-an-app](https://docs.streamlit.io/get-started/tutorials/create-an-app).

### Key Features of Streamlit:
- **Interactive Widgets**: Add sliders, checkboxes, buttons, and more to your app.
- **Live Updates**: Automatically updates the app when the script changes.
- **Caching**: Optimize performance by caching expensive computations.

## How to Run

1. **Install Streamlit**  
   If you don't already have Streamlit installed, you can install it using pip:
   ```bash
   pip install streamlit
   ```

2. **Save the Code**  
   Save the provided code snippet in a file named `app.py` or `uber_pickups.py`.

3. **Run the App**  
   Open a terminal, navigate to the directory containing the file, and run:
   ```bash
   streamlit run uber_pickups.py
   ```

4. **Open in Browser**  
   The app will open in your default web browser. If it doesn't, copy and paste the URL displayed in the terminal (e.g., `http://localhost:8501`) into your browser.

## Streamlit Basics in the Code

### 1. **Title**
```python
st.title('Uber pickups in NYC')
```
Displays the title of the app at the top of the page.

### 2. **Caching**
```python
@st.cache_data
def load_data(nrows):
    ...
```
The `@st.cache_data` decorator caches the output of the `load_data` function, ensuring that the data is not reloaded unnecessarily, improving performance.

### 3. **Interactive Widgets**
```python
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
```
- A checkbox allows users to toggle the display of raw data.
- If checked, the raw dataset is displayed in a table format.

### 4. **Loading State**
```python
data_load_state = st.text('Loading data...')
data_load_state.text("Done! (using st.cache_data)")
```
Displays a loading message while the data is being processed and updates it once the data is ready.

## Summary
This app demonstrates the basics of Streamlit, including adding a title, caching data, and using interactive widgets. It loads and displays Uber pickup data for NYC, providing a simple yet powerful example of what Streamlit can do.
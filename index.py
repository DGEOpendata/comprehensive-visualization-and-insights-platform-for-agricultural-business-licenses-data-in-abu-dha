python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
datafile = 'Agricultural_and_Livestock_Business_Licenses.xlsx'
df = pd.read_excel(datafile)

# Data preprocessing: Convert dates and clean up columns
df['Establishment Date'] = pd.to_datetime(df['Establishment Date'])
df['Issuance Date'] = pd.to_datetime(df['Issuance Date'])
df['Expiry Date'] = pd.to_datetime(df['Expiry Date'])

# Generate a bar chart for license types
license_type_data = df['License Type'].value_counts()
fig_license_type = px.bar(
    x=license_type_data.index,
    y=license_type_data.values,
    labels={'x': 'License Type', 'y': 'Number of Licenses'},
    title='Distribution of License Types'
)
fig_license_type.show()

# Generate a time series chart for license issuance over time
issuance_trend = df.groupby(df['Issuance Date'].dt.to_period('M')).size()
fig_issuance_trend = go.Figure()
fig_issuance_trend.add_trace(go.Scatter(
    x=issuance_trend.index.to_timestamp(),
    y=issuance_trend.values,
    mode='lines+markers',
    name='Issuance Trend'
))
fig_issuance_trend.update_layout(
    title='License Issuance Over Time',
    xaxis_title='Time',
    yaxis_title='Number of Licenses'
)
fig_issuance_trend.show()

# Export filtered data to a new Excel file
filtered_data = df[df['License Type'] == 'Poultry Farm']
filtered_data.to_excel('Filtered_Agricultural_Licenses.xlsx', index=False)

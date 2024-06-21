from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

root = Path(__file__).parent / "csv_files"

df = pd.read_csv(root / "weather_data.csv")

# find best city each day
ordered_df = df.groupby("day_id").apply(
    lambda x: x.sort_values(by=["temp_max", "humidity", "clouds", "rain_prob"],
                            ascending=[False, True, True, True]
                            ).head(5)).reset_index(drop=True)

print(ordered_df)
# create top 5 map of the cities
fig = px.scatter_mapbox(
    ordered_df,
    lat="lat",
    lon="lon",
    hover_name="city",
    hover_data={"day_id": True, "temp_max": True, "humidity": True,
                "clouds": True, "rain_prob": True},
    color="temp_max",
    size="temp_max",
    zoom=5,
    height=800,
    animation_frame="day_id",
    animation_group="temp_max",
    color_continuous_scale=px.colors.sequential.Bluered,
    size_max=35
)

fig.update_layout(
    mapbox_style="open-street-map",
    title={"text": "<b>Top 5 destinations according to the weather forecast</b>",
           "x": 0.5},
    margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.show()
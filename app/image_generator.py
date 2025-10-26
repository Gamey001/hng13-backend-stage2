from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

def generate_summary_image(total_countries, top_countries):
    os.makedirs("cache", exist_ok=True)
    img = Image.new("RGB", (800, 400), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), f"Total Countries: {total_countries}", fill=(0, 0, 0))
    draw.text((20, 60), "Top 5 by Estimated GDP:", fill=(0, 0, 0))

    y = 90
    for i, c in enumerate(top_countries, start=1):
        draw.text((40, y), f"{i}. {c.name} - {c.estimated_gdp:,.2f}", fill=(0, 0, 0))
        y += 30

    draw.text((20, 250), f"Last Refreshed: {datetime.utcnow().isoformat()} UTC", fill=(0, 0, 0))
    img.save("cache/summary.png")

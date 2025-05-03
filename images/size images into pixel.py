from PIL import Image
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


img = Image.open("ghibli.png")
resized_img = img.resize((400, 400))  # (width, height)
resized_img.save("ghibli_new.png")

# embed to create hover
embed = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Responsive Hover Image</title>
<style>
    html, body {
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    .container {
        width: 100%;
        max-width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .card {
        width: 100%;
        max-width: 400px;
        aspect-ratio: 1 / 1;
        background-image: url("https://sijielin.github.io/files/photo.jpg");
        background-size: cover;
        background-position: center;
        transition: background-image 0.3s ease;
    }

    .card:hover {
        background-image: url("https://sijielin.github.io/files/ghibli_new.png");
        background-size: cover;
    }
</style>
</head>
<body>
    <div class="container">
        <div class="card"></div>
    </div>
</body>
</html>
"""
# copy paste into add --> embed














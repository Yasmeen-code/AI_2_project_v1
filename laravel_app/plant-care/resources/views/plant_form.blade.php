<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Smart Plant Care 🌿</title>
  <style>
    body { font-family: Poppins, sans-serif; background: #f6fff6; text-align: center; }
    form { margin: 50px auto; width: 300px; padding: 20px; background: #fff; border-radius: 10px; box-shadow: 0 0 10px #d0e8d0; }
    input { width: 100%; margin-bottom: 10px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
    button { padding: 10px 20px; border: none; background: #4caf50; color: #fff; border-radius: 5px; cursor: pointer; }
    button:hover { background: #45a049; }
    h1 { color: #2e7d32; }
  </style>
</head>
<body>
  <h1>🌱 Smart Plant Care Advisor</h1>

  <form method="POST" action="{{ route('predict') }}">
    @csrf
    <input type="number" name="temp" placeholder="Temperature (°C)" required>
    <input type="number" name="humidity" placeholder="Humidity (%)" required>
    <input type="number" name="watering" placeholder="Watering Amount (ml)" required>
    <input type="number" name="soil_moisture" placeholder="Soil Moisture (%)" required>
    <button type="submit">Check Health</button>
  </form>

  @if(session('result'))
    <h3>{{ session('result')['status'] }}</h3>
    <p>{{ session('result')['advice'] }}</p>
  @endif
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Plant Care</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="50" cy="80" r="1.5" fill="rgba(255,255,255,0.1)"/></svg>') repeat;
            pointer-events: none;
            animation: float 20s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        .container {
            background: rgba(255,255,255,0.98);
            backdrop-filter: blur(15px);
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 600px;
            animation: fadeInUp 1s ease-out;
            position: relative;
            z-index: 1;
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(40px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }
        h2 {
            text-align: center;
            color: #2d3436;
            margin-bottom: 30px;
            font-size: 2.3rem;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h2 i {
            color: #6c5ce7;
            margin-right: 10px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 20px;
        }
        .form-group {
            display: flex;
            flex-direction: column;
            position: relative;
        }
        .form-group.full-width {
            grid-column: span 2;
        }
        label {
            display: flex;
            align-items: center;
            margin-bottom: 5px;
            color: #2d3436;
            font-weight: 600;
            font-size: 0.95rem;
        }
        label i {
            color: #6c5ce7;
            margin-right: 8px;
            transition: transform 0.3s ease;
        }
        .form-group:hover label i {
            transform: rotate(10deg);
        }
        input {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e1e8ed;
            border-radius: 12px;
            background: #f8f9fa;
            font-size: 0.95rem;
            font-family: inherit;
            transition: all 0.3s ease;
            position: relative;
        }
        input:focus {
            border-color: #6c5ce7;
            background: white;
            box-shadow: 0 0 0 3px rgba(108, 92, 231, 0.1);
            transform: translateY(-1px);
        }
        .hint {
            font-size: 0.8rem;
            color: #636e72;
            margin-top: 5px;
            line-height: 1.3;
            opacity: 0.8;
        }
        button {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            margin-top: 20px;
        }
        button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.6s;
        }
        button:hover {
            transform: translateY(-4px);
            box-shadow: 0 15px 35px rgba(108, 92, 231, 0.4);
        }
        button:hover::before {
            left: 100%;
        }
        button:active {
            transform: translateY(-2px);
        }
        .info-box {
            background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
            border-left: 5px solid #6c5ce7;
            padding: 20px;
            border-radius: 15px;
            font-size: 0.95rem;
            color: #2d3436;
            margin-top: 20px;
            line-height: 1.6;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .result {
            margin-top: 35px;
            background: linear-gradient(135deg, #fd79a8 0%, #fdcb6e 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            animation: slideIn 0.8s ease-out;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(30px) scale(0.9); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }
        .result h3 {
            color: #e17055;
            margin-bottom: 15px;
            font-size: 1.6rem;
            font-weight: 700;
        }
        .result p {
            color: #2d3436;
            font-size: 1.1rem;
            line-height: 1.5;
        }
        @media (max-width: 600px) {
            .container {
                padding: 30px 25px;
                margin: 20px;
                max-width: 100%;
            }
            h2 {
                font-size: 2rem;
            }
            input {
                padding: 12px 16px;
            }
            button {
                padding: 14px;
                font-size: 1.1rem;
            }
        }
        @media (max-width: 400px) {
            h2 {
                font-size: 1.8rem;
            }
            .container {
                padding: 25px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2><i class="fas fa-leaf"></i>Smart Plant Care</h2>

        <form method="POST" action="/predict">
            @csrf
            <div class="form-grid">
                <div class="form-group">
                    <label><i class="fas fa-thermometer-half"></i>Room Temperature (°C)</label>
                    <input type="number" name="temp" step="0.1" required>
                    <p class="hint">💡 Ideal: 18°C – 30°C</p>
                </div>

                <div class="form-group">
                    <label><i class="fas fa-tint"></i>Humidity (%)</label>
                    <input type="number" name="humidity" step="0.1" required>
                    <p class="hint">💡 Prefer: 40% – 70%</p>
                </div>

                <div class="form-group">
                    <label><i class="fas fa-water"></i>Watering Amount (ml)</label>
                    <input type="number" name="watering" required>
                    <p class="hint">💧 Small: 50-150 | Med: 200-300 | Large: 400+</p>
                </div>

                <div class="form-group">
                    <label><i class="fas fa-seedling"></i>Soil Moisture (%)</label>
                    <input type="number" name="soil_moisture" min="10" max="80" required>
                    <p class="hint">💧 Dry: 20-30% | Normal: 40-60% | Wet: 65-80%</p>
                </div>
            </div>

            <div class="form-group full-width">
                <div class="info-box">
                    🌼 <strong>Tip:</strong> Keep your plant in bright, indirect sunlight and avoid overwatering. Healthy plants have steady growth and vibrant green leaves!
                </div>
            </div>

            <button type="submit">Predict Plant Health <i class="fas fa-magic"></i></button>
        </form>

        @if(session('result'))
            <div class="result">
                <h3>{{ session('result')['status'] }}</h3>
                <p>{{ session('result')['advice'] }}</p>
            </div>
        @endif
    </div>
</body>
</html>

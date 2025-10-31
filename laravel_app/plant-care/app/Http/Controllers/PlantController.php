<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class PlantController extends Controller
{
    public function index()
    {
        return view('plant_form');
    }

    public function predict(Request $request)
    {
        $response = Http::post('http://127.0.0.1:5000/predict', [
            'temp' => $request->temp,
            'humidity' => $request->humidity,
            'watering' => $request->watering,
            'soil_moisture' => $request->soil_moisture,
        ]);

        $data = $response->json();

        $result = [
            'status' => $data['health_status'] == 1 ? '✅ Plant is Healthy!' : '❌ Unhealthy Plant!',
            'advice' => $data['advice']
        ];

        return redirect('/')->with('result', $result);
    }
}

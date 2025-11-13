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
        try {
            // 🔹 إرسال البيانات إلى Flask API
            $response = Http::post('http://127.0.0.1:5000/predict', [
                'temp' => $request->temp,
                'humidity' => $request->humidity,
                'watering' => $request->watering,
                'soil_moisture' => $request->soil_moisture,
            ]);

            // 🔹 تحويل الـ response إلى JSON
            $data = $response->json();

            // ✅ التحقق إن الرد فعلاً جاي من Flask
            if (!$response->successful() || !$data || !isset($data['message'])) {
                return redirect('/')->with('result', [
                    'status' => '⚠️ Error: Could not get response from AI model.',
                    'advice' => 'Please make sure your AI server is running on port 5000.'
                ]);
            }

            // 🔹 النتيجة النهائية
            $result = [
                'status' => $data['message'] ?? '⚠️ Unknown result',
                'advice' => $data['advice'] ?? 'No advice available'
            ];

            return redirect('/')->with('result', $result);
        } catch (\Exception $e) {
            // 🔥 في حالة حدوث خطأ بالاتصال أو السيرفر
            return redirect('/')->with('result', [
                'status' => '❌ Server Error!',
                'advice' => $e->getMessage()
            ]);
        }
    }
}

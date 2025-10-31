<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PlantController;

Route::get('/', [PlantController::class, 'index']);
Route::post('/predict', [PlantController::class, 'predict'])->name('predict');

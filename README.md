# Evaluating the Performance of Image Super-Resolution Baselines in the Presence of Spatially Correlated Pink Noise

This repository contains the official Python implementation and simulation environment for analyzing how classical digital upscaling and linear filtering baselines perform under non-white, spatially correlated $1/f$ pink noise[cite: 1, 12, 119].

##  Author
* [cite_start]**Diganth Maruthi** 

---

## Project Overview
Single-image super-resolution (SISR) models traditionally assume image degradation is caused by independent Additive White Gaussian Noise (AWGN)[cite: 10]. [cite_start]However, physical camera sensors, atmospheric scattering, and hardware anomalies frequently introduce spatially correlated, low-frequency **pink noise** ($1/f$) patterns[cite: 11, 30]. 

This study evaluates two classic pipelines:
1. [cite_start]**Method A:** Bicubic Upscaling Only [cite: 80]
2. [cite_start]**Method B:** Bicubic Upscaling + Spatial Gaussian Low-Pass Filtering ($5 \times 5$ kernel) [cite: 14, 81]

### Key Finding
Contrasting our initial hypothesis, **standard bicubic upscaling consistently maintained a lower Mean Squared Error (MSE) than the Gaussian filtering method**[cite: 15, 16, 40]. [cite_start]While the Gaussian filter visually mitigated the cloudy noise clusters, it introduced heavy edge blurring[cite: 17, 18]. [cite_start]The pixel-level mathematical penalty of this uniform blurring outweighed the benefits of background noise reduction[cite: 18, 57].

---

## Results & Quantitative Evaluation

The Mean Squared Error (MSE) scores across different noise intensities ($\sigma$) show that standalone upscaling retains pixel-level mathematical accuracy better than uniform linear filters[cite: 39, 43, 53].

### Reconstruction Error Scores (MSE)
| Experiment Trial | Noise Intensity ($\sigma$) | Bicubic Only MSE | Bicubic + Gaussian Filter MSE |
| :--- | :--- | :--- | :--- |
| **Trial 1** | 0.10 (Light Noise) | 0.00393 | 0.00496 |
| **Trial 2** | 0.20 (Medium Noise) | 0.00961 | 0.01052 |
| **Trial 3** | 0.30 (Heavy Noise) | 0.01983 | 0.02048 |

> *Note: Lower numerical scores correspond to a reduction in digital reconstruction error compared directly back to the reference source target matrix[cite: 116].*

---

## Methodology & Environment

The simulation pipeline consists of:
1. **Downsampling:** High-resolution geometric target matrices ($300 \times 300$) downscaled to $150 \times 150$ using cubic pixel interpolation[cite: 68, 69].
2. **Pink Noise Generation:** Modeled in the frequency domain using a 2D Fast Fourier Transform (FFT), scaling the grid coordinates inversely by the square root of the frequencies ($1/f$) before transforming back via IFFT[cite: 73, 74, 76].
3. **Reconstruction:** Applying bicubic upscaling and spatial Gaussian filtering to track pixel variations[cite: 79, 80, 81].

### Environment Requirements
* **Language:** Python 3.12 [cite: 66]
* **Architecture:** Executed locally on Apple M4 silicon [cite: 66]
* **Core Libraries:** `numpy`, `opencv-python` (`cv2`), `scipy`, `matplotlib` [cite: 66, 84]

---

## Getting Started

### Installation
Clone this repository and install the necessary computational modules:
```bash
git clone [https://github.com/diganthm22-lab/color-noise-stochastic-resonance-1-f-.git](https://github.com/diganthm22-lab/color-noise-stochastic-resonance-1-f-.git)
cd color-noise-stochastic-resonance-1-f-
pip install numpy opencv-python scipy matplotlib

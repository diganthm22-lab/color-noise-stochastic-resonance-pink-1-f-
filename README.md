# Evaluating the Performance of Image Super-Resolution Baselines in the Presence of Spatially Correlated Pink Noise

This repository contains the official Python simulation environment and core codebase for the research study: **"Evaluating the Performance of Image Super-Resolution Baselines in the Presence of Spatially Correlated Pink Noise"**.

The project investigates how classical single-image super-resolution (SISR) upscaling and linear spatial filtering benchmarks behave when processing images degraded by non-white, spatially correlated low-frequency noise ($1/f$ pink noise) rather than standard independent Additive White Gaussian Noise (AWGN).

---

## 📌 Abstract / Summary

Traditional Single-Image Super-Resolution (SISR) frameworks heavily rely on the assumption that image degradation is caused by independent Additive White Gaussian Noise (AWGN). However, physical camera sensors, atmospheric scattering, and specialized imaging hardware often generate spatially correlated, low-frequency colored noise patterns in real-world settings. 

This study evaluates the performance of digital upscaling (**Bicubic Interpolation**) and spatial linear filtering (**Gaussian Low-Pass Filter**) baselines when processing benchmark images corrupted with simulated $1/f$ pink noise across three distinct intensities ($\sigma = 0.10, 0.20, 0.30$).

### Key Findings
* **Hypothesis Rejection:** Contrary to our initial hypothesis that a spatial filtering pipeline would decrease overall mathematical reconstruction error, **standard bicubic upscaling consistently maintained a lower error index** across all tested noise intensities.
* **The Restorational Compromise:** While a $5 \times 5$ spatial Gaussian filter successfully removed cloudy noise clusters visually, it applied a uniform blur across the entire pixel array. Because it cannot differentiate noise from sharp boundaries, it heavily smoothed structural elements. This generated a severe pixel-level mathematical error penalty that exceeded the benefits of background noise reduction.

---

## 📊 Quantitative Results

Quantitative tracking was conducted by calculating the pixel-by-pixel **Mean Squared Error (MSE)** between the original clean high-resolution targets and the reconstructed outputs. Lower numerical scores correspond to a reduction in digital reconstruction error.

### Table 1: Reconstruction Error Scores (MSE) across Varied Pink Noise Levels

| Experiment Trial | Noise Intensity ($\sigma$) | Bicubic Only MSE | Bicubic + Gaussian Filter MSE |
| :--- | :---: | :---: | :---: |
| **Trial 1** | 0.10 (Light Noise) | **0.00393** | 0.00496 |
| **Trial 2** | 0.20 (Medium Noise) | **0.00961** | 0.01052 |
| **Trial 3** | 0.30 (Heavy Noise) | **0.01983** | 0.02048 |

---

## 🔍 Visual Assessment & Framework Setup

The simulation dataset consists of high-resolution $300 \times 300$ pixel grayscale geometric target matrices designed specifically to facilitate edge tracking. 

1. **Downsampling:** To simulate data loss from physical sensor pixel constraints, images are downscaled by a scale factor of 2 using cubic pixel interpolation (generating a $150 \times 150$ base).
2. **Noise Application:** Spatially correlated $1/f$ pink noise is generated via a 2D Fast Fourier Transform (FFT), scaled inversely by the frequency coordinates, transformed back via Inverse FFT, and combined with the downscaled images using matrix addition.
3. **Reconstruction Pathways:**
   * **Method A (Bicubic Only):** The noisy matrix is expanded back to $300 \times 300$ using a single-pass bicubic interpolation function (`cv2.INTER_CUBIC`).
   * **Method B (Filtered):** The bicubic upscaled matrix is processed through a spatial Gaussian filter utilizing a $5 \times 5$ pixel kernel (`cv2.GaussianBlur`).

---

## 💻 Environment & Requirements

All steps of this experiment were executed locally using a Python script.

* **Language/Architecture:** Python 3.12 running on Apple M4 silicon architecture
* **Core Dependencies:** * `NumPy` (for matrix addition and Fourier analysis)
  * `OpenCV` (for image resizing and Gaussian filtering packages)
  * `SciPy` (for localized computational packages)
  * `Matplotlib` (for compiling visual plots and data tracking)

### Quick Setup

```bash
# Clone the repository
git clone [https://github.com/diganthm22-lab/color-noise-stochastic-resonance-1-f-.git](https://github.com/diganthm22-lab/color-noise-stochastic-resonance-1-f-.git)
cd color-noise-stochastic-resonance-1-f-

# Install required dependencies
pip install numpy opencv-python scipy matplotlib

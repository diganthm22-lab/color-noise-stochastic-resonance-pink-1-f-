# Evaluating the Performance of Image Super-Resolution Baselines in the Presence of Spatially Correlated Pink Noise

[cite_start]This repository contains the official Python simulation environment and core codebase for the research study: **"Evaluating the Performance of Image Super-Resolution Baselines in the Presence of Spatially Correlated Pink Noise"**[cite: 1].

[cite_start]The project investigates how classical single-image super-resolution (SISR) upscaling and linear spatial filtering benchmarks behave when processing images degraded by non-white, spatially correlated low-frequency noise ($1/f$ pink noise) rather than standard independent Additive White Gaussian Noise (AWGN)[cite: 10, 11, 12].

---

## 📌 Abstract / Summary

[cite_start]Traditional Single-Image Super-Resolution (SISR) frameworks heavily rely on the assumption that image degradation is caused by independent Additive White Gaussian Noise (AWGN)[cite: 10]. [cite_start]However, physical camera sensors, atmospheric scattering, and specialized imaging hardware often generate spatially correlated, low-frequency colored noise patterns in real-world settings[cite: 11]. 

[cite_start]This study evaluates the performance of digital upscaling (**Bicubic Interpolation**) and spatial linear filtering (**Gaussian Low-Pass Filter**) baselines when processing benchmark images corrupted with simulated $1/f$ pink noise across three distinct intensities ($\sigma = 0.10, 0.20, 0.30$)[cite: 12, 14].

### Key Findings
* [cite_start]**Hypothesis Rejection:** Contrary to our initial hypothesis that a spatial filtering pipeline would decrease overall mathematical reconstruction error, **standard bicubic upscaling consistently maintained a lower error index** across all tested noise intensities[cite: 15, 16, 40, 41].
* [cite_start]**The Restorational Compromise:** While a $5 \times 5$ spatial Gaussian filter successfully removed cloudy noise clusters visually, it applied a uniform blur across the entire pixel array[cite: 17, 18, 55]. [cite_start]Because it cannot differentiate noise from sharp boundaries, it heavily smoothed structural elements[cite: 56]. [cite_start]This generated a severe pixel-level mathematical error penalty that exceeded the benefits of background noise reduction[cite: 18, 57].

---

## 📊 Quantitative Results

[cite_start]Quantitative tracking was conducted by calculating the pixel-by-pixel **Mean Squared Error (MSE)** between the original clean high-resolution targets and the reconstructed outputs[cite: 39, 82]. [cite_start]Lower numerical scores correspond to a reduction in digital reconstruction error[cite: 116].

### [cite_start]Table 1: Reconstruction Error Scores (MSE) across Varied Pink Noise Levels [cite: 113]

| Experiment Trial | Noise Intensity ($\sigma$) | Bicubic Only MSE | Bicubic + Gaussian Filter MSE |
| :--- | :---: | :---: | :---: |
| **Trial 1** | 0.10 (Light Noise) | **0.00393** | 0.00496 |
| **Trial 2** | 0.20 (Medium Noise) | **0.00961** | 0.01052 |
| **Trial 3** | 0.30 (Heavy Noise) | **0.01983** | 0.02048 |

---

## 🔍 Visual Assessment & Framework Setup

[cite_start]The simulation dataset consists of high-resolution $300 \times 300$ pixel grayscale geometric target matrices designed specifically to facilitate edge tracking[cite: 68]. 

1. [cite_start]**Downsampling:** To simulate data loss from physical sensor pixel constraints, images are downscaled by a scale factor of 2 using cubic pixel interpolation (generating a $150 \times 150$ base)[cite: 69].
2. [cite_start]**Noise Application:** Spatially correlated $1/f$ pink noise is generated via a 2D Fast Fourier Transform (FFT), scaled inversely by the frequency coordinates, transformed back via Inverse FFT, and combined with the downscaled images using matrix addition[cite: 71, 73, 74, 76, 77].
3. **Reconstruction Pathways:**
   * [cite_start]**Method A (Bicubic Only):** The noisy matrix is expanded back to $300 \times 300$ using a single-pass bicubic interpolation function (`cv2.INTER_CUBIC`)[cite: 80].
   * [cite_start]**Method B (Filtered):** The bicubic upscaled matrix is processed through a spatial Gaussian filter utilizing a $5 \times 5$ pixel kernel (`cv2.GaussianBlur`)[cite: 81].

---

## 💻 Environment & Requirements

[cite_start]All steps of this experiment were executed locally using a Python script[cite: 66, 119].

* [cite_start]**Language/Architecture:** Python 3.12 running on Apple M4 silicon architecture [cite: 66]
* [cite_start]**Core Dependencies:** * `NumPy` (for matrix addition and Fourier analysis) [cite: 66, 77]
  * [cite_start]`OpenCV` (for image resizing and Gaussian filtering packages) [cite: 66]
  * [cite_start]`SciPy` (for localized computational packages) [cite: 66]
  * [cite_start]`Matplotlib` (for compiling visual plots and data tracking) [cite: 84]

### Quick Setup

```bash
# Clone the repository
git clone [https://github.com/diganthm22-lab/color-noise-stochastic-resonance-1-f-.git](https://github.com/diganthm22-lab/color-noise-stochastic-resonance-1-f-.git)
cd color-noise-stochastic-resonance-1-f-

# Install required dependencies
pip install numpy opencv-python scipy matplotlib-python scipy matplotlib

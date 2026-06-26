# color-noise-stochastic-resonance-pink-1-f-
The project evaluates how traditional digital image upscaling (Bicubic Interpolation) and linear spatial filtering frameworks perform when tasked with reconstructing low-resolution images corrupted by non-white, spatially correlated Pink Noise (1/f) profiles instead of traditional Additive White Gaussian Noise.

import numpy as np
import cv2
import matplotlib.pyplot as plt

# --- STEP 1: MAKE PINK NOISE ---
def make_pink_noise(width, height):
    
    white = np.random.normal(0, 1, (height, width)) # This generates random matrix numbers and smooths them out to look like clouds
    fft_white = np.fft.fft2(white) 
   
    u = np.fft.fftfreq(height)[:, None]
    v = np.fft.fftfreq(width)[None, :]
   
    dist = np.sqrt(u**2 + v**2)
    dist[0, 0] = 1
   
    fft_pink = fft_white / np.sqrt(dist)
   
    pink = np.real(np.fft.ifft2(fft_pink))
    pink = (pink - np.min(pink)) / (np.max(pink) - np.min(pink))
    return pink

# --- STEP 2: CREATING AND DOWNSCALING AN IMAGE ---

hr_image = np.zeros((300, 300), dtype=np.float32)
hr_image[75:225, 75:225] = 1.0 

lr_image = cv2.resize(hr_image, (150, 150), interpolation=cv2.INTER_AREA) # Shrink it by half

noise = make_pink_noise(150, 150) * 0.3
lr_noisy = np.clip(lr_image + noise, 0, 1)

# --- STEP 3: RECONSTRUCTION ---

sr_bicubic = cv2.resize(lr_noisy, (300, 300), interpolation=cv2.INTER_CUBIC) # Method A: Basic Zooming

sr_filtered = cv2.blur(sr_bicubic, (5, 5)) # Method B: Zooming + A Blur filter

# --- STEP 4: MEAN SQUARED ERROR ---
def get_score(original, reconstructed):
    
    error = np.mean((original - reconstructed) ** 2)
    return round(error, 5)

print("Bicubic Error Score:", get_score(hr_image, sr_bicubic))
print("Filtered Error Score:", get_score(hr_image, sr_filtered))

# --- STEP 5: VISUALIZATION ---
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(hr_image, cmap='gray')
axes[0].set_title("1. Original Clean HR")

axes[1].imshow(lr_noisy, cmap='gray')
axes[1].set_title("2. Small Noisy Input")

axes[2].imshow(sr_filtered, cmap='gray')
axes[2].set_title("3. Reconstructed Output")

plt.tight_layout()
plt.show()

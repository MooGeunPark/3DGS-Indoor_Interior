# Save me, Sims!

📢 This project was conducted as part of the 2024 Winter Semester Deep Learning Society in Korea University [AIKU](https://github.com/AIKU-Official) activities.

## Introduction

Have you ever wanted to redecorate your home or a specific space in a completely different style but found it too troublesome to move furniture or make purchases?

We propose a service that allows you to redesign and visualize your space exactly how you want, simply by providing a short video clip taken from different angles and some prompts describing your requirements.

## Methodology
<p align="center"><img width="700" src="https://github.com/MooGeunPark/3DGS-Indoor_Interior/blob/main/images/Pipeline.png"></p>   

1. Record a short video capturing the space from various angles.
2. Input your prompt describing the desired changes. Example: “Replace the table with the one I provided. Put a plate on the table.”
3. se a GAN-based AI to modify the images according to the prompt.
4. Use a 3D reconstruction model for rendering and visualization.

## Example Output
### Instant-NGP
<p align="center"><img width="700" src="https://github.com/user-attachments/assets/66b56e96-d1d0-4da4-8c0f-7ef8d5fa6e67"></p>

### CustomNet
<p align="center"><img width="700" src="https://github.com/MooGeunPark/3DGS-Indoor_Interior/blob/main/images/CustomNet.png"></p>

## Limitations & Future Works
### Limitations
* Due to GPU memory issues, we were unable to experiment with many models.
* Since we were unable to fine-tune the model, there is a resolution gap compared to diffusion models, which limits performance.

### Future Works
* We focus on running models that do not require extensive computing resources or adjust the resolution for testing.
* Set the task in more detail and focus on just one specific objective.

## Team Members

- [Moogeun Park]: (3D reconstruction model, Rendering)
- [Minha Lee]: (Query mesh, Point cloud, Depth map)
- [Hyunwook Choi]: (3D reconstuction model, Diffusion model)

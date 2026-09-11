# Chapter 56 Exercise Solutions

1. Encoding maps observations to latent representations; decoding maps latent representations back to the observation space.
2. Without a constraint, a flexible model can copy inputs without learning a useful representation.
3. It measures discrepancy between an input and its reconstruction under a specified loss.
4. The score depends on learned normality, capacity, preprocessing, and nuisance variation and is not calibrated against defect labels.
5. Compute $z=\mu+\exp(0.5\log\sigma^2)\odot\epsilon$ using parameter-free noise $\epsilon$.
6. Reconstruction quality and closeness of the approximate latent distribution to the prior.
7. Smoothness in model space does not impose every physical, safety, or business constraint.
8. Feature extraction freezes the pretrained body; fine-tuning updates some or all pretrained parameters.
9. Source features may miss target evidence and may import biases or shortcuts.
10. Autoregressive, variational autoencoder, generative adversarial, and diffusion models.
11. A plausible sample can be memorized, physically impossible, repetitive, unrepresentative, or useless downstream.
12. Hold model, real training data, tuning, and untouched real test data constant; add synthetic data only to the treatment pipeline and compare prespecified metrics.
13. The generator produces too few kinds of output and fails to cover parts of the real distribution.
14. A generator can reproduce or reveal information about its training records.
15. Model weights, preprocessing, training snapshot, sampling settings, conditions or prompts, thresholds, license, and owner are suitable examples.
16. Train only on governed historical normal data, validate scores on labeled defects and nuisance shifts, set a capacity-based review threshold, run silently first, audit slices, and define owners and rollback.

## [1.0.10](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.9...v1.0.10) (2025-07-11)

### Bug Fixes

* add mlflow tracing ([227561f](https://github.com/nishaero/mlflow-llm-demo/commit/227561f334df5fc824f0f1c46bf4d86f8992c7dd))

## [1.0.9](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.8...v1.0.9) (2025-07-11)

### Bug Fixes

* update base image to include cuda 12.1 ([37295bd](https://github.com/nishaero/mlflow-llm-demo/commit/37295bd788c44c86919818934640cff986987d28))

## [1.0.8](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.7...v1.0.8) (2025-07-11)

### Bug Fixes

* install gptq and llama-cpp-python ([4c7d266](https://github.com/nishaero/mlflow-llm-demo/commit/4c7d266b65589709d406ef9d71c6310e9930b4ba))

## [1.0.7](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.6...v1.0.7) (2025-07-10)

### Bug Fixes

* update model hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 ([23ea3d0](https://github.com/nishaero/mlflow-llm-demo/commit/23ea3d008eb2199ad421f204778ced6fb2aa9138))

## [1.0.6](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.5...v1.0.6) (2025-07-10)

### Bug Fixes

* update model to use llama-3-32b.Q4_K_M.gguf ([50984e6](https://github.com/nishaero/mlflow-llm-demo/commit/50984e68a6ad26568630bd84ded0a433f65ced9a))

## [1.0.5](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.4...v1.0.5) (2025-07-10)

### Bug Fixes

* update model to meta-llama/Meta-Llama-3-70B-Instruct with 8bit quant ([bd64fc8](https://github.com/nishaero/mlflow-llm-demo/commit/bd64fc854b03c98af7c69e389fa2d0fc3c3fdff6))

## [1.0.4](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.3...v1.0.4) (2025-07-10)

### Bug Fixes

* update model to meta-llama/Meta-Llama-3-8B-Instruct ([1ba92a8](https://github.com/nishaero/mlflow-llm-demo/commit/1ba92a8d179c46f5ba9a6d8d95e8e1f8080f335c))

## [1.0.3](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.2...v1.0.3) (2025-07-10)

### Bug Fixes

* use bitsandbytes for quantization ([f743f32](https://github.com/nishaero/mlflow-llm-demo/commit/f743f320306dd520c0b90762620d0ded87a29b59))

## [1.0.2](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.1...v1.0.2) (2025-07-10)

### Bug Fixes

* update ui ([48bd347](https://github.com/nishaero/mlflow-llm-demo/commit/48bd34730b1c727f8a4e821d91989108b1265f5a))

## [1.0.1](https://github.com/nishaero/mlflow-llm-demo/compare/v1.0.0...v1.0.1) (2025-07-10)

### Bug Fixes

* update model to meta-llama/Meta-Llama-3-70B-Instruct ([a388614](https://github.com/nishaero/mlflow-llm-demo/commit/a388614fa66dbb7a060caea0a85eaff02ef74eed))

## 1.0.0 (2025-07-10)

### Features

* add llm test app ([389de63](https://github.com/nishaero/mlflow-llm-demo/commit/389de63a79f3a3a36ed5235504a52c425621780d))

### Bug Fixes

* add environment to dev ([684c0ef](https://github.com/nishaero/mlflow-llm-demo/commit/684c0efb65bc451165882b1ed552c6d9660c63f7))
* add html for direct interaction ([1956f9b](https://github.com/nishaero/mlflow-llm-demo/commit/1956f9b03b93e626743a121c1696dd3c8b828e99))
* add hugging face login using token ([40c741c](https://github.com/nishaero/mlflow-llm-demo/commit/40c741c07003a2973b28d6810cf69078e1306ef4))
* add llm runner package ([91414d7](https://github.com/nishaero/mlflow-llm-demo/commit/91414d7e3bd3201b6595bf3764bc4b7df0037fdb))
* add module accelerate ([e3432dd](https://github.com/nishaero/mlflow-llm-demo/commit/e3432dd3e0988b6f12e2d1e032447d7c66a49f6a))
* add semantic release for docker versioning ([6fa5b8c](https://github.com/nishaero/mlflow-llm-demo/commit/6fa5b8c9ebf9a14a04048d13f638918e94137c16))
* change model to llama 70b instruct ([aaa5b78](https://github.com/nishaero/mlflow-llm-demo/commit/aaa5b7853e1843e463a162ba53c513e292b374e3))
* move github folder to root ([8084072](https://github.com/nishaero/mlflow-llm-demo/commit/8084072e4c9946a0d726206f3f56b89408e8a2c9))
* move github folder to root ([eadb130](https://github.com/nishaero/mlflow-llm-demo/commit/eadb13053dbfe6c121984b574c861398f1f5a595))
* update model to phi-3-medium-128k-instruct ([37ec42b](https://github.com/nishaero/mlflow-llm-demo/commit/37ec42bfe9ea2c09357dd745e3b5efd71a2d2fc7))
* update workflow ci file ([1c32788](https://github.com/nishaero/mlflow-llm-demo/commit/1c3278811245309a3d4d9ea276c8c82c40225c68))
* use 4bit quantization to fit gpu vram 5090 ([55473be](https://github.com/nishaero/mlflow-llm-demo/commit/55473be4ed20eb1e38d0566bf445faf4d6b014cd))

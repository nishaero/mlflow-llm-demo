FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl unzip build-essential \
    python3-pip python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install additional dependencies
RUN apt-get update && apt-get install -y supervisor

# Install AutoGPTQ (CUDA 12.1)
RUN pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu121/

# Optional: llama-cpp-python (for GGUF models)
RUN pip install --upgrade llama-cpp-python --extra-index-url https://pypi.nvidia.com

# Test CUDA extension
RUN python -c "import auto_gptq.nn_modules.qlinear.qlinear_cuda; print('AutoGPTQ CUDA extension loaded')"

# Copy application code
COPY . /app
WORKDIR /app

# Expose FastAPI port
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8080 5000

CMD ["/usr/bin/supervisord"]

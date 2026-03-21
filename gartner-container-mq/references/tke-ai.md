# TKE AI/ML Workload Capabilities Reference

## Why This Matters

Dennis Smith's #1 scoring priority for 2026 MQ is AI workload support.
His Strategic Planning Assumption: "By 2028, 95% of new AI deployments will use Kubernetes."
Every AI-related answer must be strong, specific, and quantified.

---

## GPU Support

### Available GPU Types on Tencent Cloud
(⚠️ VERIFY current availability per region before submitting)
- NVIDIA T4 (inference-optimized)
- NVIDIA A10
- NVIDIA V100 (training)
- ⚠️ H100, B200, GB200: NOT AVAILABLE (US export controls) — never claim these

### qGPU — GPU Sharing Technology
Tencent Cloud's proprietary GPU virtualization technology. Key facts:
- Allows **multiple containers to share a single physical GPU card**
- Provides **strong isolation** of both GPU compute power AND video memory between containers
- Based on Tencent's Nano GPU open-source framework
- Uses hardware-level isolation (not CUDA API hijacking) → better QoS
- Resource granularity: request GPU compute as % (e.g., 10% of GPU core) and memory in GB
  - Example: `tke.cloud.tencent.com/qgpu-core: 10` = 10% compute
  - Example: `tke.cloud.tencent.com/qgpu-memory: 4GB` = 4GB VRAM
- Supports online/offline workload mixing (inference + training on same card)
- Supports GPU compute pooling (decoupling CPU/memory from GPU resources)
- Zero Kubernetes API changes for workloads — transparent to application layer

**Documentation**: https://www.tencentcloud.com/document/product/457/42973
**Significance for questionnaire**: This directly compensates for unavailable top-tier GPUs.
Emphasize that software-layer efficiency matters more than raw hardware in production.

### Elastic GPU Framework
- Kuberentes-native CRD abstraction over GPU resources
- Cluster-level visibility into GPU slice allocation (solving the "black box" problem)
- First adapter: TKE qGPU
- Use cases: mixed clusters with inference (qGPU shared) + training (whole card) workloads

---

## AI Scheduling

### Volcano Scheduler
- Batch scheduling framework for AI/ML jobs on Kubernetes
- Key capabilities:
  - **Gang scheduling**: all pods of a job start together or not at all (prevents deadlock)
  - **Fair-share queuing**: multi-tenant AI workload prioritization
  - **Preemption**: high-priority jobs can preempt lower-priority ones
  - **Bin packing**: optimize GPU node utilization
- CNCF graduated project; Tencent is a major contributor
- Natively integrated in TKE

### Node Auto-Provisioning for AI Clusters
- Cluster Autoscaler dynamically provisions GPU nodes on demand
- Heterogeneous node pools: mix CPU and GPU nodes in same cluster
- Spot/preemptible GPU instances for cost-optimized batch training

---

## LLM Serving & Inference

### TACO-LLM (Tencent Acceleration Toolkit for LLM)
- LLM inference acceleration framework developed by Tencent
- Key capabilities:
  - Up to 3x throughput improvement vs. vanilla vLLM (⚠️ VERIFY exact benchmark)
  - Supported models: Llama series, Qwen, Baichuan, and other popular open-source LLMs
  - Continuous batching, paged attention, speculative decoding
  - Optimized for NVIDIA T4 and A10 (the GPUs actually available on Tencent Cloud)
- Runs as Kubernetes workload on TKE
- [⚠️ VERIFY public documentation URL for TACO-LLM]

**Significance for questionnaire**: This is a key differentiator. TACO-LLM shows Tencent is
investing heavily in software-layer LLM optimization, compensating for GPU hardware constraints.

---

## AI Training Integration

### TI-One (Tencent Intelligent Titanium — One-Stop AI Platform)
- Full ML lifecycle: data prep → training → evaluation → deployment
- Training frameworks supported: PyTorch, TensorFlow, MXNet, PaddlePaddle
- Distributed training: supports multi-node, multi-GPU jobs via Kubernetes
- Uses Volcano scheduler for job queue management
- Output models can be deployed to TKE as inference services
- **Documentation**: https://www.tencentcloud.com/document/product/851

### Training Infrastructure on TKE
- RDMA/high-speed networking between GPU nodes for large-scale distributed training
  (⚠️ VERIFY: availability and specifics)
- PersistentVolume support for training datasets via CFS (high-throughput NFS) and COS
- Job checkpointing support for fault-tolerant long-running training runs

---

## AI at Hyperscale — Tencent Ecosystem Evidence

TKE runs AI workloads at massive scale within Tencent's own ecosystem:
- Content recommendation systems (Tencent Video, QQ Music)
- Real-time game AI inference (Honor of Kings, 100M+ DAU at peak)
- NLP model serving for Tencent's enterprise AI products
- Hunyuan (Tencent's foundation model) deployed on Tencent Cloud infrastructure

These represent production AI deployments at a scale that few cloud providers can demonstrate
from their own internal usage.

---

## Platform Engineering for AI

- **AI-specific node pools**: dedicated GPU node pools with auto-scaling
- **GPU observability**: GPU metrics via dcgm-exporter integrated into CLS/CM
- **Cost management**: qGPU sharing reduces per-inference cost; spot instances for training
- **Model registry**: container images with ML frameworks published to TCR
- **GitOps for ML**: ArgoCD + Helm for reproducible model deployment pipelines

---

## Answer Template for AI Questions

When answering AI-related questions, always follow this structure:

1. **Lead with qGPU** — it's a genuine differentiator most competitors don't have
2. **Mention Volcano** — it's CNCF-recognized and validates ecosystem participation
3. **Add TACO-LLM** — shows software-level investment to compensate for GPU hardware
4. **Cite Tencent's own ecosystem** as production-scale evidence
5. **Close with international availability** — "Available across TKE international regions including Singapore, Frankfurt, and Virginia"
6. **Include documentation URL**

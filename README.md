## Learning Unified Multimodal Embeddings for Cross-Modal Retrieval
using BERT + CLIP + CLAP + FAISS

### What is 'embeddings'?

Embeddings are a way to represent complex data (such as words, images, or audio data) as numerical vectors in a continuous vector space. The idea is that similar data points are represented by vectors that are close to each other in this space, while dissimilar data points are further apart.

![1_kJmMOn-zY-umSthftJl0cw](https://github.com/user-attachments/assets/9bbe95d5-5da0-414b-91eb-298f013d7ce9)

- Multimodal embeddings combine multiple types of data (or modalities) such as text, images, and audio into a single, unified vector space. The goal is to learn shared representations where similar information from different modalities is mapped to nearby points in the same space.
- Regular individual embeddings represent different types of data (like text, images, or audio) in separate vector spaces, while multimodal embeddings combine these different data types into a single shared vector space, allowing for cross-modal understanding and interaction.

### Overview
This project focuses on creating a unified multimodal embeddings model that integrates various modalities (only text, images, and audio) into a single representation space. 

### Process
- **Data Collection:**
  - Audio:
    - Used the `ESC-50: Environmental Sound Classification` Dataset (50 classes)
    - Merged the audios so that each class has 5 audio files
  - Image:
    - Utilized `bing_image_downloader` to download 5 images per class
  - Text:
    - Utilized `openbmb/MiniCPM-Llama3-V-2_5-int4` model from huggingface to generate comprehensive descriptions per image

- **Feature Extraction:**
  - Audio:
    - Used `laion/larger_clap_general` for audio feature extraction
    - Input tokens contributed: 180
    - Dimensions of the output feature: 512
  - Image:
    - Used `openai/clip-vit-large-patch14` for image feature extraction
    - Input tokens contributed: 197
    - Dimensions of the output feature: 768
  - Text:
    - Used `bert-base-uncased` as the text tokenizer
    - Input tokens contributed: 170
    - Dimensions of the output feature: 768

- **Training:**
  - Each modality's (text, image, and audio) raw output is created by their respective models
  - A linear layer projects each modality’s output into the same embedding space (256 dimensions)
  - After projection, each embedding is normalized to have unit magnitude

- **Evaluation:**
  - Evaluate the performance of the unified embeddings in tasks like cross-modal retrieval using FAISS
  - Visualized embeddings using UMAP based on the classes and the modality

### Drawbacks
  - The unified model shows more bias towards text modality when used for retrieval tasks with a small k
  - However, when k is large, audio and image data begin to show up
 
### How to improve?
  - Use much bigger length embeddings dimensions
  - Train longer (In this attempt, the model was trained for 20 epochs)
  - Try hyperparameter tuning
  - Weight the losses appropriately so text modality has less dominance 

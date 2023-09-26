# 💬 Generative Chat with Langchain and Llama Index: Enhancing Large Language Models with Custom Data

Large language models (LLMs) have become a cornerstone of natural language
processing, offering unparalleled capabilities for knowledge generation and
reasoning. However, despite their immense potential, incorporating custom,
private data into these models remains a challenge. This is where tools like
[LangChain](https://github.com/hwchase17/langchain) and
[LlamaIndex](https://github.com/jerryjliu/llama_index) (formerly 'GPT Index')
come into play, offering innovative solutions for data ingestion and indexing,
enabling developers to augment LLMs with their unique datasets.

LangChain and LlamaIndex facilitate in-context learning, an emerging paradigm
that allows developers to insert context into input prompts, leveraging LLM's
reasoning capabilities for generating more relevant and accurate responses. This
differs from finetuning, which requires retraining models using custom datasets,
often demanding significant computational resources and time.

By addressing data ingestion and indexing, LangChain and LlamaIndex provide a
streamlined framework for integrating custom data into LLMs. Their flexible
design simplifies incorporating external data sources, enabling developers to
focus on creating powerful applications that harness LLMs' full potential.

These tools bridge the gap between external data and LLMs, ensuring seamless
integration while maintaining performance. By utilizing LangChain and
LlamaIndex, developers can unlock LLMs' true potential and build cutting-edge
applications tailored to specific use cases and datasets.

## 🗺 Overview

This example showcases a simple way to use the core features of both frameworks,
ingesting data and building an index. There are lots of demos that you can plug
your index into, and we recommend you check out Langchain's [documentation on
use cases](https://langchain.readthedocs.io/en/latest/index.html#use-cases) for
more information on how to use your index.

**COMING SOON:** We also recommend you check out our [more advanced project
implementation](https://github.com/zenml-io/zenml-projects) which showcases
additional benefits of integrating these tools with ZenML.


## 🧰 How the example is implemented

This example is made up of the following steps:

- a Langchain loader step to get documentation from a GitBook website
- a LlamaIndex directory reader step to load markdown files.
- a Langchain index generator step that builds an index from the GitBook docs
  and the md files.

The index can then be accessed using ZenML's [post-execution workflow], for
example:

```python
from zenml.post_execution import get_pipeline

# Retrieve the pipeline for generating ZenML docs index
pipeline = get_pipeline("docs_to_index_pipeline")

# Access the last pipeline run
pipeline_run = pipeline.runs[-1]

# Retrieve the last step of the relevant run
last_step_of_relevant_run = pipeline_run.steps[-1]

# Read the vector index from the last step's output
vector_index = last_step_of_relevant_run.outputs.read()
```

# 🖥 Run it locally

## 👣 Step-by-Step

### 📄 Prerequisites

For this example you'll need the following:

- [An OpenAI API
  key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
  to interface with their embeddings in the VectorIndex. (Alternatively, you
  could use a different embedding provider as described [in the Langchain
  documentation](https://langchain.readthedocs.io/en/latest/modules/indexes/examples/embeddings.html).)

In addition to those requirements, in order to run this example, you need to
install and initialize ZenML:

```shell
# install CLI
pip install zenml[server]

# install ZenML integrations
zenml integration install langchain llama_index

# install additional dependencies for this example
pip install -r requirements.txt

# make your API keys available in the environment
export OPENAI_API_KEY=<your openai api key>
```

### ▶️ Run the Code

Now we're ready. Execute:

```shell
python run.py
```

This will run it with default arguments which are to query the ZenML docs and
md files.

```shell
python run.py --help
```

### ▶️ Run the Streamlit App
```shell
python app.py
```


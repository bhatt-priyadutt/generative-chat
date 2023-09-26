import os
from typing import List

from langchain.docstore.document import Document
from llama_index import SimpleDirectoryReader

from zenml.steps import BaseParameters, step


class DataLoaderParameters(BaseParameters):
    """Params for Data loader.

    Attributes:
        data_dir: dir name where documents exist
    """

    data_dir: str = 'data'


@step(enable_cache=False)
def data_loader(params: DataLoaderParameters) -> List[Document]:
    """llama data loader from filesystem.

    Args:
        params: Parameters for the step.

    Returns:
        List of langchain documents.
    """
    documents = SimpleDirectoryReader(
        params.data_dir
    ).load_data()
    return [d.to_langchain_format() for d in documents]

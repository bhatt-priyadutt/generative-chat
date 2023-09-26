from typing import List

from langchain.docstore.document import Document
from langchain.document_loaders import GitbookLoader

from zenml.steps import BaseParameters, step


class DocsLoaderParameters(BaseParameters):
    """Params for Gitbook loader.

    Attributes:
        docs_uri: URI of the docs.
        docs_base_url: Base URL of the docs.
    """

    docs_uri: str = "https://docs.zenml.io"
    docs_base_url: str = "https://docs.zenml.io"


@step(enable_cache=True)
def docs_loader(params: DocsLoaderParameters) -> List[Document]:
    """Langchain loader for Gitbook docs.

    Args:
        params: Parameters for the step.

    Returns:
        List of langchain documents.
    """
    loader = GitbookLoader(
        web_page=params.docs_uri,
        base_url=params.docs_base_url,
        load_all_paths=False,
    )
    return loader.load()

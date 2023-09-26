import argparse
import logging
from pipelines.index_builder import (
    docs_to_index_pipeline,
)
from steps.docs_loader import DocsLoaderParameters, docs_loader
from steps.index_generator import IndexGeneratorParameters, index_generator
from steps.data_loader import DataLoaderParameters,data_loader
from steps.utils import get_release_date, page_exists

docs_version = "0.35.0"
base_url = "https://docs.zenml.io"
docs_url = f"https://docs.zenml.io/v/{docs_version}/"

if not page_exists(docs_url):
    print(f"Couldn't find docs page for zenml version '{docs_version}'.")

release_date, next_release_date = get_release_date("zenml", docs_version)

parser = argparse.ArgumentParser(
    description="Build ZenML documentation index."
)
parser.add_argument(
    "--docs_version",
    type=str,
    default=docs_version,
    help="Docs version number",
)
parser.add_argument(
    "--base_url",
    type=str,
    default=base_url,
    help="Base URL for documentation site",
)
parser.add_argument(
    "--docs_url",
    type=str,
    default=docs_url,
    help="URL for documentation site",
)
args = parser.parse_args()

docs_version = args.docs_version
base_url = args.base_url
docs_url = args.docs_url

docs_to_index_pipeline = docs_to_index_pipeline(
    document_loader=docs_loader(
        params=DocsLoaderParameters(docs_uri=docs_url, base_url=base_url)
    ),
    index_generator=index_generator(params=IndexGeneratorParameters()),
    data_loader = data_loader(DataLoaderParameters())
)


def main():
    try:
        docs_to_index_pipeline.run()
    except Exception as e:
        print(f"Failed to build index for docs version '{docs_version}'.")
        print(e)


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    main()

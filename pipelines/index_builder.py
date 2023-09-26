from zenml.pipelines import pipeline


@pipeline()
def docs_to_index_pipeline(document_loader, index_generator, data_loader):
    documents = document_loader()
    data_docs = data_loader()
    index_generator(documents, data_docs)

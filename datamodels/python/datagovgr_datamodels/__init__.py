from importlib import resources

# The version of the API documentation the models are created from
with resources.open_text("datagovgr_datamodels", "API-DOC-VERSION") as f:
    API_DOC_VERSION = f.readline()

try:
    import pydantic

except ImportError:
    raise ImportError(
        "datagovgr-datamodels requires Pydantic to be installed"
    )


pydantic_version = pydantic.VERSION

if pydantic_version.startswith("1."):
    from datagovgr_datamodels.pydantic_v1.models import *

else:
    raise ImportError(
        f"Installed version of Pydantic is {pydantic_version}, but the "
        "provided models require < 2.0. Try importing from a different module."
    )

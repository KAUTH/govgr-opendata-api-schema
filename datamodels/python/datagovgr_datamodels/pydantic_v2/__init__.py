try:
    import pydantic

except ImportError:
    raise ImportError(
        "datagovgr-datamodels requires Pydantic to be installed"
    )


pydantic_version = pydantic.VERSION

if pydantic_version.startswith("2."):
    from datagovgr_datamodels.pydantic_v2.models import *

else:
    raise ImportError(
        f"Installed version of Pydantic is {pydantic_version}, but the "
        "provided models require >= 2.0. "
        "Try importing from a different module."
    )


# Monkeypatching field annoations of Pydantic models which are `pydantic.AwareDatetime`
# with `datatime.datetime`:
# The Documented API returns datetimes (e.g., for the `VaccinationData.referencedate` field) that
# do not have timezone info (e.g., '2021-01-01T00:00:00'). This causes a validation error
# since `datamodel-code-generator` uses only AwareDatetime for Pydantic v2 (for more
# information see https://github.com/koxudaxi/datamodel-code-generator/pull/1735).

import inspect
import sys
from datetime import datetime


current_module = sys.modules[__name__]
class_members = inspect.getmembers(current_module, inspect.isclass)

for class_member in class_members:
    cls = class_member[1]

    if issubclass(cls, BaseModel):

        for name, field in cls.model_fields.items():
            
            # We need to check if the annotation is a class (e.g., annotations 
            # such as `Union[int, NoneType]` are not classes).
            if inspect.isclass(field.annotation) and issubclass(field.annotation, pydantic.AwareDatetime):
                field.annotation = datetime
                
                cls.model_rebuild(force=True)

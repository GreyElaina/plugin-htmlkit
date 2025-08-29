from pydantic import BaseModel, Field
from typing import Optional
from contextlib import contextmanager
import os
from nonebot.compat import model_fields


class FcConfig(BaseModel):
    fontconfig_file: Optional[str] = Field(default=None, description="")
    fontconfig_path: Optional[str] = Field(default=None, description="")
    fontconfig_sysroot: Optional[str] = Field(default=None, description="")
    fc_debug: Optional[str] = Field(default=None, description="")
    fc_dbg_match_filter: Optional[str] = Field(default=None, description="")
    fc_lang: Optional[str] = Field(default=None, description="")
    fontconfig_use_mmap: Optional[str] = Field(default=None, description="")


@contextmanager
def set_fc_environ(config: FcConfig):
    old_values = {}
    fields = model_fields(FcConfig)
    for field in fields:
        name = field.name.upper()
        value = getattr(config, field.name)
        if value is not None:
            old_values[name] = os.environ.get(name)
            os.environ[name] = value
    try:
        yield
    finally:
        for name, value in old_values.items():
            if value is None:
                del os.environ[name]
            else:
                os.environ[name] = value

"""Compatibility entry point for Railway services configured with ``main:app``.

The application lives in :mod:`app`, while some Railway templates or an older
service Start Command may still launch ``uvicorn main:app``.
"""

from app import app


__all__ = ["app"]

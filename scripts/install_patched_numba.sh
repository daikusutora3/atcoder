#!/usr/bin/env bash
set -euo pipefail

NUMBA_VERSION="0.61.2"
NUMBA_SDIST_URL="https://files.pythonhosted.org/packages/1c/a0/e21f57604304aa03ebb8e098429222722ad99176a4f979d34af1d1ee80da/numba-0.61.2.tar.gz"

if [[ $# -ne 1 ]]; then
  cat <<'USAGE'
Usage: scripts/install_patched_numba.sh /path/to/python

Installs numba 0.61.2 using the same CUDA-disabled patching flow as the
official AtCoder 2025/10 CPython setup script. Pass the python
binary inside the target virtual environment, for example:

  scripts/install_patched_numba.sh .venv-cp313/bin/python
USAGE
  exit 1
fi

PYTHON_BIN="$1"

# Resolve to an absolute path so relative interpreters still work after cd.
if [[ "$PYTHON_BIN" != /* ]]; then
  PYTHON_BIN="$(cd "$(dirname "$PYTHON_BIN")" && pwd)/$(basename "$PYTHON_BIN")"
fi

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "error: '$PYTHON_BIN' is not an executable python interpreter" >&2
  exit 2
fi

export PIP_TRUSTED_HOST="pypi.org files.pythonhosted.org"

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

curl -fsSL "$NUMBA_SDIST_URL" -o "$WORKDIR/numba.tar.gz"
tar -xf "$WORKDIR/numba.tar.gz" -C "$WORKDIR"

# enter the extracted numba source directory
NUMBA_SRC_DIR="$(find "$WORKDIR" -maxdepth 1 -type d -name "numba-*")"
if [[ -z "$NUMBA_SRC_DIR" ]]; then
  echo "error: failed to locate extracted numba source directory" >&2
  exit 3
fi
cd "$NUMBA_SRC_DIR"

# Remove the CUDA extensions from the build, mirroring the official sed step.
"$PYTHON_BIN" - <<'PY'
import pathlib

setup_path = pathlib.Path("setup.py")
text = setup_path.read_text()
setup_path.write_text(text.replace("ext_cuda_extras, ", ""))
PY

rm -rf numba/cuda

"$PYTHON_BIN" -m pip install . --no-warn-script-location

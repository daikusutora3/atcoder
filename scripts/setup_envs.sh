#!/usr/bin/env bash
# One-shot setup for AtCoder 2025/10 Python environments.
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REQUIREMENTS_DIR="$PROJECT_ROOT/scripts/requirements"
NUMBA_SCRIPT="$PROJECT_ROOT/scripts/install_patched_numba.sh"

PYENV_ROOT="${PYENV_ROOT:-$PROJECT_ROOT/.pyenv}"
PYENV_BIN="$PYENV_ROOT/bin/pyenv"
CPYTHON_VERSION="3.13.7"
PYPY_VERSION="pypy3.11-7.3.20"

CPYTHON_ENV="$PROJECT_ROOT/.cp313"
PYPY_ENV="$PROJECT_ROOT/.pypy"

PIP_FLAGS=(--trusted-host pypi.org --trusted-host files.pythonhosted.org)

log() {
  printf "\n[%s] %s\n" "$(date '+%H:%M:%S')" "$*"
}

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "error: required command not found: $1" >&2
    exit 1
  fi
}

ensure_pyenv() {
  if [[ -x "$PYENV_BIN" ]]; then
    log "pyenv already present at $PYENV_ROOT"
    return
  fi
  log "Cloning pyenv into $PYENV_ROOT"
  git clone https://github.com/pyenv/pyenv.git "$PYENV_ROOT"
}

ensure_pyenv_python() {
  local version="$1"
  local target_dir="$PYENV_ROOT/versions/$version"
  if [[ -d "$target_dir" ]]; then
    log "pyenv version $version already installed"
    return
  fi
  log "Installing $version via pyenv (may take a while)"
  "$PYENV_BIN" install -s "$version"
}

python_path() {
  local version="$1"
  local binary_name="$2"
  echo "$PYENV_ROOT/versions/$version/bin/$binary_name"
}

create_env() {
  local python_bin="$1"
  local env_path="$2"
  log "Creating virtualenv at $env_path (python: $python_bin)"
  rm -rf "$env_path"
  uv venv --python "$python_bin" "$env_path"
}

bootstrap_env() {
  local python_bin="$1"
  log "Upgrading pip/setuptools for $python_bin"
  "$python_bin" -m pip install --upgrade pip setuptools "${PIP_FLAGS[@]}"
}

install_requirements() {
  local python_bin="$1"
  local requirements_file="$2"
  log "Installing requirements from $requirements_file"
  "$python_bin" -m pip install -r "$requirements_file" "${PIP_FLAGS[@]}"
}

verify_import() {
  local python_bin="$1"
  local import_stmt="$2"
  log "Verifying import: $import_stmt"
  "$python_bin" -c "$import_stmt"
}

run_numba_patch() {
  local python_bin="$1"
  log "Applying numba CUDA-disabled install for $python_bin"
  "$NUMBA_SCRIPT" "$python_bin"
}

# --- main --------------------------------------------------------------------

cd "$PROJECT_ROOT"
unset VIRTUAL_ENV VIRTUAL_ENV_PROMPT || true

require_command uv
require_command git
require_command curl

ensure_pyenv

export PYENV_ROOT
export PATH="$PYENV_ROOT/bin:$PATH"

ensure_pyenv_python "$CPYTHON_VERSION"
ensure_pyenv_python "$PYPY_VERSION"

CPYTHON_BIN="$(python_path "$CPYTHON_VERSION" python3.13)"
PYPY_BIN="$(python_path "$PYPY_VERSION" pypy3)"

for bin in "$CPYTHON_BIN" "$PYPY_BIN"; do
  if [[ ! -x "$bin" ]]; then
    echo "error: python interpreter not found or not executable: $bin" >&2
    exit 1
  fi
done

create_env "$CPYTHON_BIN" "$CPYTHON_ENV"
if ! "$CPYTHON_ENV/bin/python" -m pip --version >/dev/null 2>&1; then
  log "Bootstrapping pip via ensurepip (CPython)"
  "$CPYTHON_ENV/bin/python" -m ensurepip --upgrade
fi
bootstrap_env "$CPYTHON_ENV/bin/python"
install_requirements "$CPYTHON_ENV/bin/python" "$REQUIREMENTS_DIR/cp313.txt"
run_numba_patch "$CPYTHON_ENV/bin/python"
verify_import "$CPYTHON_ENV/bin/python" "from atcoder.segtree import SegTree"

create_env "$PYPY_BIN" "$PYPY_ENV"
if ! "$PYPY_ENV/bin/pypy3" -m pip --version >/dev/null 2>&1; then
  log "Bootstrapping pip via ensurepip (PyPy)"
  "$PYPY_ENV/bin/pypy3" -m ensurepip --upgrade
fi
bootstrap_env "$PYPY_ENV/bin/pypy3"
install_requirements "$PYPY_ENV/bin/pypy3" "$REQUIREMENTS_DIR/pypy.txt"
verify_import "$PYPY_ENV/bin/pypy3" "from atcoder.segtree import SegTree"

log "All environments provisioned successfully."

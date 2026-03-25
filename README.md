# koi-net-node-template

# Quick Start

## 1. Create repo from template
Click `Use this template` -> `Create a new repository` and finish the set up process.

## 2. Clone repo
Clone the resulting repository
```
git clone <your-github-url-here>
```

## 3. Set up virtual environment
**Recommended:**
[Install UV](https://docs.astral.sh/uv/getting-started/installation/) and run: 

```
uv venv
```

Alternatively, use the built-in virtual environment: 
```
python -m venv .venv
```
---

Activate the new environment for Mac/Linux:
```
source .venv/bin/activate
```
or for Windows:
```
.venv\Scripts\activate
```

## 4. Configure repo

Pick a name for your node, and update the package directory name in `src/`, `node_name` in `config.py`, and `name` in `pyproject.toml`. This name should be all lowercase letters separated by hyphens (or underscores for the package name in `src/`).

Set the node description, author fields, and project URL in the `pyproject.toml`.

## 5. Install your node package
This will install your node in editable mode, reflecting changes as you edit the source code.
```
uv pip install --editable .
```
or
```
pip install --editable .
```

## 6. Set up .env file
Rename `.env.example` to `.env` and set a password to encrypt the node's private key. Make sure that this file IS NOT committed by git.
## 7. Run node
```
python -m koi_net_<YOUR_NODE_NAME>_node
```

## 8. Publish node as a package
This repo comes with a workflow to publish to PyPI. You'll need a PYPI account linked to your GitHub account, and first follow [this tutorial](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/) to set up a project configured for deployment.

Once you have a project page, update the URL on line 38 of `.github/workflows/publish-to-pypi.yml`. Now whenever a tag is created of the form `v*.*.*` that commit will automatically be published to PyPI. Make sure that the version specifier in `pyproject.toml` matches the version in the tag you are using.

# Modifying this Node
Take a look at the [koi-net repo](https://github.com/BlockScience/koi-net) for documentation about the koi-net package and developing nodes. This template provides the basic structure for a full node setup. You'll likely want to start by modifying `config.py` with the RID types your node deals with, and adding your own knowledge handlers (see example in `custom_handler.py`).

# Adding a License
This template doesn't contain any license by default. If you add a `LICENSE` file, make sure to update your `pyproject.toml` with the following line:
```
license = {file = "LICENSE"}
```

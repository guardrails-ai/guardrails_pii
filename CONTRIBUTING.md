# Guardrails Validator Template

## How to create a Guardrails Validator
- On the top right of the page, click "Use this template", select "create a new repository"  and set a name for the package.  See [Naming Conventions](#naming-conventions) below.
- Clone down the new repository.
- Modify the class in [validator/main.py](validator/main.py) with source code for the new validator
    - Make sure that the class still inherits from `Validator` and has the `register_validator` annotation.
    - Set the `name` in the `register_validator` to the name of the repo prefixed with your org as a namespace and set the appropriate data type.
- Change [validator/__init__.py](validator/__init__.py) to your new Validator classname instead of ValidatorTemplate
- Perform a self install with `make dev` or `pip install -e ".[dev]"`
- Locally test the validator with the [test instructions below](#testing-and-using-your-validator)
- Modify the README and follow the Validator Card format; you can find an example [here](https://github.com/guardrails-ai/lowercase/blob/main/README.md)

* Note: This package uses a pyproject.toml file, on first run, run `make dev` to pull down and install all dependencies

### Naming Conventions
1. Avoid using `is` and `bug`
2. Use snake_case: i.e. `_` to separate words. e.g. valid_address
3. For the description of the repo, write one sentence that says what the validator does; should be the same as the description in the pydoc string.
4. When annotating the class use the `{namespace}/{validator_name}` pattern: e.g. `@register_validator(name=“guardrails/valid_address”)`

### Testing and using your validator
- Open [test/test-validator.py](test/test-validator.py) to test your new validator 
- Import your new validator and modify `ValidatorTestObject` accordingly
- Modify the TEST_OUTPUT and TEST_FAIL_OUTPUT accordingly
- Run `python test/test-validator.py` via terminal, make sure the returned output reflects the input object 
- Write advanced tests for failures, etc.

## Upload your validator to the validator hub
- Update the [pyproject.toml](pyproject.toml) file and make necessary changes as follows:
    - Update the `name` field to the name of your validator
    - Update the `description` field to a short description of your validator
    - Update the `authors` field to your name and email
    - Add/update the `dependencies` field to include all dependencies your validator needs.
- If there are are any post-installation steps such as downloading tokenizers, logging into huggingface etc., update the [post-install.py](validator/post-install.py) file accordingly.
- You can add additional files to the [validator](validator) directory, but don't rename any existing files/directories.
    - e.g. Add any environment variables (without the values, just the keys) to the [.env](.env) file.
- Ensure that there are no other dependencies or any additional steps required to run your validator.

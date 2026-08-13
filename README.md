<!-- ----------------------------------------------------------------------------
  Copyright (c) 2026 Contributors to the Eclipse Foundation

  See the NOTICE file(s) distributed with this work for additional
  information regarding copyright ownership.

  This program and the accompanying materials are made available under the
  terms of the Apache License Version 2.0 which is available at
  https://www.apache.org/licenses/LICENSE-2.0

  SPDX-License-Identifier: Apache-2.0
----------------------------------------------------------------------------- -->

# Score landing page

> [!NOTE]
> This repository offers a [DevContainer](https://containers.dev/).
> For setting this up read [eclipse-score/devcontainer/README.md#inside-the-container](https://github.com/eclipse-score/devcontainer/blob/main/README.md#inside-the-container).

## Development of the Landing Page

### Use bazelisk for bazel version management
Follow [instructions](https://github.com/bazelbuild/bazelisk) and setup bazelisk to manage your bazel version based on the .bazelversion file.

### Getting IDE support for docs-as-code development

Create the virtual environment via `bazel run //:ide_support`.
If your IDE does not automatically ask you to activate the newly created environment you can activate it.

- In VSCode via `ctrl+p` => `Select Python Interpreter` then select `.venv_docs/bin/python`
- In the terminal via `. .venv_docs/bin/activate`


### Enabeling pre-commit

Pre-commit is supported inside docs-as-code to help with code quality and make developers workflow easier.

Install the hook:
```bash
pre-commit install

# Or install it to run on pre-push via:
pre-commit install --hook-type pre-push
```

Execute the pre-commit manually via `pre-commit run` or `pre-commit run -a` to run it on all files.


## Build Documentation

Use //docs target to build the documentation.
```
$ bazel run //docs:
```

The output directory can be found under ```bazel-bin/docs/docs/_build/html```.

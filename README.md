# napari-sklearn-decomposition
<!-- Commenting these out because they dont work
[![License](https://img.shields.io/pypi/l/napari-sklearn-decomposition.svg?color=green)](https://github.com/jdeschamps/napari-sklearn-decomposition/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-sklearn-decomposition.svg?color=green)](https://pypi.org/project/napari-sklearn-decomposition)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-sklearn-decomposition.svg?color=green)](https://python.org)
[![tests](https://github.com/jdeschamps/napari-sklearn-decomposition/workflows/tests/badge.svg)](https://github.com/jdeschamps/napari-sklearn-decomposition/actions)
[![codecov](https://codecov.io/gh/jdeschamps/napari-sklearn-decomposition/branch/main/graph/badge.svg)](https://codecov.io/gh/jdeschamps/napari-sklearn-decomposition)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-sklearn-decomposition)](https://napari-hub.org/plugins/napari-sklearn-decomposition)
-->

A simple plugin implementing selected matrix decomposition algorithms from [`sklearn.decomposition`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.decomposition) within napari. 
Also includes the Olivetti sample data, for more info see [the sklearn example](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#sphx-glr-auto-examples-decomposition-plot-faces-decomposition-py). 
At present, the following algorithms are implemented:
1. [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
2. [NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html)
3. [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html)

If you'd like another algorithm implemented, please [file an issue]. For more information about signal decomposition and these methods, see [the sklearn User Guide](https://scikit-learn.org/stable/modules/decomposition.html). 

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/plugins/stable/index.html
-->

## Installation

This plugin is experimental and pre-alpha. At the moment you can only install from this repository.

To install latest development version :

    pip install git+https://github.com/jdeschamps/napari-sklearn-decomposition.git


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-sklearn-decomposition" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/jdeschamps/napari-sklearn-decomposition/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

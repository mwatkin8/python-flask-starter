Python 3.6 and Go 1.9.2 should be installed and the following steps should be followed to run the suite:

Use the virtualenv tool to create a virtual environment in which to run the program with the command: virtualenv vmcTS-venv. If virtualenv is not installed locally then use the command: pip3.6 install virtualenv. Activate the new virtual environment using the command: . vmcTS-venv/bin/activate.

Use the command: pip3.6 install -r requirements.txt to install system dependencies.

Within the vmc-test-suite directory, use the command: python app.py to activate the web server locally. Navigate your web browser to http://0.0.0.0:5000/ in order to view the web tool.

Once rendered, the tool requires a decomposed vcf file in order to transform it properly (per requirement by the VMC). A test file HG00177_sml.vcf has been provided which is taken from the 1000 Genomes project and can be found in the vmc-test-suite directory.

To deactivate vmcTS-venv when finished using the test suite, use the command: deactivate.

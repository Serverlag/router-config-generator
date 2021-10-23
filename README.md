## Router Config Generator

*A basic router configuration generator that reduces configuration time and complexity.
This configuration generator aims to make it easier for those new to enterprise grade routers to deploy reliable and well performing configurations.
This configuration tool does have some base hardening done based on industry standards, however should not be assumed that it generates secure configurations.
Network engineers should always review the outputted configuration to ensure its hardened before deploying into a production environment.*

### Getting started

```sh
python -m venv router-config-generator
python -m pip install --upgrade pip
pip install -r requirements.txt
```

After everything is up and running, visit http://127.0.0.1:5000.
## Router Config Generator

*A basic router configuration generator that reduces configuration time and complexity.
This configuration generator aims to make it easier for those new to enterprise routers to deploy reliable and well performing configurations.
This configuration tool does have some base hardening done based on industry standards, however should not be assumed that it generates secure configurations.
Network engineers should always review the outputted configuration to ensure its hardened before deploying into a production environment.*

Current supported routers:

* Cisco 880 Series
* Cisco 890 Series
* Cisco 1900 Series
* Cisco 2900 Series

### Getting started
#### Ubuntu:
```sh
sudo apt install -y python3 python3-pip python3-venv git
git clone https://github.com/Serverlag/router-config-generator.git
cd router-config-generator
python3 -m venv router-config-generator
source router-config-generator/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
cd router-config-generator
npm install -D tailwindcss
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

After everything is up and running, visit http://server_ip_address:5000.

#### Using Docker (Ubuntu)

```sh
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
git clone https://github.com/Serverlag/router-config-generator.git
cd router-config-generator
sudo docker build -t rcg .
sudo docker run -d -p 5000:5000 --name router-config-generator rcg
```

visit http://server_ip_address:5000
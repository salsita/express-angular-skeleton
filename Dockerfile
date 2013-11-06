FROM realyze/ubuntu-node-sshd

MAINTAINER Tomas Brambora "tomas@salsitasoft.com"

# Install all the Node-ish dependencies.
RUN npm install -g grunt-cli
RUN npm install -g karma
Run npm install -g bower
Run npm install -g phantomjs
Run npm install -g coffee-script

# Install the necessary commands.
RUN apt-get install -y git
# Required by PhantomJS.
RUN apt-get install -y fontconfig

# Install Supervisord.
RUN apt-get install -y python-setuptools
RUN easy_install supervisor


# Share npm cache (speeds things up).
RUN npm config set cache /data/.npm --global

# Expose Express.js port.
EXPOSE 3000

# Expose SSHD port.
EXPOSE 22

# Add the project sources to the image.
ADD . /srv/project/

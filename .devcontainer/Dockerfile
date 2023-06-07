FROM ubuntu:20.04

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get -y install gcc gdb valgrind python3.8 python3-pip git
RUN apt-get -y install curl zsh man-db locales && \
    pip3 install --no-cache-dir pycodestyle==2.8.0 pre-commit && \
    git clone https://github.com/alx-tools/Betty.git /home/Betty

# Install betty
RUN locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    cd /home/Betty && ./install.sh

# Install zsh `robbyrussell` theme
RUN zsh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" ||true

# Set Zsh as the default shell
ENV SHELL="/bin/zsh" PATH="/usr/local/bin:$PATH"

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

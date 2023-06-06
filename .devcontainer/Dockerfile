FROM ubuntu:20.04

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update
RUN apt-get -y install python3.8 python3-pip zsh curl git
RUN pip3 install pycodestyle==2.8.0

# Install zsh `robbyrussell` theme
RUN zsh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" ||true

# Set Zsh as the default shell
ENV SHELL /bin/zsh

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# TODO: add / gcc gdb pdb betty pre-commit

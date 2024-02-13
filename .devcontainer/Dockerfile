FROM osrf/ros:humble-desktop-jammy
# Add vscode user with same UID and GID as your host system
# (copied from https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

COPY .bashrc /home/$USERNAME/.bashrc
#RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
RUN mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory 
# && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

#https://pagepro.co/blog/autocomplete-git-commands-and-branch-names-in-terminal/
COPY .git-completion.bash /home/$USERNAME/.git-completion.bash

# Switch from root to user
USER $USERNAME

# Add user to video group to allow access to webcam
RUN sudo usermod --append --groups video $USERNAME

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Install python packages
RUN sudo apt update && sudo apt install -y \
python3-pip

RUN pip3 install \
numpy \
exudyn \
roboticstoolbox-python

# Install Git
RUN sudo apt install -y git

# Rosdep update
RUN rosdep update

WORKDIR /martinDock2Ros2/workspace

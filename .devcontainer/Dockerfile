FROM osrf/ros:jazzy-desktop

ARG USERNAME=ubuntu

RUN apt-get update \
    && apt-get install --yes --no-install-recommends sudo \
    && echo "${USERNAME} ALL=(root) NOPASSWD:ALL" \
        > "/etc/sudoers.d/${USERNAME}" \
    && chmod 0440 "/etc/sudoers.d/${USERNAME}" \
    && rm -rf /var/lib/apt/lists/*


RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

USER root

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Install Git and other ubuntu stuff
RUN sudo apt install -y \
    software-properties-common \
    build-essential \
    cmake \
    git \
    git-lfs \
    wget \
    nano \
    eza \
    unzip \
    mesa-utils \
    xterm \
    ripgrep \
    htop \
    bat \
    less \
    zsh

# python required dependencies
COPY requirements.txt /tmp/requirements.txt

# install python system packages
RUN apt install -y python3-pip python3-venv

# initialize virtual environment
ENV VIRTUAL_ENV=/python/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
RUN python3 -m venv "${VIRTUAL_ENV}"

# install python dependencies inside venv
# NOTE: dont use `python3 -m pip`!
#		`pip` resolves to `$VIRTUAL_ENV`/bin/pip,
# 		while the former does not (nessacerely)!
RUN pip install --upgrade pip setuptools wheel
RUN pip install --requirement /tmp/requirements.txt


# Rosdep update
RUN rosdep update

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN export PATH="/home/vscode.local/bin:$PATH"
#RUN source ~/.bashrc   

# Switch from root to user
USER $USERNAME
WORKDIR /martinDock2Ros2/workspace


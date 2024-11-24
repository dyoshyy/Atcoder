FROM python:3.8.2

ARG USERNAME=vscode
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update \
    && groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get -y install sudo \ 
    && echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# Python3, PyPy3の環境想定
RUN apt-get update && \
    apt-get install -y python3-pip pypy3 nodejs npm

# pythonライブラリをインストール
COPY requirements.txt /tmp/
RUN python -m pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

# コンテスト補助ツールをインストール
RUN pip3 install online-judge-tools
RUN npm install -g atcoder-cli

# .bashrcにエイリアスを追加
RUN echo '# PyPy3でのテスト実施' >> ~/.bashrc && \
    echo "alias test='oj t -c \"pypy3 main.py\" -d ./tests/'" >> ~/.bashrc && \
    echo '# Pythonでのテスト実施' >> ~/.bashrc && \
    echo "alias test2='oj t -c \"python3 main.py\" -d ./tests/'" >> ~/.bashrc && \
    echo '# PyPy3での解答提出' >> ~/.bashrc && \
    echo "alias sb='acc s main.py -- --guess-python-interpreter pypy'" >> ~/.bashrc && \
    echo '# Pythonでの解答提出' >> ~/.bashrc && \
    echo "alias sb2='acc s main.py'" >> ~/.bashrc && \
    echo '# コンテストフォルダへ移動' >> ~/.bashrc && \
    echo "alias c='cd contest'" >> ~/.bashrc && \
    echo '# main.pyを開く' >> ~/.bashrc && \
    echo "alias o='code main.py'" >> ~/.bashrc && \
    echo '# 出力確認用' >> ~/.bashrc && \
    echo "alias d='python main.py'" >> ~/.bashrc

# accの初期設定
RUN acc config default-task-choice all
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y wget git
RUN useradd -m user
USER user
WORKDIR /home/user
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& sh ./Miniconda3-latest-Linux-x86_64.sh -b -f \
	&& rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH $PATH:/home/user/miniconda3/bin

FROM Mdnoor786/lionuserbot:latest

#clonning repo 
RUN git clone https://github.com/mdnoor786/lionuserbot.git /root/lion
#working directory 
WORKDIR /root/lion

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/lion/bin:$PATH"

CMD ["python3","-m","lion"]

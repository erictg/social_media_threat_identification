FROM logstash

RUN logstash-plugin install logstash-input-tcp

RUN logstash-plugin install logstash-output-elasticsearch

RUN logstash-plugin install logstash-output-file

RUN logstash-plugin install logstash-output-stdout

COPY logstash.conf /var/config/

CMD ["-f", "/var/config/logstash.conf"]
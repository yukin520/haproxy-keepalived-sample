
# HAProxy-KeepAlived Sample

HAProxyとKeepalivedの動作をサクッと確認するためのリポジトリです。
以下の構成の環境を立ち上げることができます。

![architecture](./img/architecture.drawio.svg)

## how to use

1. 本リポジトリをクローンし、dokcer composeで立ち上げます。

    ```shell
    $ git clone https://github.com/yukin520/haproxy-keepalived-sample.git
    $ cd haproxy-keepalived-sample
    $ docker compose up -d
    ```

2. clientコンテナに入ります。clientコンテナからVIPに対してHTTPリクエストを投げることで挙動を確認することができます。

    ```shell
    $ docker exec -it client /bin/bash
    ```

    ```shell
    $ curl http://10.0.0.50:80
    ```

3. 利用を終了する際は、dokcer compseで環境を破棄します。

    ```shell
    $ docker compose down
    ```


## 参考

[Building a High Availability Cluster with HAProxy, Keepalived, and Docker: A Step-by-Step Guide](https://medium.com/@yahyasghiouri1998/building-a-high-availability-cluster-with-haproxy-keepalived-and-docker-a-step-by-step-guide-9325f4ac8aa7)
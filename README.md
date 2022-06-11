# Nginx-Django-Uwsgi

## Django

### 搭建虚拟环境

* 安装虚拟环境的命令

  >sudo pip install vitualenv
  >
  >sudo pip install virtualenvwrapper

  安装虚拟环境后，如果提示找不到mkvirtualenv命令，需要配置环境变量

  >```shell
  ># 1、创建目录用来存放虚拟环境
  >mkdir 
  >$HOME/.virtualenvs
  >
  ># 2、打开~/.bashrc文件，并添加如下：
  >export WORKON_HOME=$HOME/.virtualenvs
  >source /usr/local/bin/virtualenvwrapper.sh
  >
  ># 3、运行
  >source ~/.bashrc
  >```

* 创建虚拟环境的命令

  如果不指定python的版本，默认安装的是python2的虚拟环境

  * 在python2创建虚拟环境

    >```shell
    >mkvirtualenv 虚拟环境名称
    >例 ：
    >mkvirtualenv py_django
    >```

  * 在python3创建虚拟环境

    >```
    >mkvirtualenv -p python3 虚拟环境名称
    >例 ：
    >mkvirtualenv -p python3 py3_django
    >```

* 提示：

  创建虚拟环境需要连网，创建成功后，会在这个虚拟环境上，工作在虚拟环境上，提示符前边将会出现虚拟环境名称

### 使用虚拟环境

查看虚拟环境（查看所有虚拟环境）

>workon

使用虚拟环境

>workon 虚拟环境名称
>
>如：
>
>workon py3_django

退出虚拟环境

>deactivate

删除虚拟环境命令

>rmvirtualenv 虚拟环境名称
>
>deactivate # 退出
>
>rmvirtualenv py3_django 

### 虚拟环境中安装包

提示 : 工具包安装的位置 :

python2版本下：

`~/.virtualenvs/py_flask/lib/python2.7/site-packages/`

python3版本下：

`~/.virtualenvs/py3_flask/lib/python3.5/site-packages`

python3版本下安装django-1.11.11的包 :

```
pip install 包名称

例 : 安装django-1.11.11的包
pip install django==1.11.11
```

查看虚拟环境中安装的包 :

```
pip list
```

### 安装django

```
pip install django
```

### 创建django项目

```shell
django-admin start bookmanager
```

文件夹django-test下，含有一个bookmanager的django项目

### 配置django项目

更改setting.py里面的ALLOWED_HOSTS,把服务器的ip加入进去，有域名的话，也把域名加入

## Uwsgi

安装uwsgi

```
pip install uwsgi
```

安装好以后可以在项目根目录下(manage同级)使用

>uwsgi --http :8000 --module 对应的名称(在你项目目录下与settings同级).wsgi

效果和 python3 manage.py runserver 0.0.0.0:8000一样,去浏览器用你的公网ip加上8000访问下，成功说明可跳过下一步测试直接新建uwsgi.ini编辑。

下面来试一下uwsgi是否好使：
找个位置新建一个py文件，就叫test.py好了,写入以下内容，(本仓库下的uwsgitest目录下test.py)

>def application(env, start_response):
>    start_response('200 OK', [('Content-Type','text/html')])
>    return [b"Hello Uwsgi"]

然后输入以下命令启动uwsgi，把这个部署到某个端口，以9090端口为例

>uwsgi --http :9090 --wsgi-file uwsgi.py

这时会出现spawned uWSGI worker 1 (and the only) (pid: 11812, cores: 1)
找个浏览器，访问http://<你的服务器ip>:9090/，不出意外的话你会看到Hello Uwsgi的字样，说明uwsgi能正常运行。

项目的目录下创建bookmanager.ini,内容如下(bookmanager.ini位于仓库下django-test/bookmanager目录中)

>```
>[uwsgi]
>chdir=/home/ubuntu/work-space/django-test/bookmanager
>module=bookmanager.wsgi
>
>socket = 127.0.0.1:8000
>http = :9000
>
>master=True
>processes=4
>threads=2
>vacuum=True
>
># static-map=/static=static  # Django静态文件
>
># 后台启动
># 日志文件位置
>daemonize=%(chdir)/log/uwsgi-8000.log
># 日志文件大小byte
>log-maxsize = 1024000000  # 1G
># 进程id信息
>pidfile = %(chdir)/pid/uwsgi-8000.pd
>
>```

有了uwsgi.ini我们只需要输入uwsgi --ini bookmanager.ini就可以运行，浏览器输入ip地址加:8000端口（先绕过nginx因为还没配置呢），发现可以显示我们的项目了

## Nginx

### 安装Nginx

```shell
sudo apt-get install nginx
```

### 配置Nginx

仓库下目录/etc/nginx有相应的配置信息,主要配置信息存放在conf.d/nginx.conf文件中，html页面存放在html目录下

### 启动nginx

>nginx -v 查看nginx的版本
>
>nginx
>
>nginx restart
>
>nginx -s reload 重新加载nginx
>
>nginx -s stop 停止nginx
>
>nginx -t 检查配置文件

## 参考资料

[(1条消息) Django2+uwsgi+nginx部署详解（Ubuntu18.04）_H_Super_King的博客-CSDN博客](https://blog.csdn.net/weixin_44076955/article/details/108243485?spm=1001.2014.3001.5506)
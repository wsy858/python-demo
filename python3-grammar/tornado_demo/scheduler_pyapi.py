"""
@to  调度操作接口
@author wangshengyong
@date 2018-11-07 14:01:20
"""

import requests
import shlex
import subprocess
import threading

from tornado import escape
from tornado import httpserver
from tornado import ioloop
from tornado import web
from tornado.options import options, define

# 启动方式
# 金融： python scheduler_pyapi.py --port=8001 --yarn_rm_host=sz-5-centos47 --yarn_rm_port=8088
# 集团： python scheduler_pyapi.py --port=8001 --yarn_rm_host=sz-5-centos47 --yarn_rm_port=8088 --yarn_config_path=/home/hadoop/spark-remote/conf/yarn-conf/

# 启动命令参数
define("port", default=8001, help="TCP port to listen on")
define("yarn_rm_host", help="yarn restful host")
define("yarn_rm_port", default=8088, help="yarn restful post")
define("yarn_config_path", default=None, help="yarn配置文件路径，可选参数，集团环境需要指定")


# 请求基类
class BaseRequestHandler(web.RequestHandler):
    SUPPORTED_METHODS = ("PUT", "POST", "GET", "DELETE")
    # def render_xml(self, value):
    #     assert isinstance(value, dict) and len(value) == 1
    #     self.set_header("Content-Type", "application/xml; charset=UTF-8")
    #     name = list(value.keys())[0]
    #     parts = []
    #     parts.append("<" + name + ' xmlns="http://doc.s3.amazonaws.com/2006-03-01">')
    #     self._render_parts(value[name], parts)
    #     parts.append("</" + name + ">")
    #     self.finish('<?xml version="1.0" encoding="UTF-8"?>\n' + "".join(parts))


# 提交任务
class SubmitHandler(BaseRequestHandler):

    def post(self):
        result = {"code": 1, "msg": "OK"}
        data = escape.json_decode(self.request.body)
        print("parameters===============================> " + str(data))
        # 解析参数
        yarn_tags = data.get('yarn_tags')
        if yarn_tags is None:
            self.write({"code": 0, "msg": "yarn_tags can not be empty"})
        numExecutors = data.get('numExecutors', '10')
        driverMemory = data.get('driverMemory', '1g')
        executorMemory = data.get('executorMemory', '2g')
        file = data.get('file')
        if not str(file).startswith("hdfs://"):
            file = "hdfs://ssjlicai" + file
        driverCores = data.get('driverCores', '2')
        executorCores = data.get('executorCores', '2')
        # proxyUser = data.get('proxyUser', 'hadoop')
        name = data.get('name')
        className = data.get('className')
        queue = data.get('queue', 'root.dw')
        conf = data.get('conf')
        args = data.get('args')
        spark_command = "spark2-submit --deploy-mode cluster --master yarn "
        spark_command += " --name '" + name + "'"
        spark_command += " --queue '" + queue + "'"
        spark_command += " --class '" + className + "'"
        spark_command += " --conf spark.submit.deployMode=cluster"
        spark_command += " --conf spark.master=yarn"
        spark_command += " --conf spark.yarn.submit.waitAppCompletion=false"
        spark_command += " --conf spark.executor.instances=" + str(numExecutors)
        spark_command += " --conf spark.executor.cores=" + str(executorCores)
        spark_command += " --conf spark.executor.memory=" + str(executorMemory)
        spark_command += " --conf spark.driver.cores=" + str(driverCores)
        spark_command += " --conf spark.driver.memory=" + str(driverMemory)
        if yarn_tags is not None:
            spark_command += " --conf spark.yarn.tags='" + yarn_tags + "'"
        if conf is not None:
            for key in conf:
                spark_command += " --conf " + key + "=" + str(conf[key])
        spark_command += " '" + file + "' "
        if args is not None:
            for arg in args:
                spark_command += " '" + arg + "' "
        thread = threading.Thread(target=execute_command, args=(spark_command,))
        thread.start()
        result["code"] = 1
        self.write(result)


# 获取任务状态
# 状态： "NEW", "NEW_SAVING", "SUBMITTED", "ACCEPTED", "RUNNING", "FINISHED", "FAILED", "KILLED"
class StatusHandler(BaseRequestHandler):

    def get(self):
        result = {"code": 0, "msg": ""}
        yarn_tags = self.get_argument("yarn_tags")
        app_info = get_application_info(yarn_tags)
        if app_info is not None:
            state = app_info[len(app_info) - 1].get("state")
            result["code"] = 1
            result['data'] = state
        else:
            result["msg"] = "apps info not exists----"
        self.write(result)


# 获取任务日志地址
class GetLogsHandler(BaseRequestHandler):

    def get(self):
        result = {"code": 0, "msg": ""}
        yarn_tags = self.get_argument("yarn_tags")
        app_info = get_application_info(yarn_tags)
        if app_info is not None and len(app_info) > 0:
            logs_url = app_info[len(app_info) - 1].get("trackingUrl")
            result["code"] = 1
            result['data'] = logs_url
        else:
            result["msg"] = "apps info not exists----"
        self.write(result)


# 获取批量任务状态
class BatchStatusHandler(BaseRequestHandler):

    def get(self):
        result = {"code": 0, "msg": ""}
        yarn_tags = self.get_argument("yarn_tags")
        app_info = get_application_info(yarn_tags)
        data = {}
        if app_info is not None:
            for tag in yarn_tags.split(","):
                for app in app_info:
                    if tag == app.get("applicationTags"):
                        data[tag] = app.get("state")
                        break
                if data.get(tag) is None:
                    data[tag] = None
        else:
            for tag in yarn_tags.split(","):
                data[tag] = None
        result["code"] = 1
        result['data'] = data
        self.write(result)


# 中断任务
class KillHandler(BaseRequestHandler):

    def post(self):
        result = {"code": 0, "msg": ""}
        yarn_tags = self.get_argument("yarn_tags")
        application_info = get_application_info(yarn_tags, "NEW,NEW_SAVING,SUBMITTED,ACCEPTED,RUNNING")
        if application_info is not None:
            kill_app(application_info)
            self.write({"code": 1, "msg": "OK"})
        else:
            print("get application_info is empty")
            self.write({"code": 0, "msg": "error"})


# 根据tags获取applicationInfo
# @param yarn_tags : 筛选标识
# @param states ： 筛选状态
def get_application_info(yarn_tags, states=None):
    result = None
    yarn_rm_host = options.yarn_rm_host
    yarn_rm_port = options.yarn_rm_port
    app_get_url = "http://" + yarn_rm_host + ":" + str(
        yarn_rm_port) + "/ws/v1/cluster/apps/?limit=100&applicationTags=" + yarn_tags
    if states is not None:
        app_get_url += "&states=" + states
    http_result = requests.get(app_get_url)
    if http_result.status_code == 200:
        # LogHelper.info("r.text: " + http_result.text)
        try:
            result_json = http_result.json()
            if result_json is not None and result_json["apps"] is not None and len(result_json["apps"]["app"]) > 0:
                result = result_json["apps"]["app"]
        except Exception as e:
            print(e)
    return result


# kill任务
def kill_app(application_info):
    stopped_state = ["FINISHED", "FAILED", "KILLED"]
    for app in application_info:
        app_id = app.get("id")
        state = app.get("state")
        if stopped_state.count(state) == 0:
            command_str = "yarn application -kill " + app_id
            yarn_config_path = options.yarn_config_path
            if yarn_config_path is not None:
                command_str = "yarn --config " + yarn_config_path + " application -kill " + app_id
            print(command_str)
            execute_command(command_str)


# 执行shell等外部命令
def execute_command(cmd_string, cwd=None, shell=False):
    """ 执行一个SHELL命令, 封装了subprocess的Popen方法, 支持超时判断，支持读取stdout和stderr，
       参数:
         cwd: 运行命令时更改路径，如果被设定，子进程会直接先更改当前路径到cwd
         shell: 是否通过shell运行
       Returns: return_code
       """
    if shell:
        cmd_string_list = cmd_string
    else:
        cmd_string_list = shlex.split(cmd_string)

    sub = subprocess.Popen(cmd_string_list, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, shell=shell, bufsize=4096)
    for info in sub.communicate():
        print(info.decode())
    print("========================================command return code: " + str(sub.returncode))
    return sub.returncode


# 初始化app，配置映射路由
class S3Application(web.Application):
    def __init__(self):
        web.Application.__init__(
            self,
            [
                (r"/sparkapi/job_submit/", SubmitHandler),
                (r"/sparkapi/job_status/", StatusHandler),
                (r"/sparkapi/job_batch_status/", BatchStatusHandler),
                (r"/sparkapi/job_kill/", KillHandler),
                (r"/sparkapi/job_logs/", GetLogsHandler),
            ],
        )


# 监听端口，启动服务
def start(port):
    if options.yarn_rm_host is None:
        print("yarn_rm_host启动参数不能为空")
        return
    application = S3Application()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(port)
    print("启动成功---")
    ioloop.IOLoop.current().start()


# main入口
if __name__ == "__main__":
    options.parse_command_line()
    start(options.port)

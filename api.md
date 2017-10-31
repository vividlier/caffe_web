# 接口文档//暂定
## 注册
post /user/signUp  
request:
```json
{
    "username":"xxx",
    "password":"xxx"
}
```
response:
```json
{
    "status":"ok",
    "data":{
        "user_id":"xx",
        "username":"xxx"
    }
}
```
```
header:set-cookie
```
## 登录
post /user/signIn  
request:
```json
{
    "username":"xxx",
    "password":"xxx"
}
```
response:
```json
{
    "status":"ok",
    "data":{
        "user_id":"xx",
        "username":"xxx"
    }
}
```
```
header:set-cookie
```
## 获取project页列表
post /project/getProjectListByUser  
request:
```json
{
    "user_id":"xx"
}
```
response:
```json
{
    "status":"ok",
    "data":{
        "project_list":[
            {
                "project_id":"xx",
                "project_name":"xxx",
                "updated_time":"xxx"
            }
        ]
    }
}
```
## 获取project详情
post /project/getProjectDetailById  
request:
```json
{
    "project_id":"xx"
}
```
response:
```json
{
    "status":"ok",
    "data":{
        "project_ame":"xxx",
        "dataset_name":"xxx",
        "net_name":"xxx",
        "solver_name":"xxd"
    }
}
```
## 新建project
post /project/createProject  
request:
```json
{
    "project_name":"xxx"
}
```
response:
```json
{
    "status":"ok",
    "data":{}
}
```
## 获取dataset列表
## 新建dataset
## 修改dataset
## 上传dataset //后续可以修改成通用上传接口

# 接口文档//暂定
## 注册
POST **/user/signUp**

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
    "user_id": "用户id",
    "username": "用户名称"
}
```
```
header: Set-Cookie

Location: /user/<int:id>

创建成功会返回 201 CREATED

创建失败（可能是用户名重名）会返回 400 BAD REQUEST
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
    "status":"200",
    "data":{
        "user_id":"xx",
        "username":"xxx"
    }
}
```
```
header:set-cookie

登陆失败会返回 400 BAD REQUEST
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
post /dataset/getDatasetListByUser
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
        "dataset_list":[
            {
                "dataset_id":"xx",
                "dataset_name":"xxx",
                "dataset_size":"xxx",
                "formate":"xxx",
                "path":"xxx",
                "description":"xxx",
                "created_time":"xxx"
            }
        ]
    }
}
```
## 新建dataset
post /dataset/createDataset
request:
```json
{
    "dataset_name":"xxx",
    "format":"xxx",
    "description":"xxx"
}
```
response:
```json
{
    "status":"ok",
    "data":{}
}
```
## 修改dataset
post /dataset/updateDataset
request:
```json
{
    "dataset_id":"xx",
    "dataset_name":"xxx",
    "format":"xxx",
    "description":"xxx"
}
```
response:
```json
{
    "status":"ok",
    "data":{}
}
```
## 上传dataset //后续可以修改成通用上传接口
post /dataset/uploadDataset
request:
```json
{
    "file":{}
}
```
response:
```json
{
    "status":"ok",
    "data":{}
}
```
## 获取net
## 创建net
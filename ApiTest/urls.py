"""ApiTest re_path Configuration

The `re_pathpatterns` list routes re_paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/re_paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to re_pathpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to re_pathpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another re_pathtconf
    1. Import the include() function: from django.conf.re_paths import re_path, include
    2. Add a re_path to re_pathpatterns:  re_path(r'^blog/', include('blog.re_paths'))
"""
from django.urls import path, re_path
from django.contrib import admin
from MyApp.views import *
from MyApp.views_tools import *
from MyApp.views_test import *
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^welcome/$',welcome) , #获取菜单
    re_path(r'^$',home),
    re_path(r'^home/$', home),  # 进入首页
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/(?P<ooid>.*)/$",child),  # 返回子页面
    re_path(r'^login/$', login),  # 进入登陆页面
    re_path(r'^login_action/$', login_action),  # 登陆
    re_path(r'^register_action/$', register_action),  # 注册
    re_path(r'^accounts/login/$', login),  # 非登陆状态自动跳回登陆页面
    re_path(r'^logout/$', logout),  # 退出
    re_path(r'^pei/$', pei),  # 匿名吐槽
    re_path(r'^help/$', api_help),  # 进入到帮助文档
    re_path(r'^project_list/$', project_list),  # 进入项目列表
    re_path(r'^delete_project/$', delete_project),  # 删除项目
    re_path(r'^add_project/$', add_project),  #新增项目
    re_path(r'^apis/(?P<id>.*)/$', open_apis),  # 进入接口库
    re_path(r'^cases/(?P<id>.*)/$', open_cases),  # 进入用例设置
    re_path(r'^project_set/(?P<id>.*)/$', open_project_set),  # 进入项目设置
    re_path(r'^save_project_set/(?P<id>.*)/$', save_project_set),  # 保存项目设置
    re_path(r'^project_api_add/(?P<Pid>.*)/$', project_api_add),  # 新增接口
    re_path(r'^project_api_del/(?P<id>.*)/$', project_api_del),  # 删除接口
    re_path(r'^save_bz/$', save_bz),  # 保存备注
    re_path(r'^get_bz/$', get_bz),  # 获取备注
    re_path(r'^Api_save/$', Api_save),  # 保存接口
    re_path(r'^get_api_data/$', get_api_data),  # 获取接口数据
    re_path(r'^Api_send/$', Api_send),  # 调试层发送请求
    re_path(r'^copy_api/$', copy_api),  # 复制接口
    re_path(r'^error_request/$', error_request),  # 调用异常测试接口
    re_path(r'^Api_send_home/$', Api_send_home),  # 首页发送请求
    re_path(r'^get_home_log/$', get_home_log),  # 获取最新请求记录
    re_path(r'^get_api_log_home/$', get_api_log_home),  # 获取完整的单一的请求记录数据
    re_path(r'^home_log/(?P<log_id>.*)/$', home),  # 再次进入首页，这次要带着请求记录
    re_path(r'^add_case/(?P<eid>.*)/$', add_case),  # 增加用例
    re_path(r'^del_case/(?P<eid>.*)/(?P<oid>.*)/$', del_case),  # 删除用例
    re_path(r'^copy_case/(?P<eid>.*)/(?P<oid>.*)/$', copy_case),  # 复制用例
    re_path(r'^save_case_concurrent/$',save_case_concurrent),# 保存用例并发设置

    re_path(r'^concurrent_cases/(?P<pid>.*)/$', concurrent_cases),  # 用例并发
    re_path(r'^look_concurrent_report/(?P<pid>.*)/$', look_concurrent_report),  # 查看用例并发报告
    re_path(r'^get_step_report/$',get_step_report), #获取具体step数据

    re_path(r'^get_small/$', get_small),  # 获取小用例步骤的列表数据
    re_path(r'^user_upload/$', user_upload),  # 上传头像
    re_path(r'^add_new_step/$', add_new_step),  # 新增小步骤接口
    re_path(r'^delete_step/(?P<eid>.*)/$', delete_step),  # 删除小步骤接口
    re_path(r'^get_step/$', get_step),  #获取小步骤
    re_path(r'^save_step/$', save_step),  # 保存小步骤
    re_path(r'^step_get_api/$', step_get_api),  # 步骤详情页获取接口数据
    re_path(r'^Run_Case/$', Run_Case),  # 运行大用例
    re_path(r'^look_report/(?P<eid>.*)/$', look_report),  # 查看报告
    re_path(r'^save_project_header/$', save_project_header),  # 保存项目公共请求头
    re_path(r'^save_caes_name/$', save_caes_name),  # 保存用例名字
    re_path(r'^save_project_host/$', save_project_host),  # 保存项目公域名
    re_path(r'^project_get_login/$', project_get_login),  # 获取项目登陆态接口
    re_path(r'^project_login_save/$', project_login_save),  # 保存项目登陆态接口
    re_path(r'^project_login_send/$', project_login_send),  # 调试请求登陆态接口
    re_path(r'^Home_save_api/$', Home_save_api),  # 首页保存请求数据
    re_path(r'^search/$', search),  # 首页搜索功能
    re_path(r'^global_data/(?P<id>.*)/$', global_data),  # 进入全局变量设页面

    re_path(r'^global_data_add/$', global_data_add),  # 增加一个全局变量组
    re_path(r'^global_data_delete/$', global_data_delete),  # 删除一个全局变量组
    re_path(r'^global_data_save/$', global_data_save),  # 保存一个全局变量组
    re_path(r'^global_data_change_check/$', global_data_change_check),  # 更改项目的生效变量组

    re_path(r'^encyption_save/$',encyption_save), #加密配置保存

    re_path(r'^cert_upload/(?P<pid>.*)/$', cert_upload),  # 上传证书


    # ------------ 测试用接口
    re_path(r'^test_login_A/$', test_login_A),
    re_path(r'^test_login_B/$', test_login_B),
    re_path(r'^test_api_A/$', test_api_A),
    re_path(r'^test_api_B/$', test_api_B),

    # ------------ 小工具 --------------- #
    re_path(r'^tools_zhengjiao/$', zhengjiao),  # 进入小公举页面
    re_path(r'^zhengjiao_play/$', zhengjiao_play),  # 正交工具运行
    re_path(r'^zhengjiao_excel/$', zhengjiao_excel),  # 正交工具导出

]


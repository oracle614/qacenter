# Generated by Django 2.0.3 on 2018-08-10 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavTd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.CharField(max_length=20, verbose_name='用户')),
            ],
            options={
                'verbose_name': '我收藏的事务',
                'db_table': 'Data_Fav_Td',
            },
        ),
        migrations.CreateModel(
            name='ModuleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('module_name', models.CharField(max_length=50, verbose_name='模块名称')),
                ('test_user', models.CharField(max_length=50, verbose_name='测试人员')),
                ('dev_user', models.CharField(max_length=50, verbose_name='开发人员')),
                ('simple_desc', models.CharField(max_length=100, null=True, verbose_name='简要描述')),
            ],
            options={
                'verbose_name': '模块信息',
                'db_table': 'Data_ModuleInfo',
            },
        ),
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('project_name', models.CharField(max_length=50, verbose_name='项目名称')),
                ('responsible_name', models.CharField(max_length=20, verbose_name='项目负责人')),
                ('test_user', models.CharField(max_length=100, verbose_name='测试人员')),
                ('simple_desc', models.CharField(max_length=100, null=True, verbose_name='简要描述')),
            ],
            options={
                'verbose_name': '项目信息',
                'db_table': 'Data_ProjectInfo',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.CharField(max_length=20, verbose_name='用户')),
                ('request', models.TextField(verbose_name='请求参数')),
                ('result', models.TextField(verbose_name='返回结果')),
            ],
            options={
                'verbose_name': '调用历史',
                'db_table': 'Data_record',
            },
        ),
        migrations.CreateModel(
            name='TdInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=50, verbose_name='事务名称')),
                ('td_url', models.CharField(max_length=200, verbose_name='事务地址')),
                ('author', models.CharField(max_length=20, verbose_name='编写人员')),
                ('run_count', models.IntegerField(default=0, verbose_name='调用次数')),
                ('params', models.TextField(verbose_name='入参列表')),
                ('instruction', models.TextField(verbose_name='帮助说明')),
                ('belong_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.ModuleInfo')),
                ('belong_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.ProjectInfo')),
            ],
            options={
                'verbose_name': '事务信息',
                'db_table': 'Data_TdInfo',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=30, verbose_name='姓名')),
                ('type', models.IntegerField(default=1, verbose_name='角色')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('status', models.IntegerField(default=1, verbose_name='有效/无效')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'UserInfo',
            },
        ),
        migrations.AddField(
            model_name='record',
            name='belong_td',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.TdInfo'),
        ),
        migrations.AddField(
            model_name='moduleinfo',
            name='belong_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.ProjectInfo'),
        ),
        migrations.AddField(
            model_name='favtd',
            name='belong_td',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataManager.TdInfo'),
        ),
    ]

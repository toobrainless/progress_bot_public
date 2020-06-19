import peewee
import datetime as d

db = peewee.SqliteDatabase('brainless.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Task(BaseModel):
    task_id = peewee.AutoField(column_name='TaskID', primary_key=True)
    user_id = peewee.TextField(column_name='UserID')
    task_text = peewee.TextField(column_name='TaskText')
    done = peewee.BooleanField(column_name='Done', default=False)
    task_date = peewee.DateField(column_name='Date', default=d.datetime.date(d.datetime.today()))
    task_desc = peewee.TextField(column_name='TaskDesc', default='Тут должно быть описание📝')
    last_target_list = peewee.TextField(column_name='LastTargetList')

    class Meta:
        table_name = 'Tasks'


class User(BaseModel):
    user_id = peewee.IntegerField(column_name='UserID', primary_key=True)
    last_target_list = peewee.IntegerField(column_name='LastTargetListID', default=0)

    class Meta:
        table_name = 'Users'






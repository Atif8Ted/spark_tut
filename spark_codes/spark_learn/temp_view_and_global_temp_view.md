## TempView
> * Is accessible only from the sparksession it is created from.
> * Once the sparksession it is created closed , its lifetime will be over.
> * <b>syntax to access</b> : ```
select * from temp_view_name```

## Global TempView
> * Is accessible  from the sparksession it is created from as well as other sparksession.
> *  Once the sparksession it is created closed , its lifetime will be over.
> * <b>syntax to access </b>: `select * from global_temp.global_temp_view_name`




### Syntax to create new Session in spark

> ```python newSpark_session = spark.newSession```

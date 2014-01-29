#!/usr/bin/python
# coding: utf-8


import sys
sys.path.insert(0,"/s/apps/lin/vfx_test_apps/OpenRenderManagement/Puli/src")


from puliclient import Task, Graph

tags =  { "prod":"test", "shot":"test" }

runner='puliclient.contrib.commandlinerunner.CommandLineRunner'
arguments={ 'args':'echo TOTO' }

graph = Graph('debug', tags=tags, poolName='default' )

task1 = graph.addNewTask( "TASK_1", tags=tags, arguments=arguments, runner=runner )
# task2 = graph.addNewTask( "TASK_2", tags=tags, arguments=arguments, runner=runner )
# task1.dependsOn(task2)


graph.submit("pulitest", 8004)
graph.execute()

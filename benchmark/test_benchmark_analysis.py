import os
import process_data as pro
import pytest
from jinja2 import Template
import json 

# 定义一个fixture，用于收集每个benchmark的分数
@pytest.fixture
def single_benchmark_scores():
    benchmark = {}
    if os.path.exists('logs/7zip-output.log'):
        _7zip_score = pro.get_data('logs/7zip-output.log','Tot:',3)
        benchmark['7zip']={}
        benchmark['7zip']['scores']=_7zip_score
    else :
        print("7zip-output.log日志文件不存在")
    
    if os.path.exists('logs/blogbench-1.1-output.log'):
        blogbench_score =  pro.get_data('logs/blogbench-1.1-output.log','asdasd',0)#需要修改
        benchmark['blogbench']={}
        benchmark['blogbench']['scores']=blogbench_score
    else :
        print("blogbench-1.1-output.log日志文件不存在")

    if os.path.exists('logs/ebizzy-0.3-output.log'):
        ebizzy_score = pro.get_data('logs/ebizzy-0.3-output.log','records/s',0)
        benchmark['ebizzy']={}
        benchmark['ebizzy']['scores']=ebizzy_score
    else :
        print("ebizzy-0.3-output.log日志文件不存在")


    if os.path.exists('logs/ffte-7.0-output.log'):
        ffte_score = pro.get_data('logs/ffte-7.0-output.log','MFLOPS',0)
        benchmark['ffte']={}
        benchmark['ffte']['scores']=ffte_score
    else :
        print("ffte-7.0-output.log日志文件不存在")


    if os.path.exists('logs/Fhourstone-output.log'):
        Fhourstone_score = pro.get_data('logs/Fhourstone-output.log','Kpos/sec',6)
        benchmark['Fhourstone']={}
        benchmark['Fhourstone']['scores']=Fhourstone_score
    else :
        print("Fhourstone-output.log日志文件不存在")

    if os.path.exists('logs/hackbench-output.log'):
        hackbench_score = pro.get_data('logs/hackbench-output.log','Time: ',1)
        benchmark['hackbench']={}
        benchmark['hackbench']['scores']=hackbench_score
    else :
        print("hackbench-output.log日志文件不存在")

    
    if os.path.exists('logs/miniFE-2.2.0-output.log'):
        miniFE_score = pro.get_data('logs/miniFE-2.2.0-output.log','Final Resid Norm',3)
        benchmark['miniFE']={}
        benchmark['miniFE']['scores']=miniFE_score
    else :
        print("miniFE-2.2.0-output.log日志文件不存在")    


    if os.path.exists('logs/mpc-1.1.0-output.log'):
        mpc_score = pro.get_data('logs/mpc-1.1.0-output.log','global score ',2)
        benchmark['mpc']={}
        benchmark['mpc']['scores']=mpc_score
    else :
        print("mpc-1.1.0-output.log日志文件不存在")    

    if os.path.exists('logs/nbench-output.log'):
        nbench_score = pro.get_data('logs/nbench-output.log','INTEGER INDEX',3)
        benchmark['nbench']={}
        benchmark['nbench']['scores']=nbench_score
    else :
        print("nbench-output.log日志文件不存在")    

    if os.path.exists('logs/PENNANT-1.0.1-output.log'):
        PENNANT_score = pro.get_data('logs/PENNANT-1.0.1-output.log','hydro cycle run time=',4)
        benchmark['PENNANT']={}
        benchmark['PENNANT']['score']=PENNANT_score
    else :
        print("PENNANT-1.0.1-output.log日志文件不存在")    

    if os.path.exists('logs/RSBench-output.log'):
        RSBench_score = pro.get_data('logs/RSBench-output.log','Lookups/s:',1)
        benchmark['RSBench']={}
        benchmark['RSBench']['scores']=RSBench_score
    else :
        print("RSBench-output.log日志文件不存在")    

    if os.path.exists('logs/superPI-output.log'):
        superPI_score = pro.get_data('logs/superPI-output.log','sec. ',0)
        benchmark['superPI']={}
        benchmark['superPI']['scores']=superPI_score
    else :
        print("superPI-output.log日志文件不存在")      
    print(benchmark)

    # 依此类推...

    return benchmark

# 测试用例使用benchmark_scores fixture来获取每个benchmark的分数
def test_benchmarks(single_benchmark_scores):
    
    assert len(single_benchmark_scores) == 13  # 假设有3个benchmark
    print(single_benchmark_scores)
    # 其他断言或操作...

import glob
import os

configfile: "config.yaml"

logic_path = config['logic_path']
data_path = config['data_path']
name = config['targets']

logic = [os.path.basename(x) for x in glob.glob(f'{logic_path}/*')]

rule all:
    input: expand("{name}/{logic}/results.json", logic=logic, name=name)

rule cello:
    input: ucf=lambda wildcards: f"{data_path}/{wildcards.name}.UCF.json",
         input=lambda wildcards: f"{data_path}/{wildcards.name}.input.json",
         out=lambda wildcards: f"{data_path}/{wildcards.name}.output.json",
         logic=lambda wildcards: f"{logic_path}/{wildcards.logic}"
    output: "{name}/{logic}/results.json"
    log: "{name}/{logic}/log.txt"
    benchmark: "{name}/{logic}/benchmark.txt"
    params: app_path=config['app_path'],
            out_dir=lambda wildcards: f'{wildcards.name}/{wildcards.logic}'
    shell:
         """
         java -classpath {params.app_path} org.cellocad.v2.DNACompiler.runtime.Main \
         -inputNetlist {input.logic} \
         -userConstraintsFile {input.ucf} \
         -inputSensorFile {input.input} \
         -outputDeviceFile {input.out} \
         -pythonEnv python \
         -outputDir {params.out_dir} 2> {log}
         """

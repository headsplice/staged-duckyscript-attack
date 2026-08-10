import subprocess 

subprocess.run(["pip","install","pyjokes","-q","--disable-pip-version-check","--root-user-action=ignore"])
# long arguments are for suppressing pip notices and errors
import pyjokes
print(pyjokes.get_joke())
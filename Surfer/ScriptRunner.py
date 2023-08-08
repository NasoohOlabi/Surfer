
class ScriptRunner:
  from selenium import webdriver
  def __init__(self,driver:webdriver.Chrome,defaultFolder:str):
    self.driver = driver
    self.defaultFolder = defaultFolder
    
  def __call__(self,name:str,verbose=False,folder:str|None=None):
    _folder = self.defaultFolder if folder is None else folder
    from typing import Any
    def script(*args:Any):
      script_string = ScriptRunner.get_script(_folder,name)(*args)
      try:
        answer = self.driver.execute_script(script_string)
      except Exception as e:
        print('the following script crashed!')
        print(script_string)
        raise e
      if verbose:
        print('script_string: ',script_string,' Answer: ', answer)
      return answer
    return script
  
  @staticmethod
  def get_script(folder:str,filename:str):
    import json
    script = ''
    with open(f'./{folder}{filename}.js','r') as f:
      script = f.read()
    script = script.replace('\n','')
    def replacer(*args):
      acc = script
      for i,x in enumerate(args):
        acc = acc.replace('$'+str(i),str(x))
      return 'try{' + f'console.log(`{filename}`,JSON.parse(`{json.dumps(args)}`));'+acc+'}catch(err){console.error(`{filename}`,err);}'
    return replacer
    
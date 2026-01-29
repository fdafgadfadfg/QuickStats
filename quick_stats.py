
import sys
import sys
import os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))
from scipy import stats
from flowlauncher import FlowLauncher 
class QuickStats(FlowLauncher):
    def query(self, query):
       
       return [
            {
                "Title": "Mean and stdev, comma separated.",
                "SubTitle": "Get normal pdf",
                "ContextData": ["foo", "bar"],
                "JsonRPCAction": {
                    "method": "norm",
                    "parameters": [f"{query}"]
                }
            }
        ]

    def norm(self, query):
       get_vals = query.split(',')
       stats.norm.pdf(get_vals[0], get_vals[1])
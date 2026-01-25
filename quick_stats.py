
import sys
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path
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
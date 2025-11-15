from loader import Loader
from workshop import Workshop

loader = Loader()
job = loader.load("table.yaml")

ws = Workshop()
ws.load_job(job)

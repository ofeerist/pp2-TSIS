def log(n: str):
  return lambda a : print(n + a)

warning = log("Warning: ")
exception = log("Exception: ")

warning("Detected memore leak while executing job system")
exception("Invalid data type")
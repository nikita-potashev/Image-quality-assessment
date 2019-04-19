from gui.main import app
from utils.config import process_config
from utils.utils import get_args

if __name__ == "__main__":
    # try:
    #     args = get_args()
    #     config = process_config(args.config)
    # except:
    #     print("missing or invalid arguments")
    #     exit(0)
        
    app()
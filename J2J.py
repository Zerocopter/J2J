import sys
import io
import json
import javaobj
from javaobj import JavaObjectUnmarshaller

def seek_size(f):
    pos = f.tell()
    f.seek(0, io.SEEK_END)
    size = f.tell()
    f.seek(pos)
    return size


def main():
    with open(sys.argv[1], "rb") as fin:
        i = 0
        t = None
        
        fileSize = seek_size(fin)
        tmpObject = None
        
        marshaller = JavaObjectUnmarshaller(fin)
        
        try:
            tmpObject = marshaller.readObject(ignore_remaining_data=False)
            objectType = tmpObject.__str__();
            
            if objectType == "<javaobj:java.util.Properties>":
                properties = {}
                while fin.tell() != fileSize:
                    key = marshaller.readObject(ignore_remaining_data=True)
                    value = marshaller.readObject(ignore_remaining_data=True)
                    properties[key] = value
                
                if len(sys.argv) > 2:
                    with open(sys.argv[2], 'w') as f:
                        json.dump(properties, f)
                else:
                    print(json.dumps(properties, indent=4))
            else:
                items = []
                for obj in marshaller.references:
                    str = obj.__str__()
                    if str.startswith("[") and str.endswith("]"):
                        continue;
                    items.append(str)
                if len(sys.argv) > 2:
                    with open(sys.argv[2], 'w') as f:
                        json.dump(items, f)
                else:
                    print(json.dumps(items, indent=4))
               
        except Exception:
            raise

        
            

        if fin.tell() != fileSize:
            print("error!")

if __name__ == "__main__":
    sys.exit(main())
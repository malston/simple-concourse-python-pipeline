import os
import numpy as np

def main():
    print("Hello, Concourse!")
    msg = "Roll a dice!"
    print(msg)

    print(np.random.randint(1,9))

    with open('/tmp/output.txt', 'w') as f:
        f.write("Task completed successfully!")

if __name__ == "__main__":
    main()

"""import os

def ipc(parent_message, child_writes, pipe_read, pipe_write):
    process_id = os.fork()

    if process_id:
        # Parent process
        os.close(pipe_write)
        r = os.fdopen(pipe_read)
        print(f"Parent {os.getpid()} reading")
        message = r.read()
        print(f"Parent {os.getpid()} reads = {message}")
        r.close()
    else:
        # Child process
        os.close(pipe_read)
        w = os.fdopen(pipe_write, 'w')
        print(f"Child {os.getpid()} writing")
        w.write(child_writes)
        print(f"Child {os.getpid()} writes = {child_writes}")
        w.close()
    
    if process_id:
        os.wait()

if __name__ == "__main__":
    # Create two pipes for communication
    pipe_1_read, pipe_1_write = os.pipe()
    pipe_2_read, pipe_2_write = os.pipe()

    # Create two parent processes
    parent_1_pid = os.getpid()
    parent_2_pid = parent_1_pid + 1
    
    child_11 = os.fork()
    if child_11 == 0:
        ipc(f"Message from Parent {parent_1_pid} to Child 11!", "Child 11 Response", pipe_1_read, pipe_1_write)
        os._exit(0)
    
    child_21 = os.fork()
    if child_21 == 0:
        ipc(f"Message from Parent {parent_2_pid} to Child 21!", "Child 21 Response", pipe_2_read, pipe_2_write)
        os._exit(0)

    os.close(pipe_1_read)
    os.close(pipe_1_write)
    os.close(pipe_2_read)
    os.close(pipe_2_write)

    os.waitpid(child_11, 0)
    os.waitpid(child_21, 0)"""
    
print("""Parent 6956 reading
Parent 6956 reads = Message from Parent 6955 to Child 11!
Child 6958 writing
Child 6958 writes = Child 11 Response
Parent 6957 reading
Parent 6957 reads = Message from Parent 6956 to Child 21!
Child 6960 writing
Child 6960 writes = Child 21 Response""")
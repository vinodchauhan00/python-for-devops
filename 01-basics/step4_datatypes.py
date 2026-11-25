# Python Data Types and f-strings

# 1) Variables: each one has a different data type
server_name = "46server"       # str   -> text (inside quotes)
ip_address = "192.168.1.10"    # str   -> an IP address is always written in quotes
port = 109                     # int   -> whole number
cpu_usage = 72.567             # float -> number with a decimal point
is_running = True              # bool  -> only True or False (capital T and F)

# 2) type(): tells us which data type a variable has
print(type(server_name))       # <class 'str'>
print(type(port))              # <class 'int'>
print(type(cpu_usage))         # <class 'float'>
print(type(is_running))        # <class 'bool'>

# 3) f-string: put f before the quotes and the variable inside { }
print(f"Server {server_name} is running on port {port}")

# 4) :.1f -> show only 1 digit after the decimal point (72.567 -> 72.6)
print(f"CPU usage: {cpu_usage:.1f}%")

# 5) Calculations also work inside { } (the real value of port does not change)
print(f"Next port: {port + 1}")

# 6) "5" in quotes is text, 5 without quotes is a number
print("5" + "3")               # text gets joined  -> 53
print(5 + 3)                   # maths is done     -> 8
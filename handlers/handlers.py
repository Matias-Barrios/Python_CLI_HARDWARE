
import cpu.cpu_load as cpu_load
import memory.memory as mem

HS = { 'load' : cpu_load.get_cpu_load,
       'stats' : mem.get_memory_stats,
       }

def get_handler(name) :
    return HS[name]

import subprocess

def add_rvm_env_segment():
    try:
        env = subprocess.check_output("rvm-prompt").decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return False
    except OSError:
        # we were unable to find rvm-prompt on the commandline
        # so let's ignore this segment:
        return False
    except:
        return False
    bg = 35
    fg = 0
    powerline.append(' %s ' % env, fg, bg)

add_rvm_env_segment()

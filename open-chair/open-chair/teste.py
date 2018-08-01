import subprocess
import sys

create = [sys.executable, '/opt/mycroft/skills/heart-rate.tiagochiavericosta/finger_heart_rate_monitor.py']

subprocess.call(create)

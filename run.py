import subprocess
import os
import time
import numpy as np
import matplotlib.pyplot as plt

def run_c_o3():
    print "running c (O3)"
    subprocess.call(['gcc', '-O3', "c.c", "-o", "c"])
    exe = os.getcwd() + '/c'
    start = time.time()
    p = subprocess.Popen(exe, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    os.remove(exe)
    return int(t * 1000), int(output[1])

def run_c():
    print "running c"
    subprocess.call(['gcc', "c.c", "-o", "c"])
    exe = os.getcwd() + '/c'
    start = time.time()
    p = subprocess.Popen(exe, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    os.remove(exe)
    return int(t * 1000), int(output[1])


def run_clojue():
    print "running clj"
    start = time.time()
    clj = 'java -cp ../rssminer/lib/clojure-1.4.0.jar clojure.main clj.clj'
    p = subprocess.Popen(clj, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    return int(t * 1000), int(output[1])

def run_go():
    print "runing go"
    subprocess.call(['go', "build", "go.go"])
    exe = os.getcwd() + '/go'
    start = time.time()
    p = subprocess.Popen(exe, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    os.remove(exe)
    return int(t * 1000), int(output[1])

def run_py():
    print "running python"
    start = time.time()
    exe = "python py.py"
    p = subprocess.Popen(exe, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    return int(t * 1000), int(output[1])

def run_js():
    print "running nodejs"
    start = time.time()
    exe = "node node.js"
    p = subprocess.Popen(exe, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    return int(t * 1000), int(output[1])

def run_java():
    print "running java"
    subprocess.call(['javac', "Test.java"])
    start = time.time()
    p = subprocess.Popen("java Test", stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    output = p.stdout.read().split('\n')
    t = time.time() - start
    exe = os.getcwd() + '/Test.class'
    os.remove(exe)
    return int(t * 1000), int(output[1])

def autolabel(ax, rects, delta):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        x = rect.get_x()+rect.get_width()/2.
        ax.text(x + delta, height + 200, '%d'%int(height),
                ha='center', va='bottom', fontsize=8)

if __name__ == '__main__':
    c03 = run_c_o3()
    c = run_c()
    clj = run_clojue()
    go = run_go()
    py = run_py()
    js = run_js()
    java = run_java()

    total, runtime = zip(*[c03, c, clj, go, py, js, java])
    names = ["C(O3)", "C", "Clojure", "go", "python", "node", "JAVA"]
    ind = np.arange(len(names))  # the x locations for the groups
    width = 0.35              # the width of the bars

    fig = plt.figure(figsize=(7,6))
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, total, width, color='r')
    rects2 = ax.bar(ind+width, runtime, width, color='y')

    # add some
    ax.set_ybound(upper=37000)
    ax.set_ylabel('millisecond')
    ax.set_title('fibonacci(40) benchmark game')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( names )

    ax.legend((rects1[0], rects2[0]), ('Total (including startup)', 'Fibonacci time'))

    delta = rects1[1].get_x() * 0.05
    autolabel(ax, rects1, -delta)
    autolabel(ax, rects2, delta)
    fig.savefig('pic.png')

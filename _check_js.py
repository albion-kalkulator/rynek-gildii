import re, subprocess, tempfile, os
p = r"C:\Users\konra\jakiś syf\1\rynek-gildii\index.html"
js = re.search(r"<script>(.*)</script>", open(p, encoding="utf-8").read(), re.S).group(1)
lines = js.splitlines()
lo, hi = 2380, 2627
while lo < hi:
    mid = (lo + hi) // 2
    chunk = "\n".join(lines[:mid]) + "\n"
    fd, path = tempfile.mkstemp(suffix=".js")
    os.write(fd, chunk.encode("utf-8"))
    os.close(fd)
    r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
    os.unlink(path)
    if r.returncode == 0:
        lo = mid + 1
    else:
        hi = mid
print("first fail line", lo)
print("content:", lines[lo-1][:120] if lo <= len(lines) else "EOF")

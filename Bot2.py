from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("arg1", type=int, nargs="?", default=60)
parser.add_argument("arg2", type=int, nargs="?", default=60)
parser.add_argument("crns", nargs="*")
args = parser.parse_args()
crn = "'" + "','".join(args.crns) + "'"

url = "https://obs.itu.edu.tr/"



s = "var e = [" + crn + "]"
script = """
let t = document.querySelectorAll("input[type='number']"),
n = 0;
t.forEach(t => {
    (function e(t) {
        let n = window.getComputedStyle(t);
        if ("none" === n.display || "hidden" === n.visibility) return !1;
        let l = t.parentElement;
        for (; l;) {
            let i = window.getComputedStyle(l);
            if ("none" === i.display || "hidden" === i.visibility) return !1;
            l = l.parentElement
        }
        return !0
    })(t) && n < e.length && (t.value = e[n], t.dispatchEvent(new Event("input", {
        bubbles: !0
    })), n++)
}), setTimeout(function() {
    let e = document.querySelector('button[type="submit"]:not([disabled])');
    e && e.click(), setTimeout(function() {
        let e = document.querySelector(".card-footer.d-flex.justify-content-end");
        if (e) {
            let t = e.getElementsByTagName("button");
            t.length > 1 && t[1].click()
        }
    }, 50)
}, 50);
"""
script = s + script

driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(args.arg1)
    while True:
        driver.execute_script(script)

        time.sleep(args.arg2)

except KeyboardInterrupt:
    print("Exit")
finally:
    driver.quit()

import os
import sys
import subprocess
import requests
from bs4 import BeautifulSoup

class HackerFramework:
    def __init__(self):
        self.tools = {
            "port_scanner": "nmap",
            "password_cracker": "hydra",
            "packet_sniffer": "wireshark",
            "vulnerability_scanner": "nmap",
            "web_crawler": "crawl",
            "web_scanner": "nikto",
            "web_server_scanner": "w3af",
            "exploit_finder": "searchsploit",
            "social_engineering_tool": "setoolkit",
            "password_manager": "keepassxc",
            "malware_analysis_tool": "volatility",
            "steganography_tool": "steghide",
            "ddos_tool": "slowhttptest",
            "spiderfoot": "spiderfoot",
            "metasploit": "msfconsole",
            "burp_suite": "burpsuite"
        }

    def install_tool(self, tool_name):
        if tool_name not in self.tools:
            print(f"{tool_name} is not a valid tool.")
            return
        tool_path = self.tools[tool_name]
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", tool_path])
            print(f"{tool_name} has been installed.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {tool_name}.")

    def scan_ports(self, target):
        subprocess.call(["nmap", target])

    def crack_passwords(self, target, username, wordlist):
        subprocess.call(["hydra", "-l", username, "-P", wordlist, target, "ssh"])

    def sniff_packets(self, interface):
        subprocess.call(["wireshark", "-i", interface])

    def scan_vulnerabilities(self, target):
        subprocess.call(["nmap", "--script", "vuln", target])

    def crawl_website(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")
        for link in links:
            print(link.get("href"))

    def scan_webserver(self, url):
        subprocess.call(["w3af", "-s", url])

    def search_exploits(self, exploit):
        subprocess.call(["searchsploit", exploit])

    def social_engineering(self, target, message):
        subprocess.call(["setoolkit", "-i", target, "-m", message])

    def manage_passwords(self, password_file):
        subprocess.call(["keepassxc", "--pw-file", password_file])

    def analyze_malware(self, malware_file):
        subprocess.call(["volatility", "-f", malware_file, "--profile=Win7SP1x64", "pslist"])

    def hide_data(self, input_file, output_file):
        subprocess.call(["steghide", "embed", "-cf", input_file, "-ef", output_file])

    def perform_ddos(self, target):
        subprocess.call(["slowhttptest", "-c", "1000", "-H", "-i", "10", "-r", "100", "-t", "GET", "-u", target])

    def spiderfoot_scan(self, target):
        subprocess.call(["spiderfoot", "-s", target])

    def exploit_metasploit(self, exploit, target):
        subprocess.call(["msfconsole", "-x", f"use {exploit}; set RHOST {target}; exploit"])

    def use_burp_suite(self, target):
        subprocess.call(["burpsuite", "-u", target])

    def run_tool(self, tool_name, *args):
        if tool_name not in self.tools:
            print(f"{tool_name} is not a valid tool.")
            return
        tool_method = getattr(self, tool_name.replace(" ", "_"))
        tool_method(*args)

    def list_tools(self):
        print("Available tools:")
        for tool in self.tools.keys():
            print(f"- {tool}")

def main():
    hacker_framework = HackerFramework()
    hacker_framework.list_tools()
    while True:
        user_input = input("Enter a command (or 'help' for help): ")
        if user_input == "help":
            print("Available commands:")
            print("- install <tool_name>")
            print("- scan_ports <target>")
            print("- crack_passwords <target> <username> <wordlist>")
            print("- sniff_packets <interface>")
            print("- scan_vulnerabilities <target>")
            print("- crawl_website <url>")
            print("- scan_webserver <url>")
            print("- search_exploits <exploit>")
            print("- social_engineering <target> <message>")
            print("- manage_passwords <password_file>")
            print("- analyze_malware <malware_file>")
            print("- hide_data <input_file> <output_file>")
            print("- perform_ddos <target>")
            print("- spiderfoot_scan <target>")
            print("- exploit_metasploit <exploit> <target>")
            print("- use_burp_suite <target>")
            print("- exit")
        elif user_input == "exit":
            break
        else:
            try:
                command, *args = user_input.split()
                hacker_framework.run_tool(command, *args)
            except TypeError:
                print("Invalid command. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    main()
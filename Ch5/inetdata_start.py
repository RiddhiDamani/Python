# 
# Example file for retrieving data from the internet
#

# this module provides the classes and code that will be needed to make the http request. 
import urllib.request


def main():
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(webUrl.getcode()))
  data = webUrl.read()
  print(data)


if __name__ == "__main__":
  main()

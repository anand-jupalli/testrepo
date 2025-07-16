def outer(text):
            t=text
            def inner():
                        print(t)
            print("hiii")
            inner()
if __name__=="__main__":
            outer('hello')

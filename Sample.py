def function1():
    print("Hello 1");
    def function2():
        print("hello 2");
        return function2();
    return function1();


A=function1;
function1()()();

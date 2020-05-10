# decorator is a simple function that takes other function as input
def call_logger(sample_function):
    # Here the scope od inner_function is inside the decorator only
    def inner_function():
        # importing the datetime module
        from datetime import datetime
        # open a file to set the logs
        file = open("../log.txt", 'a')
        file.write('called the function on ' + str(datetime.now()) + '\n')
        file.close()
        # now call the function passed, here first inner_function will execute only after
        # that the other function is called
        return sample_function()
    return inner_function


@call_logger # assigning the decorator
def test_function():
    print("I am a normal function")


# calling the functions, first decorators will run then the logic inside the function will run!!
test_function()
test_function()
test_function()
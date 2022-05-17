class university:
    def __init__(self):
        self.student = ['Graduate','post graduate','scholar']

    def courses(self):
        print("available courses in uni")
        for study in self.student:
            print("\t%s" % study)


class college:
    def __init__(self):
        self.student = ['MPC','BPC','MEC']

    def courses(self):
        print("available courses in college")
        for study in self.student:
            print("\t%s" % study)


class school:
    def __init__(self):
        self.student = ['SSC','CBSE','ICSE']

    def courses(self):
        print("available courses in School")
        for study in self.student:
            print("\t%s" % study)
import os 
import glob
import yaml
import shutil

# main class
class PackTool():
    def __init__(self):
        print("pack-tool by enorsu(idk why i put my name here)")
        self.loadConfiguration("./configuration.yaml")

    def imagemagick(self, infile, outfile, arguments, binary):
        # run command
        os.system(f"{binary} {infile} {arguments} {outfile}")
    def sox(self, infile, outfile, arguments, binary):
        # fuck it we ball
        tmp = "./temp"
        if not os.path.isdir(tmp):
            os.mkdir(tmp)

        # command
        # remove the first dot
        thing = list(outfile)
        if thing[0] == ".":
            thing[0] = ""
        
            # make it do the thing into temp file
        outpfile = tmp + "".join(thing)
        if not os.path.exists(outpfile):
            os.makedirs(os.path.dirname(outpfile), exist_ok=True)
        os.system(f"{binary} {arguments} {infile} {outpfile}")

        # move from temp to original location
        # and before that delete the original one
        os.remove(outfile)
        shutil.move(outpfile, outfile)

    def search(self, dir, filetype):
        # glob
        # remove duplicates with list(set(x))
        # yeah
        return list(set(glob.glob(pathname=f"{dir}/**/**/**/**/**/**.{filetype}", recursive=True)))

    def loadConfiguration(self, filename):
        with open(filename, "r") as file:
            self.configuration = yaml.safe_load(file.read())
        print("config loaded", filename)
    
    def autoimg(self):
        # if its not enabled then dont do it 
        if not self.configuration["actions"]["imagemagick"]["enabled"]:
            return print("no imagemagick, doing nothing")
        
        binary = self.configuration["actions"]["imagemagick"]["binary"]
        arguments = self.configuration["actions"]["imagemagick"]["arguments"]

        directory = self.configuration["folder"]

        files = self.search(directory, "png")
        
        total = len(files)

        for i in range(total):
            file = files[i]
            self.imagemagick(infile=file, outfile=file, binary=binary, arguments=arguments)
            print(f"[{i + 1}/{total}]{file}")
    def autosox(self):
        # if its not enabled then dont do it 
        if not self.configuration["actions"]["sox"]["enabled"]:
            return print("no sox, doing nothing")
        
        binary = self.configuration["actions"]["sox"]["binary"]
        arguments = self.configuration["actions"]["sox"]["arguments"]

        directory = self.configuration["folder"]

        files = self.search(directory, "ogg")
        
        total = len(files)

        for i in range(total):
            file = files[i]
            self.sox(infile=file, outfile=file, binary=binary, arguments=arguments)
            print(f"[{i + 1}/{total}]{file}")
    def automatic(self):
        # yuh
        self.autoimg()
        self.autosox()

packtool = PackTool()


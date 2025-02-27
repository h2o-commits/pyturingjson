import json
import sys;

def init(filename):
    global position;
    global tape;
    global rules;
    global state;

    with open(filename) as data_file:    
        jsonObject = json.load(data_file);

    position = jsonObject["position"];
    tape = jsonObject["tape"];
    rules = jsonObject["rules"];
    state = jsonObject["rules"][0][0];


def show():
    for i in range(position):
        print(' ', end='');
    print('P');
    print(tape);
    print("State: "+ str(state));
    print("Position: "+ str(position));
    print("");

def getch():
    global position;
    global tape;
    print(str(position));
    print(str(tape));
    if (position>=len(tape)):
        return "#"
    elif (position<0):
        return "#"; 
    else:
        if tape[position]==" ":
            return "#"; 
        return tape[position];

def next():
    global state;
    global position;
    global tape;
    for key in rules:
        oldstate=key[0];
        ch=key[1];
        replace=key[2];
        newstate=key[3];
        direction=key[4];
        if (state == oldstate):
            if getch() == ch or ch=="*": 
                print ("Match: "+str(key));
                if replace!="*":
                    tape = tape[:position]+replace+tape[position+1:];
                state=newstate;
                if direction =="R":
                    position +=1;
                    if position>=len(tape):
                        tape=tape+"#";
                elif direction =="L":
                    if position==0:
                        tape="#"+tape;
                    else:
                        position -=1;
                break;

def main():
    if len(sys.argv)<2:
        print("Usage: python3 pyturingjson.py filename.json")
        exit(1);
    init(sys.argv[1]);
    i=0;
    while(state!='h'):
        print("Step "+str(i)+ ":");
        show();
        next();
        print("---------------------------------------------");
        i+=1;
        if i==200:
            break;

if __name__ == '__main__':
    main()

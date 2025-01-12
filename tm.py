import json

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
    print("State:"+ str(state));
    print("Position:"+ str(position));
    print("");

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
            if tape[position] == ch:
                print ("Match: "+str(key));
                tape = tape[:position]+replace+tape[position+1:];
                state=newstate;
                if direction =="R":
                    position +=1;
                else:
                    position -=1;
                break;

def main():
    init("increment.json");
    i=0;
    while(state!='h'):
        show();
        next();
        print("---------------------------------------------");
        i+=1;
        if i==100:
            break;

if __name__ == '__main__':
    main()

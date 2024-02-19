from tkinter.colorchooser import Chooser
from pystyle import Colorate, Center, Write, Anime, Colors, System, Col
import os, time 
import random


barre = """\n\n╔═════[X WHIZEN X@whizen\n\n"""

barre2 = """╔═════[ID]"""

barre3 = """@password]"""

barre4 = """╔═════["""

Barre5 = (Colorate.Vertical(Colors.red_to_black, "L I V E: "))

barre6 = (Colorate.Vertical(Colors.white_to_black, "X WHIZEN X "))

barre7 = (Colorate.Vertical(Colors.green_to_cyan, " | "))

barre8 = (Colorate.Vertical(Colors.blue_to_cyan, " Discord :"))

barre9= (Colorate.Vertical(Colors.white_to_black, " Debitage_online"))

barre10 = (Colorate.Vertical(Colors.cyan_to_green, " <Fresh update done!>"))

ascii = """

                     ─┐ ┬  ┬ ┬  ┬ ┬  ┬  ┌─┐  ┌─┐  ┌┐┌  ─┐ ┬
                     ┌┴┬┘  │││  ├─┤  │  ┌─┘  ├┤   │││  ┌┴┬┘
                     ┴ └─  └┴┘  ┴ ┴  ┴  └─┘  └─┘  ┘└┘  ┴ └─
                     X WHIZEN X can't shine without darkness  
                   ══════╦══════════════════════════════╦═════   
                      ╔══╩══════════════════════════════╩══╗
                      ║------Welcome to X WHIZEN X Net-----║
                      ║------Snapchat debitage_online------║  
                      ╚══╦══════════════════════════════╦══╝
             ╔═══════════╩══════════════════════════════╩═════════╗
             ║  -Copyright @ 2022 X WHIZEN X All Rights Reserved- ║
             ║ - - -Please Type [HELP] To view All  Commands- - - ║
             ╚════════════════════════════════════════════════════╝"""

ascii2= """
                     ─┐ ┬  ┬ ┬  ┬ ┬  ┬  ┌─┐  ┌─┐  ┌┐┌  ─┐ ┬
                     ┌┴┬┘  │││  ├─┤  │  ┌─┘  ├┤   │││  ┌┴┬┘
                     ┴ └─  └┴┘  ┴ ┴  ┴  └─┘  └─┘  ┘└┘  ┴ └─
                      ╚════╦════════════════════════╦════╝    
                  ╔════════╩════════════════════════╩════════╗
                  ║  METHODS > LISTS OUR METHODS             ║  
                  ║  CHAT > ENTERSTHE PLUBLIC CHAT ROOM      ║
                  ║  ATTACK > ATTACK THE IPV4/IPV7           ║
                  ║  RULES > LISTS OUR TOS / RULES           ║
                  ║  PLAN > LISTS YOUR INFO                  ║
                  ║  TOOLS > LIST THE TOOLS                  ║
                  ║  CLEAR > CLEAR YOUR TERMINAL             ║
                  ║  CLS > CLOSE THE SESSION                 ║
                  ╚══════════════════════════════════════════╝"""

ascii3 = """
                             ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
                             ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
                             ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
                     ╔══════════════════════════════════╗                            
             ╔═══════╩═══╗╔═══════════╗╔═══════════╗╔═══╩═══════╗
             ║ RAIL      ║║ OVH-NUKE  ║║ OVH-ANGEL ║║ FIVEM     ║
             ║ LDAP      ╠╣ OVH-VITAL ╠╣ OVH-FAITH ╠╣ SSH       ║
             ║ HOLD      ║║ OVH-YUIV2 ║║ OVH-RAPE  ║║ ROBLOX    ║
             ╚═════╦═════╝╚═════╦═════╝╚═════╦═════╝╚═════╦═════╝
             ╔═════╩═════╗╔═════╩═════╗╔═════╩═════╗╔═════╩═════╗
             ║ 100UP     ║║ NFO-STUN  ║║ SYN-AMPE  ║║ LAYER7    ║
             ║ CHAOS     ╠╣ NFO-FRAG  ╠╣ AMPBYPASS ╠╣ UDP-XV    ║
             ║ HYDRA     ║║ NFO-PORT  ║║ MULTISSYN ║║ DNS-C2    ║
             ╚═════╦═════╝╚═════╦═════╝╚═════╦═════╝╚═════╦═════╝
             ╔═════╩═════╗╔═════╩═════╗╔═════╩═════╗╔═════╩═════╗
             ║ GAME-SLAP ║║ 100UP-CPU ║║ HTTPS-SEC ║║ OVH-UDP   ║
             ║ XFORTNITE ╠╣ NTP-SMOKE ╠╣ HTTPS-RAW ╠╣ NTP-XV    ║
             ║ TRUMP-SEC ║║ HOME-CLAP ║║ HTTPS-QUE ║║ VSE-C2    ║
             ╚═══════════╝╚═══════════╝╚═══════════╝╚═══════════╝
"""

ascii4 = """
─┐ ┬  ┬ ┬  ┬ ┬  ┬  ┌─┐  ┌─┐  ┌┐┌  ─┐ ┬
┌┴┬┘  │││  ├─┤  │  ┌─┘  ├┤   │││  ┌┴┬┘
┴ └─  └┴┘  ┴ ┴  ┴  └─┘  └─┘  ┘└┘  ┴ └─

Username : [whizen]
Admin : [True]
Resellert : [True}
VIP : [True]
Banned : [False]

Days Left : [illimited] 
Cooldown : [1]
Concurrents : [4]
Max sessions : [1]

Current Running Attacks globally : [1]
Attacks Sent By Exit : [89]"""

ascii5 = """
─┐ ┬  ┬ ┬  ┬ ┬  ┬  ┌─┐  ┌─┐  ┌┐┌  ─┐ ┬
┌┴┬┘  │││  ├─┤  │  ┌─┘  ├┤   │││  ┌┴┬┘
┴ └─  └┴┘  ┴ ┴  ┴  └─┘  └─┘  ┘└┘  ┴ └─

[PLEASE READ THE FOLLOWING RULES]
1) ~ Not following them will result in a ban on blacklist !
2) ~ D'ont share your spot !
3) ~ Do not spam the net !
4) ~ Don't hit now gouvernement websites !"""

IP = '1.1.1.1'

ascii6 = """
                      ─┐ ┬  ┬ ┬  ┬ ┬  ┬  ┌─┐  ┌─┐  ┌┐┌  ─┐ ┬
                      ┌┴┬┘  │││  ├─┤  │  ┌─┘  ├┤   │││  ┌┴┬┘
                      ┴ └─  └┴┘  ┴ ┴  ┴  └─┘  └─┘  ┘└┘  ┴ └─
                ╔════════════════════════════════════════════════╗
                ║[TARGET] > https://www.gaypride.fr
                ║[PORT] > 80
                ║[TIME] > 300
                ║[METHODS] > HTTPS-SEC
                ║[PPS] > -1 (UNLINITED)
                ║[TOTAL ATTACK] > 31
                ╚═════════╦════════════════════════════╦═════════╝
                ╔═════════╩════════════════════════════╩═════════╗
                ║[USER] > whizen
                ║[VIP] > True
                ╚════════════════════════════════════════════════╝"""

def barreH():
        System.Clear()
        print(Barre5 + barre6 + barre7 + barre8 + barre9 + barre7 + barre10)
        

def interface():
    System.Clear()
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mwhizen \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238 Discord:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mBvn\x1b[38;2;179;96;197mhFa\x1b[38;2;172;103;198mACT\x1b[38;2;165;110;199ms \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii)))

def interface1():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mwhizen \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238m Discord:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mBvn\x1b[38;2;179;96;197mhFa\x1b[38;2;172;103;198mACT\x1b[38;2;165;110;199ms \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii2)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'methods':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface2()
    if cmd == 'clear':
            main()
    if cmd == 'cls':
           exit()
    if cmd == 'plan':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface3()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

def interface2():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mwhizen \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238m Discord:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mBvn\x1b[38;2;179;96;197mhFa\x1b[38;2;172;103;198mACT\x1b[38;2;165;110;199ms \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii3)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'methods':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface2()
    if cmd == 'clear':
            main()
    if cmd == 'cls':
           exit()
    if cmd == 'plan':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface3()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

def interface3():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mwhizen \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238m Discord:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mBvn\x1b[38;2;179;96;197mhFa\x1b[38;2;172;103;198mACT\x1b[38;2;165;110;199ms \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii4)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'methods':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface2()
    if cmd == 'clear':
            main()
    if cmd == 'cls':
           exit()
    if cmd == 'plan':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface3()  
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

def interface4():
    System.Clear
    print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mwhizen \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238m Discord:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mBvn\x1b[38;2;179;96;197mhFa\x1b[38;2;172;103;198mACT\x1b[38;2;165;110;199ms \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
    print(Colorate.Vertical(Colors.cyan_to_blue, (ascii5)))
    print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
    cmd = Write.Input("╚══>", Colors.purple_to_blue)
    if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
    if cmd == 'methods':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface2()
    if cmd == 'clear':
            main()
    if cmd == 'cls':
           exit()
    if cmd == 'plan':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface3()
    if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
    else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

def interface5():
        System.Clear()
        print('\x1b[38;2;0;255;253m| \x1b[38;2;255;0;55mL I V E: \x1b[38;2;46;42;42mwhizen \x1b[38;2;0;255;253m| \x1b[38;2;146;109;238m Discord:\x1b[38;2;235;40;189m htt\x1b[38;2;228;47;190mps:\x1b[38;2;221;54;191m//\x1b[38;2;214;61;192mdis\x1b[38;2;207;68;193mcor\x1b[38;2;200;75;194md.gg\x1b[38;2;193;82;195m/\x1b[38;2;186;89;196mBvn\x1b[38;2;179;96;197mhFa\x1b[38;2;172;103;198mACT\x1b[38;2;165;110;199ms \x1b[38;2;0;255;253m| \x1b[38;2;235;40;189m[\x1b[38;2;3;252;136mENJOY!\x1b[38;2;235;40;189m]')
        print(Colorate.Vertical(Colors.cyan_to_blue, (ascii6)))
        print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
        cmd = Write.Input("╚══>", Colors.purple_to_blue, interval=0.005)
        if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
        if cmd == 'methods':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface2()
        if cmd == 'clear':
            main()
        if cmd == 'cls':
           exit()
        if cmd == 'plan':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface3()
        if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()



      


def whizen():
    System.Title("whizen - Total Clients[1] - Online[1] - Expiring[8567.21]days")
    System.Size(83, 24)
    Log = Write.Input("Login as : ", Colors.white_to_blue, interval=0.005)
    if Log == 'whizen':    
        Log2 = Write.Input(Log+"@password : ", Colors.white_to_blue, interval=0.005)
        if Log2 == 'whizen':
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m...\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m..\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    print('\x1b[38;2;235;40;189mL\x1b[38;2;228;47;190mo\x1b[38;2;221;54;191ma\x1b[38;2;214;61;192md\x1b[38;2;207;68;193mi\x1b[38;2;200;75;194mn\x1b[38;2;193;82;195mg \x1b[38;2;186;89;196mC\x1b[38;2;179;96;197my\x1b[38;2;172;103;198ms\x1b[38;2;165;110;199mt\x1b[38;2;158;117;200ma\x1b[38;2;151;124;201ml\x1b[38;2;172;103;198m \x1b[38;2;130;145;204mS\x1b[38;2;123;152;205me\x1b[38;2;116;159;206mr\x1b[38;2;109;166;207mv\x1b[38;2;102;173;208me\x1b[38;2;95;180;209mr\x1b[38;2;88;187;210ms: \x1b[38;2;41;58;186m[\x1b[38;2;3;252;136m.\x1b[38;2;41;58;186m] ')
                    time.sleep(0.1)
                    os.system('cls')
                    main()
        else:
                print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
                time.sleep(2)
                whizen()

def main():
        System.Title("whizen - Total Clients[1] - Online[1] - Expiring[8567.21]days - identity: [whizen]")
        System.Size(83, 24)
        barreH()
        interface()
        print (Colorate.Horizontal(Colors.purple_to_blue, (barre)))
        cmd = Write.Input("╚══>", Colors.purple_to_blue, interval=0.005)
        if cmd == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface1()
        if cmd == 'methods':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface2()
        if cmd == 'clear':
            main()
        if cmd == 'cls':
           exit()
        if cmd == 'plan':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface3()
        if cmd == 'rules':
            os.system('cls' if os.name == 'nt' else 'clear')
            interface4()
        if cmd == '-SEC https://www.gaypride.fr 80 300':
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')                
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')
                os.system('cls')
                print(Colorate.Horizontal(Colors.white_to_red, """\n\n                                                .^!7~:.    .:               
                          .:!7!^.             .:7B@@&5^....!~               
                         .^5@@&G!:            .^J@@@@B~.:77?:               
                    .:.  .^5@@@@7:            ..^5BPY~:.!GG!                
                     ~J7:..:7JJ7:               .......^JP!                 
                      ~57:                           .~JY^.                 
                       !P5~.         ..             ^!J5^                   
                       :^55?!.       ... .  .    :~7555~.                   
                         :!?5J!7^7~::^^^7~!!:!^?!P5GPY!                     
                           :!7PPP#BGPGBP@5#&7&P5#PP5!^                      
                             :?5&G5BYGBG#?BB7P555B7!.                       
                               .J!5P5YP?G75Y?P?P??.                         
                                 :^~?55?&5#B?BY~^.                          
                                 .  .:::J7J?!^. .                           
                                 .. .      .^                               
                                 .. .       .                               
                                    .                                       
                                    .                                       
                                    ."""))
                time.sleep(0.1)
                os.system('cls')
                print("")
                time.sleep(0.1)
                os.system('cls')

                interface5()
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Error Syntax 404"))
            time.sleep(2)
            main()

if __name__ == '__main__':
    whizen()
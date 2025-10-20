signal=input("Enter the traffic color")

match signal.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("ready")
    case "green":
        print("go")
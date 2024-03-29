import os

def file_contents():
    myfile = open("html.txt", "rt", encoding="utf8")
    contents = myfile.read()
    myfile.close()
    return contents

def file_write(coords):
    coordinates_file = open("coordinates.txt", "a", encoding="utf8")
    coordinates_file.write(coords)
    coordinates_file.close()



def main():
    if os.path.exists("coordinates.txt"):
        os.remove("coordinates.txt")
        print("coordinates.txt removed")
    if os.path.exists("coordinates.js"):
        os.remove("coordinates.js")
        print("coordinates.js removed")
    st = file_contents()
    target = "http://static.maps.2gis.com/1.0?center="
    counter = 0
    point = 0
    file_write("var addressPoints = [\n")
    for i in st:
        start = st.index(i, counter)
        end = start + len(target)
        if st[start:end] == "http://static.maps.2gis.com/1.0?center=":
            coordinates = ""
            for j in st[end:end+30]:
                if j != "&":
                    coordinates = coordinates + f"{j}"
                else:
                    break
            c = coordinates.split(",")
            p = f'{c[1]}, {c[0]}'
            #print(p)                
            #print(f'[{c}, "{point}"],')
            file_write(f'[{p}, "{point}"],\n')
            point += 1
        counter += 1
    file_write("];")
    os.rename("coordinates.txt", "coordinates.js")
    print("coordinates.txt renamed to coordinates.js")

if __name__ == "__main__":
    main()
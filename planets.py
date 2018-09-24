def weight_on_planets():
    weight_input = int(input("What do you weigh on earth? "));
    mars = weight_input * 0.38;
    jupiter = weight_input * 2.34;

    print("\nOn Mars you would weigh %s pounds.\nOn Jupiter you would weigh %s pounds." % (mars, jupiter));


if __name__ == '__main__':
    weight_on_planets()

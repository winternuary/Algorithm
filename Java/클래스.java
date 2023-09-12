class A {
    public void printHello() {
        System.out.println("안녕");
    }

    public int add() {
        return 3;
    }

    public double addDoubles(int a, double b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        A a = new A();

       a.printHello();

        int sumInt = a.add();
        System.out.println(sumInt);

        double sumDouble = a.addDoubles(3, 2.0);
        System.out.println(sumDouble);
    }
}

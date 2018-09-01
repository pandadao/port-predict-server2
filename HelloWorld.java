import java.lang.Thread;

public class HelloWorld{
    private static int inc = 0;

    private static long getId(){

        long id = Long.parseLong(String.valueOf(System.currentTimeMillis())
                .substring(1,10)
                .concat(String.valueOf(inc)));
        inc = (inc+1)%100;
        System.out.println(inc);
        return id;
    }
     public static void main(String []args){
        System.out.println("Hello World");
        long id = 0;
        while(true){
            id = getId();
            System.out.println(id);
            try
            {
                Thread.sleep(1000);
            }
            catch(InterruptedException ex)
            {
                Thread.currentThread().interrupt();
            }
        }

     }
}

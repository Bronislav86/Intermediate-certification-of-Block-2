package Java;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Reader {

    public Reader() {
    }

    public List<String> toRead(){
        File file = new File("Java/input.txt");
        List<String> list = new ArrayList<>();
        BufferedReader br = null;
        try {
        br = new BufferedReader(new FileReader(file));
        } catch (FileNotFoundException e){
            e.getMessage();
        }
        try{
        String text = br.readLine();
        while (text != null) {
            list.add(text);
            text = br.readLine();
        }
        }catch (IOException e){
            e.getMessage();
        }
        try {
            br.close();
        } catch (IOException e){
            e.getMessage();
        }
        return list;
    }
}

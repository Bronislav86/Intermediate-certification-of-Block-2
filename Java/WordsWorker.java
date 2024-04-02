package Java;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class WordsWorker {

    public WordsWorker() {
    }

    public List<String> deleteSpaces(List<String> o){
        if (o.size() == 0) {
            throw new NullPointerException("Файл не содержит слов");
        }

        String[] array = new String[o.size()];
        String word = String.join(" ", o);
        array = word.split(" ");
        List<String> newList = new ArrayList<>();

        for (int i = 0; i < array.length; i++) {
            if (!array[i].equals("")) {
                newList.add(array[i]);
            }
        }

        return newList;
    }

    public int wordsCount(List<String> o) throws NullPointerException {
        int count;
        if (o.size() == 0) {
            throw new NullPointerException("Файл не содержит слова для подсчета");
        }
        return count = o.size();
    }

    public String mostLongWord(List<String> o) {

        String[] array = new String[o.size()];
        String word = String.join(" ", o);
        array = word.split(" ");
        int maxLength = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i].length() > maxLength) {
                maxLength = array[i].length();
                word = array[i];
            }
        }

        return word;
    }

    public Map<String, Integer> inventoryFruits(List<String> o)throws NumberFormatException{

        String[] array = new String[o.size()];
        String word = String.join(" ", o);
        array = word.split(" ");
        Map<String, Integer> myFruits = new HashMap<>();

        for (String item : array) {
            if (item.equals("")) {
                continue;
            }
            if (!myFruits.containsKey(item)) {
                    myFruits.put(item, 1); 
            } else {
                myFruits.put(item, myFruits.get(item) + 1);
            }
        }
        System.out.println("На пикник взяли много разных фруктов и овощей:");
        for (Map.Entry<String, Integer> item : myFruits.entrySet()) {
            System.out.println(item.getKey() + " в количестве " + item.getValue() + " штук(и).");
        }
        return myFruits;
    } 
}

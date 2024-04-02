package Java;

import java.util.ArrayList;
import java.util.List;

class Progarm {

    public static void main(String[] args) {
        Reader reader = new Reader();
        List <String> data = new ArrayList<>(reader.toRead());
        data.remove("");
        
        WordsWorker wd = new WordsWorker();
        data = wd.deleteSpaces(data);
        System.out.println();
        System.out.printf("Мы взяли с собой на пикник %d фруктов и овощей.\n", wd.wordsCount(data));
        System.out.println();
        System.out.printf("Самое длинное название фрукта(овоща): %s\n", wd.mostLongWord(data));
        System.out.println();
        wd.inventoryFruits(data);
    }

}
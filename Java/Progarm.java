package Java;

import java.util.ArrayList;
import java.util.List;

class Progarm {

    public static void main(String[] args) {
        Reader reader = new Reader();
        List <String> data = new ArrayList<>(reader.toRead());
        data.remove("");
        
        WordsWorker wd = new WordsWorker();
        System.out.printf("Файл input.txt содержит %d слов(а).\n", wd.wordsCount(data));
        System.out.printf("Самое длинное слово в фале: %s\n", wd.mostLongWord(data));
    }

}
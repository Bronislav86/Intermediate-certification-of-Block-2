package Java;

import java.util.List;

public class WordsWorker {

    public WordsWorker() {
    }

    public int wordsCount(List<String> o) throws NullPointerException {
        int count = 0;
        if (o.size() == 0) {
            throw new NullPointerException("Файл не содержит слова для подсчета");
        }
        String reString = String.join(", ", o);

        return count = reString.length();
    }

    public String mostLongWord(List<String> o) {
        String word = new String();

        String[] array = new String[o.size()];
        word = String.join(", ", o);
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
}

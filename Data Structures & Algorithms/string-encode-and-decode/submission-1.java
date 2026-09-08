class Solution {

    public String encode(List<String> strs) {
        String encodedstr = "";
        for (String word : strs) {
            int wordlength = word.length();
            encodedstr += String.valueOf(wordlength) + "#" + word;
        }
        return encodedstr;
    }

    public List<String> decode(String str) {
        ArrayList<String> decodedstr = new ArrayList<>();
        int i = 0;
        String getWordLength = "";
        while (i < str.length()) {
            if (!(str.charAt(i) == '#')) {
                getWordLength += str.charAt(i);
                i++;
                continue;
            } else {
                int count = Integer.parseInt(getWordLength);
                String cutString = str.substring(i + 1 , i + count + 1);
                decodedstr.add(cutString);
                getWordLength = "";
                i += 1 + count;
            }
        }
        return decodedstr;
    }
}

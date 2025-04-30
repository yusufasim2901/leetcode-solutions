class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) return false;

        Map<Character,String> p2w = new HashMap<>();
        Map<String,Character> w2p = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char pChar = pattern.charAt(i);
            String w = words[i];
            if (p2w.containsKey(pChar)) {
                if (!p2w.get(pChar).equals(w)) return false;
            } else {
                p2w.put(pChar, w);
            }
            if (w2p.containsKey(w)) {
                if (w2p.get(w) != pChar) return false;
            } else {
                w2p.put(w, pChar);
            }
        }

        return true;
    }
}

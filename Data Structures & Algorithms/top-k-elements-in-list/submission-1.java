class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> elementFreq = new HashMap<>();

        for (int num : nums) {
            if (!elementFreq.containsKey(num)) {
                elementFreq.put(num, 1);
            } else {
                elementFreq.put(num, elementFreq.get(num) + 1);
            }
        }

        ArrayList<Integer> sortKeys = new ArrayList<>(elementFreq.keySet());
        // sort by frequency descending
        Collections.sort(sortKeys, (a, b) -> elementFreq.get(b) - elementFreq.get(a));
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < k; ++i) {
            result.add(sortKeys.get(i));
        }
        int[] resArray = result.stream().mapToInt(Integer::intValue).toArray();
        return resArray;

    }
}

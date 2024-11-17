class Solution {

    public static int numUniqueEmails(String[] emails) {
        Set<String> uniqueEmails = new HashSet<>();
        for (String email : emails) {
            String localName = email.substring(0, email.indexOf('@'));
            localName = localName.replace(".", "");
            if (localName.indexOf('+') >= 0) {
                localName = localName.substring(0, localName.indexOf('+'));
            }
            uniqueEmails.add(localName + email.substring(email.indexOf('@')));
        }

        return uniqueEmails.size();
    }
}
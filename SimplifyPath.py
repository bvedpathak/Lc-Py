'''
You are given an absolute path for a Unix-style file system, which always begins 
with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a 
valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current 
or parent directories.
Return the simplified canonical path.
Time: O(n2) where n is number of words
'''
class Solution(object):
    def simplifyPath(self, path):
        stack = list()
        curr = ""
        for literal in path.split('/'):
            if literal != "":
                if literal == "..":
                    if stack:
                        if curr[-1] == '/':
                            curr = curr[:-1]
                        curr = curr[:-len(stack[-1])]
                        stack.pop()
                elif literal != ".":
                    stack.append(literal)
                    curr += literal if curr and curr[-1] == '/' else '/' + literal
                else:
                    if not curr:
                        curr = literal
            else:
                if not curr:
                    curr = '/'
                else: 
                    curr += '/' if curr[-1] != '/' else ''

        return curr[:-1] if len(curr) > 1 and curr[-1] == '/' else curr

path = "./home//foo/../.."
path = "/home//foo/"
path = "/home/user/Documents/../Pictures"
path = "/../"
path = "/.../a/../b/c/../d/./"
path = "/a/../../b/../c//.//"
print(f"\nSimplified unix path for {path} is: {Solution().simplifyPath(path)}\n")

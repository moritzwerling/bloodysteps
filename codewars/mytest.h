void testequal(std::string ans, std::string sol) {
    Assert::That(ans, Equals(sol));
}


Describe(your_path_finder_function) {
  It(should_work_for_a_few_simple_fixed_tests_involving_small_mazes) {
    /*
      Maze:
        .W.
        .W.
        ...
    */
    Assert::That(path_finder(".W.\n.W.\n..."), Equals(4));
    /*
      Maze:
        .W.
        .W.
        W..
    */
    //Assert::That(path_finder(".W.\n.W.\nW.."), Equals(-1));
    /*
      Maze:
        ......
        ......
        ......
        ......
        ......
        ......
    */
    //Assert::That(path_finder("......\n......\n......\n......\n......\n......"), Equals(10));
    /*
      Maze:
        ......
        ......
        ......
        ......
        .....W
        ....W.
    */
    //Assert::That(path_finder("......\n......\n......\n......\n.....W\n....W."), Equals(-1));
  }
};



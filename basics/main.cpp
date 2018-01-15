#include <functional>
int add_(int n)
{
  static int sum = 0;
  sum += n;
  return sum;
}
auto add(int n)
{
    add_(n);
    std::function<int(int)> f = add_;
    return f;
}



int main(int argc, char *argv[])
{
auto addTwo = add(2);

}






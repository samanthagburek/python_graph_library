#include <nanobind/nanobind.h>

NB_MODULE(_booty_boost, m) { //make this very, very, very simple
    m.def("add", []() { return "Hello world!"; });
}

//int add(int a, int b) { return a + b; }
//
//NB_MODULE(my_ext, m) {
//    m.def("add", &add);
//}

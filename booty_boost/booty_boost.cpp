#include <nanobind/nanobind.h>

int add(int a, int b) { return a + b; }

NB_MODULE(booty_boost, m) {
    m.doc() = "test module with simple add function"
    m.def("add", &add);
}
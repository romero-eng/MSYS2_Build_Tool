#ifndef ARITHMETIC_H
#define ARITHMETIC_H

#ifdef ADD_EXPORTS
  #define ADDAPI __declspec(dllexport)
#else
  #define ADDAPI __declspec(dllimport)
#endif

namespace Arithmetic
{
    ADDAPI int add(int x, int y);

    ADDAPI double add(double x, double y);

    ADDAPI double add(double x, int y);

    ADDAPI double add(int x, double y);

    ADDAPI int subtract(int x, int y);

    ADDAPI double subtract(double x, double y);

    ADDAPI double subtract(double x, int y);

    ADDAPI double subtract(int x, double y);

    ADDAPI int multiply(int x, int y);

    ADDAPI double multiply(double x, double y);

    ADDAPI double multiply(double x, int y);

    ADDAPI double multiply(int x, double y);

    ADDAPI double divide(double x, double y);

    ADDAPI double divide(double x, int y);

    ADDAPI double divide(int x, double y);
}

#endif

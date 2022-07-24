---
layout: default
title: Releases
---

## Latest Releases

You can find the latest stable version of S2E on master. We compile here from time to time a list of important updates.

### 24 July 2022
 * Added support for Ubuntu 22.04 and Debian 11.3 guest images.
 * Removed support for Debian 9 images.
 * Replaced ``s2eget`` and ``s2eput`` with ``s2ecmd get|put``.

### 03 May 2022
 * Upgraded the symbolic execution engine to LLVM 14.
 * Added support for Debian 11 and Ubuntu 22.04 LTS.

### 14 Feb 2021
 * Added control flow integrity checker with Microsoft Office support.
 * ``UserSpaceTracer`` plugin supports per-thread tracing.
 * Added the ``Tickler`` plugin and the corresponding Windows guest tool in order to automatically
   click on dialog boxes while testing Microsoft Office and other apps.
 * Added the ``Screenshot`` plugin in order to record screenshots of the guest.
 * Added a command to ``s2e-env`` to automatically generate S2E plugin boilerplate.

### 16 June 2020
 * Added support for Microsoft Office 2010, 2013, 2016, 2019.
 * Added tutorial about symbolic execution of VBA macros.
 * Improved image building makefile to make it easier to add support for other Windows apps.
 * Better support for seed files in ``s2e new_project``.
 * Added ``libs2e.dll`` to make it easier to call S2E APIs from other programs.
 * Removed Windows 8.1 and 10 1703 images.

### 01 May 2020

 * Upgraded to LLVM 10.0.0.
 * Added support for Ubuntu 20.04 LTS.
 * Updated the Windows 10 image to 1909.
 * Applied latest patches to Windows XP and 7 images (up to 2016 and 2020 respectively).

### 17 Feb 2020
 * Switched the S2E engine [license](https://github.com/S2E/s2e/blob/master/LICENSE) to MIT
 * Upgraded [s2e-env](https://github.com/s2e/s2e-env) to Python 3

### 03 Feb 2020

 * Upgraded to LLVM 9.0.0 from 3.9.1.
 * S2E now compiles with Clang 9.0.
 * Consolidated the 14 repositories that composed ``libs2e`` into a [monorepo](https://github.com/s2e/s2e).
   The old repositories will be deleted after Feb 14.

### 07 Dec 2019

 * Upgraded the code generation backend (TCG, Tiny Code Generator) from version 1.0 to 4.0.
   This is a prerequisite for upgrading the x86 translator to support new instruction sets.
 * Tutorial on how to [profile](https://s2e.systems/docs/Profiling/ProfilingS2E.html) S2E.
 * Fixed memory leaks and optimized memory usage in KLEE. Made all KLEE expressions immutable, merged ``MemoryObject``
   and ``ObjectState``, removed unused fields, use reference counting for all objects, minimize memory allocations, etc.
 * [Optimized](https://github.com/S2E/klee/commit/afaaaaebf0815fa3755cdf07e818efb77c16234d) calling of external
   functions in KLEE. Invoke these functions directly instead of generating complex LLVM stubs for every call site.
 * [Fixed](https://github.com/S2E/klee/commit/3216200aaacae7f124803acbcd79b05855f432d2)
   sign extension in solver interface that was resulting in incorrect solver results.
 * [Fixed](https://github.com/S2E/klee/commit/823ca86f6ca5d03bdbe75d6c1e319b7a7f9d52c8) performance bug in the
   expression simplifier that was causing symbolic execution to get stuck on large expressions.
 * [Upgraded](https://github.com/S2E/build-scripts/commit/9802fee21cc8da3321da72cce237551e280498a7) the docker image
   from Ubuntu 16.04 to 18.04.
 * Ubuntu 16.04 is not supported anymore due to `glib` package issues.

### 29 May 2019

 * Support for symbolic FP/MMX/SSE registers on x86 guests. You can now run programs that use these registers
   without forcing concretizations when symbolic data enters them. Big thanks to [@humeafo](https://github.com/humeafo)
   for implementing this!
 * Added a [testsuite](http://s2e.systems/docs/Testsuite.html). It covers most tutorials and exercises major aspects
   of S2E functionality. This should considerably reduce regressions and make it easier for you to add new features
   without fearing of breaking things.
 * Major performance improvements for concrete/symbolic execution and faster parallel mode.
 * [Code coverage](http://s2e.systems/docs/Howtos/Coverage/index.html) generation is now orders of magnitude faster
   for large binaries. You will get a Linux kernel coverage report in seconds instead of minutes.
 * Plugins now record execution traces in ``protobuf`` format.
 * Fixed guest hangs when running S2E in parallel mode (by
   [Alan Wang](https://www.linkedin.com/in/zhongjie-wang-09001922/)).
 * Many other bug fixes and improvements both in the code and the documentation.

### 14 Jan 2019

 * QEMU 3.0 support
 * Windows 7 32-bit guest support
 * Ubuntu 18.04 host support
 * Documentation updates
    * KVM interface design
    * Testing error recovery code in Windows drivers with multi-path fault injection
    * Using SystemTap with S2E
    * Combining Kaitai Struct and S2E for analyzing parsers
    * Analyzing trigger-based malware with S2E
    * Automated proof of vulnerability generation on Linux, Windows, and Decree platforms
    * Getting code coverage for various types of binaries
    * Setting up Windows development environment
 * Various engine fixes and refactorings

### 16 Oct 2017 - S²E V2.0

 * Rearchitected version of S²E, decoupled from QEMU
 * KVM-compatible interface
   * ``libs2e.so`` is a shim library that intercepts ``ioctl`` to ``/dev/kvm``
   * can be ``LD_PRELOAD``ed into QEMU or any other KVM-compatible VMM.
 * Modular and flexible architecture, any component of S²E can be reused independently
   * ``libs2e``: exposes the symbolic execution engine and the dynamic binary translator through a KVM-compatible
     interface
   * ``libs2ecore``: main S²E execution engine
   * ``libs2eplugins``: S²E plugins
   * ``libcpu``: processor emulation library, extracted from QEMU 1.0
   * ``libtcg``: dynamic binary translator backend, extracted from QEMU 1.0
   * ``libvmi``: virtual machine introspection library
   * ``libq``: JSON serialization support, to interface S²E with Web services, extracted from QEMU 1.0
   * ``libcoroutine``: cooperative threading support, extracted from QEMU 1.0
   * ``libfsigc++``: fast drop-in replacement for the ``libsigc++`` library
   * ``klee``: symbolic LLVM interpreter
   * ``lua``: LUA scripting engine
 * Supports latest versions of Linux and Windows XP, 7, 8, 8.1, 10
   * Windows crash dump generation, compatible with WinDbg
   * Exposes OS events to plugins (process/thread creation/destruction, memory mappings, module loads, etc.)
 * Advanced tooling to easily set up symbolic execution for arbitrary programs
   * Automatic generation of S²E configuration file and launch script based on the binary to analyze
   * Easy file transfers between the guest and the host during symbolic execution, ideal for per-path core dump
     extraction, etc.
   * Code coverage support
 * Up to 6x faster concrete execution than S²E 1.3
 * Z3 constraint solver
 * Extensive set of plugins and tools for vulnerability analysis and proof of vulnerability generation
   * Easily show the exploitability of a crash
   * Demonstrated during the DARPA Cyber Grand Challenge
 * Concolic execution
 * State merging
   * Exponentially reduces number of paths to explore by combining similar execution paths
 * Function models
   * Exponentially reduces number of paths to explore by replacing standard library functions with equivalent models
 * Advanced path searchers
   * Modular searcher architecture, mix and match existing searchers, and combine them with your own
   * Class-Uniform Path Analysis minimizes likelihood of exploration getting stuck
 * Fuzzer integration
   * ``SeedSearcher`` plugin automatically picks up seeds generated by a fuzzer or other analysis tools and schedules
     them for exploration
   * Generate new test cases that can be used to guide fuzzers and other tools
 * Revgen: static x86 to LLVM translator

<hr/>

## Old Releases

The following releases are archived.

### 05 Dec 2013 - S²E V1.3

  * x86-64 guests support, LLVM 3.2

### 27 Apr 2012 - S²E V1.2

  * QEMU 1.0, LLVM 3.0, Clang
  * S²E now includes the latest features of QEMU and uses a modern toolchain
  * Concolic Execution
  * Reuse your existing testsuites to easily reach deep parts of programs under analysis

### 10 Sep 2011 - S²E V1.1

  * Experimental ARM support
  * Analyze embedded applications
  * Available in the arm-experimental branch of the repository
  * Multi-core support
  * Explore orders of magnitude more paths
  * 20x faster plugin infrastructure
  * Complete plugin-intensive analyses such as Windows driver testing in minutes instead of hours
  * 2x faster concrete execution
  * Run bigger systems

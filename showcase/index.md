---
layout: default
title: Showcase
---


## Showcase

S²E is used by many scientific projects across the world. This page lists some of them.
We'll be happy to list yours as well, just drop us a line!


-   **<a href="https://www.usenix.org/conference/usenixsecurity23/presentation/yao-mingxuan">Hiding in Plain Sight: An
    Empirical Study of Web Application Abuse in Malware</a>** at <a href="https://cyfi.ece.gatech.edu/">Georgia
    Institute of Technology CyFI Lab</a> and United States Military Academy (<a
    href="https://mingxuan.ece.gatech.edu/">Mingxuan Yao</a>, et al).

    Web applications provide a wide array of utilities that are abused by malware as a replacement for traditional
    attacker-controlled servers. Thwarting these Web App-Engaged (WAE) malware requires rapid collaboration between
    incident responders and web app providers. We developed Marsea, an automated malware analysis pipeline that uses S2E
    to study WAE malware and enables rapid remediation. Given 10K malware samples, Marsea revealed 893 WAE malware in 97
    families abusing 29 web apps. This research uncovered a 226% increase in the number of WAE malware since 2020. To
    date, we have used Marsea to collaborate with the web app providers to take down 80% of the malicious web app
    content.


-   **<a href="https://www.usenix.org/system/files/osdi20-hu.pdf">Automated Reasoning and Detection of Specious
    Configuration in Large Systems with Symbolic Execution</a>** at Johns Hopkins University
    (Yigong Hu, Gongqi Huang, and Peng Huang).

    This paper introduces Violet — a tool that uses symbolic execution in order to detect software misconfigurations
    that lead to extremely poor performance. Violet makes symbolic the configuration parameters of the program under test,
    which allows the tool to automatically explore the program along paths that depend on these parameters.
    In addition to that, Violet runs a benchmark on each path, making it possible to determine paths that perform poorly,
    while showing users which combinations of parameters actually cause the problem. Violet helped identify
    problematic configurations for MySQL, Postgres, Apache, and Squid, which prompted the maintainers of these systems
    to clarify the documentation.


-   **<a href="https://download.vusec.net/papers/binrec_eurosys20.pdf">
    BinRec: Dynamic Binary Lifting and Recompilation</a>** at University of California (Irvine),
    Vrije Universiteit Amsterdam, KU Leuven (Anil Altinay, Joseph Nash, Taddeus Kroes, et al.).

    BinRec [is a] a new approach to heuristic-free binary recompilation which lifts dynamic traces of a binary to a
    compiler-level intermediate representation (IR) and lowers the IR back to a "recovered" binary.
    This enables BinRec to apply rich program transformations, such as compiler-based optimization passes, on top of
    the recovered representation. [BinRec] can accurately disassemble and lift binaries without heuristics,
    and can successfully recover obfuscated code and all SPEC INT 2006 benchmarks including C++ applications.

    [The] dynamic lifting engine is built on top of S2E, a framework that facilitates symbolic execution of a single
    process running in the QEMU virtual machine. Code is translated to LLVM IR in order to be symbolically executed
    by the KLEE symbolic executor. S2E automatically provides multi-architecture support and sandboxing of input
    binaries, since it is based on QEMU.


-   **<a href="https://publications.cispa.saarland/2922/1/malpity-eurosp2019.pdf">MALPITY: Automatic Identification
    and Exploitation of Tarpit Vulnerabilities in Malware</a>**
    at Saarland University (Sebastian Walla and Christian Rossow).

    This paper proposes techniques to automatically find network inputs that would slow down malware to the point
    of making it unusable (tarpit vulnerabilities). MALPITY uses S2E in single-path mode, taking advantage of
    its powerful instrumentation capabilities in order to monitor malware network activity. This allowed MALPITY to
    find 12 previously unknown vulnerabilities, e.g., in Pushdo, SalityP2P, or bashlite.


-   **<a href="https://www-users.cs.umn.edu/~kjlu/papers/tss.pdf">Unleashing Use-Before-Initialization Vulnerabilities
    in the Linux Kernel Using Targeted Stack Spraying</a>**
    at Georgia Institute of Technology, DFKI, MPI-SWS, CISPA, and Saarland University (Kangjie Lu et al.).

    Kernel stack spraying consists in running syscalls in such a way that their invocation leaves user-controlled
    data on the stack, which can then be used to trigger vulnerabilities from the use of uninitialized variables.
    The implementation of the stack sprayer uses S2E to find as many code paths as possible that have user-controlled
    data on the kernel stack. That data is then matched against subsequent syscalls that happen to have uninitialized
    data at the controlled locations.


-   **<a href="https://www.usenix.org/system/files/conference/woot17/woot17-paper-patrick-evans.pdf">POTUS: Probing
    Off-The-Shelf USB Drivers with Symbolic Fault Injection</a>**
    (<a href="https://www.usenix.org/sites/default/files/conference/protected-files/woot17_slides_patrick-evans.pdf">slides</a>)
    at Royal Holloway, University of London (James Patrick-Evans, Lorenzo Cavallaro, and Johannes Kinder).
    *Awarded Best Paper*.

    USB client device drivers are a haven for software bugs, due to the sheer variety of devices and the tendency
    of maintenance to slip as devices age. At the same time, the high privilege level of drivers makes them a prime
    target for exploitation. We present the design and implementation of POTUS, a system for automatically
    finding vulnerabilities in USB device drivers for Linux, which is based on fault injection, concurrency fuzzing,
    and symbolic execution.

    Built on the S2E framework, POTUS exercises the driver under test in a complete
    virtual machine. It includes a generic USB device that can impersonate arbitrary devices and implements
    a symbolic fault model. With our prototype implementation, we found and confirmed two previously undiscovered
    zero-days in the mainline Linux kernel
    [<a href="https://www.cvedetails.com/cve/CVE-2016-5400/">CVE-2016-5400</a>,
    <a href="https://www.cvedetails.com/cve/CVE-2017-15102/">CVE-2017-15102</a>].
    Furthermore, we show that one of these vulnerabilities can lead to
    a data-only exploit affecting even hardened systems protected with the latest software and hardware defenses.


-   **<a href="https://www.usenix.org/system/files/conference/atc17/atc17-kim.pdf">CAB-Fuzz: Practical Concolic
    Testing Techniques for COTS Operating Systems</a>**
    at Georgia Tech, Purdue University (Su Yong Kim et al.)

    CAB-FUZZ exploits real programs interacting with COTS OSes to construct proper contexts to explore deep and
    complex kernel states without debug information. We applied CAB-FUZZ to Windows 7 and Windows Server 2008 and
    found 21 undisclosed unique crashes, including two local privilege escalation vulnerabilities
    (<a href="https://www.cvedetails.com/cve/CVE-2015-6098/">CVE-2015-6098</a> and
    <a href="https://www.cvedetails.com/cve/CVE-2016-0040/">CVE-2016-0040</a>) and one information disclosure
    vulnerability in a cryptography driver
    (<a href="https://www.cvedetails.com/cve/CVE-2016-7219/">CVE-2016-7219</a>).
    CAB-FUZZ found vulnerabilities that are non-trivial to discover; five vulnerabilities have existed for 14 years,
    and we could trigger them even in the initial version of Windows XP (August 2001).


-   **<a href="https://www.usenix.org/conference/woot15/workshop-program/presentation/bazhaniuk" target="_blank">Symbolic Execution for BIOS Security</a>** at
    Intel Corporation (Oleksandr Bazhaniuk, John Loucaides, Lee Rosenbaum, Mark R. Tuttle, and Vincent Zimmer).

    We are building a tool that uses symbolic execution to search
    for BIOS security vulnerabilities including dangerous memory
    references (call outs) by SMM interrupt handlers in
    UEFI-compliant implementations of BIOS. Given a
    snapshot of SMRAM, the base address of SMRAM, and the address of
    the variable interrupt handler in SMRAM, the tool uses S2E to
    run the KLEE symbolic execution engine to search for concrete
    examples of a call to the interrupt handler that causes the
    handler to read memory outside of SMRAM. We discuss our approach,
    our current status, our plans for the tool, and the obstacles we face.

-   **<a href="http://research.cs.wisc.edu/sonar/projects/symdrive/" target="_blank">Testing Linux Device
    Drivers</a>** at
    University of Wisconsin-Madison (Matthew J. Renzelmann, Asim Kadav,
    and Michael M. Swift). SymDrive is a system for testing Linux and
    FreeBSD drivers without their devices. The system uses symbolic
    execution to remove the need for hardware, and provides three new
    features beyond prior symbolic-testing tools. First, SymDrive
    greatly reduces the effort of testing a new driver with a
    static-analysis and source-to-source transformation tool. Second,
    SymDrive allows checkers to be written as ordinary C and execute in
    the kernel, where they have full access to kernel and driver state.
    Finally, SymDrive provides an execution-tracing tool to identify how
    a patch changes I/O to the device and to compare device driver
    implementations. In applying SymDrive to 21 Linux drivers and 5
    FreeBSD drivers, we found 39 bugs.

-   **<a href="http://dslab.epfl.ch/proj/chef">Chef</a>** at EPFL (Stefan Bucur and George Candea).
    Chef is a platform for obtaining symbolic execution engines for interpreted languages.
    It works by reusing the interpreter itself as an executable language specification, thus
    reducing the effort of obtaining an engine to a matter of days. The resulting engines can
    be used like any other engine for finding bugs, generating high-coverage test suites,
    assisting in debugging, and more.


-   **<a href="http://dslab.epfl.ch/pubs/Achilles.pdf">
    Finding Trojan Message Vulnerabilities in Distributed Systems</a>**
    at EPFL (Radu Banabic, George Candea, and Rachid Guerraoui).
    Achilles helps developers discover Trojan Messages in distributed
    systems, i.e., messages that are accepted as valid by receiver
    nodes, but cannot be generated by any correct sender node. Achilles
    uses S2E to analyze both the client and server nodes of a target
    distributed system. It extracts predicates that define the messages
    that can be generated and accepted, respectively. In a sense, one
    can think of these predicates as representations of the grammar of
    messages in the protocol, as implemented in the client and in the
    server. The predicates are stored in the form of symbolic
    expressions and constraints. After extracting the server and client
    predicates, Achilles computes the predicate that defines Trojan
    messages as the difference between the two. In our evaluation, we
    show how Achilles can discovered Trojan messages in FSP, a file
    transfer system, and PBFT, a Byzantine-Fault-Tolerant State Machine
    Replication library. The Trojan messages discovered by Achilles lead
    to subtle bugs in the respective distributed systems.


-   **File Systems Equivalence Checking** at Max Planck Institute for
    Software Systems (<a href="http://www.mpi-sws.org/index_noflash.php?n=people/Joao_Carreira" target="_blank">Carreira
    João</a>,
    <a href="http://www.mpi-sws.org/~rodrigo/" target="_blank">Rodrigo Rodrigues</a>, <a href="http://www.cs.ucla.edu/~rupak/" target="_blank">Rupak
    Majumdar</a>). The goal of this project
    is to find functional bugs in systems code by checking the
    equivalence of multiple implementations that obey the same
    specification. Checking the equivalence of the different systems is
    performed by comparing the outputs and the logical state of
    different systems after executing the operations in their
    specification. Symbolic execution will allows us to reason about all
    possible executions and results of these operations. We specifically
    intend to apply this approach to find functional bugs in file
    systems.


-   **Corruption Impact Analysis** at University of Wisconsin
    (<a href="http://pages.cs.wisc.edu/~srirams/new_hp_2011/homepage.html" target="_blank">Subramanian
    Sriram</a>,
    <a href="http://pages.cs.wisc.edu/~swami/" target="_blank">Sundararaman Swaminathan</a>,
    <a href="http://pages.cs.wisc.edu/~dusseau/" target="_blank">Andrea C. Arpaci-Dusseau</a>,
    <a href="http://pages.cs.wisc.edu/~remzi/" target="_blank">Remzi Arpaci-Dusseau</a>).
    Corruption Impact Analysis is a novel technique to understand the
    impact of memory corruptions in file systems. We employ selective
    symbolic execution to exhaustively explore the impact of memory
    corruptions on other in-memory data structures, disk and the user.
    Our technique emphasizes the importance of the location of
    corruption in addition to the corrupted data structure. We present a
    detailed case study of applying our technique to Ext2. We identify
    the data structures and code regions most sensitive to corruption
    and present corruption spectrums for each scenario. Thus, our
    technique offers developers the opportunity to improve file system
    reliability without sacrificing performance.

-   **<a href="http://www.comsys.rwth-aachen.de/research/projects/kleenet/" target="_blank">KleeNet
    project</a>**
    at Chair of Communication and Distributed Systems (ComSys), RWTH
    Aachen University (Raimondas
    Sasnauskas,
    <a href="http://www.comsys.rwth-aachen.de/team/klaus/" target="_blank">Klaus Wehrle</a>).
    Within KleeNet project, we are symbolically executing unmodified
    sensornet applications to generate distributed execution paths at
    high-coverage. However, the symbolic execution of Internet
    communication protocols is difficult since the software is not
    self-contained and hence heavily interacts with its surrounding
    environment (OS, libraries). Using S2E, we are able to switch
    between symbolic and native execution in a flexible way with low
    manual effort. Therefore, it allows us to drive the analysis towards
    interesting software parts.

-   **<a href="http://people.engr.ncsu.edu/txie/" target="_blank">Improving Automation in Developer Testing: Cooperative Developer
    Testing</a>** at North Carolina
    State University (<a href="http://people.engr.ncsu.edu/txie/" target="_blank">Xie Tao</a>).
    Developer testing, a common step in software development, involves
    generating sufficient test inputs and checking the behavior of the
    program under test during the execution of the test inputs. This
    project develops novel techniques and tools for improving automation
    in developer testing focusing on improving automation in test
    generation and test oracles. This project also investigates the
    methodology of cooperative developer testing: developers and tools
    cooperate in effectively accomplishing challenging tasks in software
    testing.

-   **Exploiting Parallelism for Effective Low-Level Software Analysis**
    at Institute of Software Chinese Academy of Sciences (<a href="http://124.16.139.203/self_pages/liujian/index.htm" target="_blank">Jian
    Liu</a>, Bin Li,
    Sunlv Wang). In this project, one goal is to analyze typical
    application software and system code such as embedded OS or
    hypervisor. For example, we use S2E to analyze hypercalls in the Xen
    hypervisor. This project also plans to improve performance of S2E.
    We introduce concurrency algorithms and build a framework of
    scheduling rules to maximize the multi-path processing efficiently
    using multi-threading and multi-core processors. We are also
    devising heuristics to reduce the search time and to enhance
    efficiency.

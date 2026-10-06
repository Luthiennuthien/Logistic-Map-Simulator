import numpy as np
import matplotlib.pyplot as plt
import math
import csv

def logistic_map(x, r):
 
    return r * x * (1 - x)


while True:
    print("\n Commands: \nr only\nbifurcation\nlyapunov\nlyapunov graph\nblock entropy\nblock entropy graph\nentropy convergence\nentropy vs lyapunov\n")

    input = input("What operation would you like to do?")


    if input == "r only":

        r = float(input("R Value? "))
        x0 = float(input("Initial Condition? "))
        N = int(input("Total Iterations After Transient? "))
        transient = int(input("To Be Discarded Transient Phase? "))

        total_iterations = transient + N
        print(total_iterations)
        x = np.zeros(total_iterations + 1)
        x[0] = x0


        for n in range(total_iterations):
            x[n + 1] = r * x[n] * (1 - x[n])

        x_plot = x[transient:]

        n_plot = np.arange(transient, total_iterations + 1)


        plt.figure()

        plt.plot(n_plot, x_plot)

        plt.xlabel("Iteration n")
        plt.ylabel("x")
        plt.title(f"Logistic Map (r = {r}, transient = {transient})")

        plt.grid()

        plt.show(block=False)
        plt.pause(0.1)

        x = np.linspace(0, 1, 1000)
        f = logistic_map(x, r)

        plt.figure(figsize=(8, 6))
        plt.plot(x, f, "b-", label=f"Logistic Map ($r={r}$)")
        plt.plot(x, x, "k--", label="$y = x$")

        # Simulate iterations
        print(len(x_plot))
        for i in range(len(x_plot)-1):
            y=x_plot[i]
            plt.plot([x_plot[i], x_plot[i]], [x_plot[i], x_plot[i+1]], "r", lw=0.5)  
            plt.plot([x_plot[i], x_plot[i+1]], [x_plot[i+1], x_plot[i+1]], "r", lw=0.5)  
   

        plt.xlabel("$x_n$", fontsize=12)
        plt.ylabel("$x_{n+1}$", fontsize=12)
        plt.title("Cobweb Plot for the Logistic Map")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.show(block=False)

    elif input == "bifurcation":

        r_min = float(input("Minimum R Value? "))
        r_max = float(input("Maximum R Value? "))
        r_points = 10000

        x0 = 0.4
        transient = 100000
        N = 100

        r_values = np.linspace(r_min, r_max, r_points)


        r_plot = []
        x_plot = []

        for r in r_values:

            x = x0

       
            for n in range(transient):
                x = logistic_map(x, r)

    
                x = logistic_map(x, r)

                r_plot.append(r)
                x_plot.append(x)

      
        plt.figure(figsize=(10, 7))

        plt.plot(
            r_plot,
            x_plot,
            ",",
            alpha=0.5
        )

        plt.xlabel("$r$", fontsize=12)
        plt.ylabel("$x_n$", fontsize=12)
        plt.title("Bifurcation Diagram of the Logistic Map")

        plt.grid(alpha=0.2)
        plt.xlim(r_min, r_max)
        plt.ylim(0, 1)

        plt.show(block=False)
        
    elif input=="lyapunov":
       

        r = float(input("R Value? "))
        x0 = float(input("Initial Condition? "))
        transient = int(input("Transient Iterations? "))
        N = int(input("Iterations for Lyapunov calculation? "))

        x = x0


        for n in range(transient):
            x = r * x * (1 - x)

   
        lyapunov = 0

        for n in range(N):

            derivative = r * (1 - 2 * x)

            lyapunov += np.log(abs(derivative))

            x = r * x * (1 - x)

        lyapunov = lyapunov / N

        print("Lyapunov exponent:", lyapunov)
    elif input == "lyapunov graph":

        r_min = float(input("Minimum R Value? "))
        r_max = float(input("Maximum R Value? "))
        r_points = int(input("Number of R Values? "))

        x0 = float(input("Initial Condition? "))
        transient = int(input("Transient Iterations? "))
        N = int(input("Iterations for Lyapunov Calculation? "))

        r_values = np.linspace(r_min, r_max, r_points)
        lyapunov_values = []

        for r in r_values:

            x = x0


            for n in range(transient):
                x = logistic_map(x, r)

            lyapunov = 0

 
            for n in range(N):

                derivative = r * (1 - 2 * x)

                lyapunov += np.log(abs(derivative))

                x = logistic_map(x, r)

            lyapunov = lyapunov / N

            lyapunov_values.append(lyapunov)


        plt.figure(figsize=(10, 6))

        plt.plot(r_values, lyapunov_values, ".", markersize=1)

        plt.axhline(0, color="black", linewidth=0.8)

        plt.xlabel("$r$")
        plt.ylabel("$\\lambda$")
        plt.title("Lyapunov Exponent vs $r$")

        plt.grid(alpha=0.3)
        plt.show(block=False)
        
    elif input == "block entropy":
        r = float(input("R Value? "))
        x = float(input("Initial Condition? "))
        transient = int(input("Transient Iterations? "))
        N = int(input("Iterations for Entropy calc "))
        Block_Length = int(input("block lengths didddy nigga "))

        block_entropy = []
        sorted_block_entropy = []

        for n in range(transient):
            x = logistic_map(x, r)

        for i in range(N):
            x = logistic_map(x, r)

            if x < 0.5:
                block_entropy.append("0")
            else:
                block_entropy.append("1")

        for z in range(len(block_entropy) // Block_Length):
            start = z * Block_Length
            end = start + Block_Length
            sorted_block_entropy.append("".join(block_entropy[start:end]))

        cases = {}

        for i in range(2 ** Block_Length):
            case = format(i, f"0{Block_Length}b")
            cases[case] = 0

        for block in sorted_block_entropy:
            cases[block] += 1

        total_blocks = len(sorted_block_entropy)

        probabilities = {}

        for case in cases:
            probabilities[case] = cases[case] / total_blocks

        entropy = 0

        for probability in probabilities.values():
            if probability > 0:
                entropy -= probability * math.log2(probability)

        
        print(sorted_block_entropy)
        
        print("Block Entropy:", entropy)

    elif input == "block entropy graph":
            r_min = float(input("Minimum R Value? "))
            r_max = float(input("Maximum R Value? "))
            r_points = int(input("Number of R Values? "))

            x0 = float(input("Initial Condition? "))
            transient = int(input("Transient Iterations? "))
            N = int(input("Iterations for Entropy calc? "))
            Block_Length = int(input("block lengths didddy nigga "))

            r_values = np.linspace(r_min, r_max, r_points)
            entropy_values = []

            for r in r_values:
                x = x0

                for n in range(transient):
                    x = logistic_map(x, r)

                block_entropy = []
                for i in range(N):
                    x = logistic_map(x, r)
                    if x < 0.5:
                        block_entropy.append("0")
                    else:
                        block_entropy.append("1")

                sorted_block_entropy = []
                for z in range(len(block_entropy) // Block_Length):
                    start = z * Block_Length
                    end = start + Block_Length
                    sorted_block_entropy.append("".join(block_entropy[start:end]))

                cases = {}
                for i in range(2 ** Block_Length):
                    case = format(i, f"0{Block_Length}b")
                    cases[case] = 0

                for block in sorted_block_entropy:
                    cases[block] += 1

                total_blocks = len(sorted_block_entropy)

                entropy = 0
                if total_blocks > 0:
                    for count in cases.values():
                        probability = count / total_blocks
                        if probability > 0:
                            entropy -= probability * math.log2(probability)

                entropy_values.append(entropy)

            plt.figure(figsize=(10, 6))
            plt.plot(r_values, entropy_values, ".", markersize=2)

            plt.xlabel("$r$")
            plt.ylabel("Block Entropy (bits)")
            plt.title(f"Block Entropy vs $r$ (block length = {Block_Length})")

            plt.grid(alpha=0.3)
            plt.show(block=False)

    elif input == "entropy convergence":
            r = float(input("R Value? "))
            x = float(input("Initial Condition? "))
            transient = int(input("Transient Iterations? "))
            N = int(input("Iterations for Entropy calc? "))
            L_max = int(input("Maximum Block Length? "))

            for n in range(transient):
                x = logistic_map(x, r)

            symbols = []
            for i in range(N):
                x = logistic_map(x, r)
                symbols.append("0" if x < 0.5 else "1")
            seq = "".join(symbols)

            L_values = list(range(1, L_max + 1))
            H_values = []

            for L in L_values:
                counts = {}
                n_blocks = N - L + 1              

                for i in range(n_blocks):
                    w = seq[i:i + L]
                    counts[w] = counts.get(w, 0) + 1

                H_L = 0
                for c in counts.values():
                    p = c / n_blocks
                    H_L -= p * math.log2(p)

                H_values.append(H_L)


            h_values = [H_values[i + 1] - H_values[i] for i in range(len(H_values) - 1)]
            h_L_values = L_values[:-1]

            print("L    H_L")
            for L, H_L in zip(L_values, H_values):
                print(f"{L:<4} {H_L:.4f}")
            print("\nL    h_L = H_(L+1) - H_L")
            for L, h_L in zip(h_L_values, h_values):
                print(f"{L:<4} {h_L:.4f}")


            plt.figure(figsize=(8, 5))
            plt.plot(L_values, H_values, "o-")
            plt.xlabel("Block length $L$")
            plt.ylabel("$H_L$ (bits)")
            plt.title(f"Block Entropy $H_L$ vs $L$ (r = {r})")
            plt.grid(alpha=0.3)
            plt.show(block=False)

       
            plt.figure(figsize=(8, 5))
            plt.plot(h_L_values, h_values, "o-")
            plt.xlabel("Block length $L$")
            plt.ylabel("$h_L = H_{L+1} - H_L$ (bits/symbol)")
            plt.title(f"Entropy Increment $h_L$ vs $L$ (r = {r})")
            plt.grid(alpha=0.3)
            plt.show(block=False)
    elif input == "entropy vs lyapunov":
        r_min = float(input("Minimum R Value? "))
        r_max = float(input("Maximum R Value? "))
        r_points = int(input("Number of R Values? "))
        x0 = float(input("Initial Condition? "))
        transient = int(input("Transient Iterations? "))
        N = int(input("Iterations per R (entropy + Lyapunov)? "))
        L_max = int(input("Maximum Block Length? "))

        r_values = np.linspace(r_min, r_max, r_points)
        h_plateau = []
        lyap_bits = []
        bif_r = []
        bif_x = []

        for r in r_values:
            x = x0
            for n in range(transient):
                x = logistic_map(x, r)

    
            bits = np.empty(N, dtype=np.int64)
            lyap_sum = 0.0
            for i in range(N):
                bits[i] = 0 if x < 0.5 else 1
                lyap_sum += math.log(max(abs(r * (1 - 2 * x)), 1e-300))
                if i >= N - 100:
                    bif_r.append(r)
                    bif_x.append(x)
                x = logistic_map(x, r)


            H_values = []
            codes = bits
            for L in range(1, L_max + 1):
                if L > 1:
                    n_blocks = N - L + 1
                    codes = (codes[:n_blocks] << 1) | bits[L - 1:L - 1 + n_blocks]
                counts = np.bincount(codes, minlength=2 ** L)
                p = counts[counts > 0] / len(codes)
                H_values.append(-np.sum(p * np.log2(p)))

            h_values = np.diff(H_values)         
            h_plateau.append(h_values[-1])    
            lyap_bits.append(max(lyap_sum / N, 0) / math.log(2))   

        h_plateau = np.array(h_plateau)
        lyap_bits = np.array(lyap_bits)
        residual = h_plateau - lyap_bits

        k = np.argmax(np.abs(residual))
        print(f"Largest residual: {residual[k]:.4f} at r = {r_values[k]:.4f}")
        print(f"Mean |residual| (r where lyapunov > 0): "
              f"{np.mean(np.abs(residual[lyap_bits > 0])):.4f}")

        fig, axes = plt.subplots(3, 1, figsize=(10, 11), sharex=True)

        axes[0].plot(bif_r, bif_x, ",", alpha=0.5)
        axes[0].set_ylabel("$x_n$")
        axes[0].set_title("Bifurcation diagram")

        axes[1].plot(r_values, lyap_bits, "-", label=r"$\max(\lambda,0)/\ln 2$")
        axes[1].plot(r_values, h_plateau, "o", ms=2, label=f"$h_L$ plateau (L = {L_max - 1})")
        axes[1].set_ylabel("bits / symbol")
        axes[1].legend()
        axes[1].grid(alpha=0.3)

        axes[2].plot(r_values, residual, "-")
        axes[2].axhline(0, color="black", linewidth=0.8)
        axes[2].set_ylabel(r"$h_L - \max(\lambda,0)/\ln 2$")
        axes[2].set_xlabel("$r$")
        axes[2].grid(alpha=0.3)

        plt.tight_layout()
        plt.show(block=False)
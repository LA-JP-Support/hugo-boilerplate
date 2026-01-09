---
title: "AlphaFold"
date: 2026-01-08
translationKey: AlphaFold
description: "AlphaFold is DeepMind's AI system that predicts protein structures from amino acid sequences, revolutionizing structural biology and drug discovery."
keywords:
- AlphaFold
- protein structure prediction
- artificial intelligence
- structural biology
- drug discovery
category: "Application & Use-Cases"
type: glossary
draft: false
---

## What is an AlphaFold?

AlphaFold is a groundbreaking artificial intelligence system developed by DeepMind that predicts the three-dimensional structure of proteins from their amino acid sequences with unprecedented accuracy. This revolutionary deep learning system represents one of the most significant breakthroughs in computational biology, solving a fundamental challenge that has puzzled scientists for over fifty years known as the "protein folding problem." The system utilizes advanced neural network architectures, particularly attention mechanisms and geometric deep learning, to analyze the complex relationships between amino acid sequences and their corresponding three-dimensional structures. AlphaFold's predictions achieve atomic-level accuracy comparable to experimental methods, enabling researchers to understand protein function, design new therapeutics, and accelerate biological discoveries across multiple disciplines. The system has been trained on vast datasets of known protein structures and evolutionary information, allowing it to capture the intricate patterns and constraints that govern how proteins fold into their functional conformations.

Traditional approaches to determining protein structure have relied heavily on experimental techniques such as X-ray crystallography, nuclear magnetic resonance spectroscopy, and cryo-electron microscopy, which are time-consuming, expensive, and technically challenging processes that can take months or years to complete for a single protein. AlphaFold fundamentally transforms this paradigm by providing accurate structural predictions in a matter of hours or days, democratizing access to structural information and enabling researchers worldwide to study proteins that were previously inaccessible through experimental methods. The system's ability to predict structures for proteins across all domains of life, including those from understudied organisms and challenging membrane proteins, has opened new avenues for research in areas ranging from antibiotic resistance to crop improvement. Unlike traditional computational methods that relied on homology modeling or physics-based simulations with limited accuracy, AlphaFold leverages the power of artificial intelligence to learn directly from evolutionary patterns and structural principles encoded in protein databases, resulting in predictions that often surpass the accuracy of previous computational approaches by orders of magnitude.

The business and scientific impact of AlphaFold extends far beyond academic research, creating substantial value across pharmaceutical, biotechnology, and agricultural industries while accelerating the pace of scientific discovery in ways that generate measurable economic and societal benefits. Pharmaceutical companies are utilizing AlphaFold predictions to identify new drug targets, optimize lead compounds, and reduce the time and cost associated with drug development pipelines, potentially saving billions of dollars in research and development expenses. The system has enabled the creation of the AlphaFold Protein Structure Database, which provides free access to over 200 million protein structure predictions covering nearly every known protein, representing a public resource valued at billions of dollars if generated through traditional experimental methods. Biotechnology companies are leveraging these predictions to engineer enzymes for industrial applications, develop new biomaterials, and create innovative therapeutic approaches, while agricultural researchers are using the structural insights to develop crops with improved nutritional content and resistance to environmental stresses. The democratization of protein structural information has accelerated research timelines, enabled smaller research groups to compete with well-funded laboratories, and fostered international collaboration on global health challenges, demonstrating how artificial intelligence can serve as a powerful tool for advancing human knowledge and addressing societal needs.

## Core Deep Learning Technologies

<strong>Attention Mechanisms</strong>- AlphaFold employs sophisticated attention mechanisms that allow the neural network to focus on relevant parts of the protein sequence and identify long-range interactions between amino acids that are crucial for proper folding. These mechanisms enable the system to capture dependencies across the entire protein sequence, regardless of distance, which is essential for understanding how distant parts of a protein can influence each other's structural arrangement.

<strong>Evolutionary Multiple Sequence Alignments</strong>- The system leverages evolutionary information by analyzing multiple sequence alignments of related proteins across different species, extracting patterns that reveal which amino acid positions are conserved and which can vary while maintaining structural integrity. This evolutionary context provides crucial constraints that guide the folding prediction process and help distinguish between plausible and implausible structural configurations.

<strong>Geometric Deep Learning</strong>- AlphaFold incorporates geometric deep learning principles that explicitly model the three-dimensional nature of protein structures, using specialized neural network architectures that can reason about spatial relationships, angles, and distances between atoms. This approach allows the system to maintain geometric consistency throughout the prediction process and generate physically realistic protein conformations.

<strong>Transformer Architecture</strong>- The system builds upon transformer neural network architectures, originally developed for natural language processing, adapting them to understand the "language" of protein sequences and their structural relationships. These architectures excel at capturing complex patterns and dependencies in sequential data, making them particularly well-suited for analyzing protein sequences and predicting their folding patterns.

<strong>End-to-End Differentiable Structure Module</strong>- AlphaFold features a sophisticated structure module that directly predicts atomic coordinates while maintaining differentiability throughout the entire pipeline, allowing for efficient training and optimization. This module incorporates physical constraints and geometric principles to ensure that predicted structures are chemically and physically plausible.

<strong>Iterative Refinement Process</strong>- The system employs an iterative refinement approach that progressively improves structural predictions through multiple rounds of processing, similar to how proteins fold in nature through a series of intermediate states. This iterative process allows the system to correct initial errors and converge on increasingly accurate structural predictions.

<strong>Multi-Scale Feature Integration</strong>- AlphaFold integrates features at multiple scales, from individual amino acid properties to secondary structure elements to global fold topology, creating a comprehensive representation that captures the hierarchical nature of protein structure. This multi-scale approach enables the system to make accurate predictions across different levels of structural organization.

## How AlphaFold Works

1. <strong>Sequence Input and Preprocessing</strong>- The process begins with inputting the target protein's amino acid sequence, which is then preprocessed to extract relevant features such as amino acid properties, sequence length, and compositional characteristics. The system also performs quality checks to ensure the sequence is valid and suitable for structural prediction.

2. <strong>Multiple Sequence Alignment Generation</strong>- AlphaFold searches large protein databases to identify homologous sequences and generates multiple sequence alignments that reveal evolutionary relationships and conservation patterns. This step is crucial for understanding which parts of the protein are structurally important and which regions may be more flexible or variable.

3. <strong>Evolutionary Feature Extraction</strong>- The system analyzes the multiple sequence alignments to extract evolutionary features, including co-evolution signals that indicate which amino acid positions tend to change together, suggesting potential structural contacts. These features provide valuable constraints that guide the folding prediction process.

4. <strong>Neural Network Processing</strong>- The extracted features are fed into AlphaFold's deep neural network, which processes the information through multiple layers of attention mechanisms and geometric reasoning modules. The network learns to identify patterns and relationships that are indicative of specific structural arrangements and folding motifs.

5. <strong>Distance and Angle Prediction</strong>- The neural network generates predictions for inter-residue distances and backbone angles, creating a detailed map of spatial relationships between different parts of the protein. These predictions serve as constraints that define the overall shape and organization of the protein structure.

6. <strong>Structure Assembly</strong>- Using the predicted distances and angles as constraints, AlphaFold assembles a three-dimensional protein structure through a differentiable structure module that optimizes atomic coordinates. This process ensures that the final structure satisfies both the predicted constraints and fundamental physical principles.

7. <strong>Iterative Refinement</strong>- The system performs multiple rounds of refinement, progressively improving the structural prediction by identifying and correcting inconsistencies or errors. Each iteration allows the network to reconsider its predictions in light of the emerging overall structure.

8. <strong>Confidence Assessment</strong>- AlphaFold generates confidence scores for different regions of the predicted structure, indicating which parts are likely to be accurate and which may be less reliable. This confidence assessment helps researchers understand the limitations and reliability of specific structural predictions.

9. <strong>Final Structure Optimization</strong>- The system performs final optimization steps to ensure the predicted structure is physically realistic and chemically plausible, adjusting bond lengths, angles, and other geometric parameters as needed.

10. <strong>Output Generation</strong>- AlphaFold produces the final protein structure in standard formats along with confidence scores and additional metadata, making the results accessible for further analysis and research applications.

<strong>Example Workflow:</strong>A researcher studying a newly discovered enzyme from an extremophile organism inputs the 300-amino acid sequence into AlphaFold. The system searches protein databases and identifies 1,000 related sequences from various organisms, generating a multiple sequence alignment that reveals highly conserved active site residues and variable surface loops. The neural network processes this evolutionary information along with the target sequence, predicting that residues 45 and 156 are likely to be in close contact despite being distant in the sequence. The structure assembly module uses these distance predictions along with thousands of other constraints to build a three-dimensional model showing a classic enzyme fold with a deep active site pocket. The confidence assessment indicates high reliability for the core structure but lower confidence for several surface loops, guiding the researcher to focus experimental validation efforts on the most uncertain regions while using the high-confidence core structure for drug design efforts.

## Key Benefits

<strong>Unprecedented Speed</strong>- AlphaFold can predict protein structures in hours or days compared to months or years required for experimental determination, accelerating research timelines and enabling rapid hypothesis testing. This dramatic speed improvement allows researchers to study multiple protein variants or conduct large-scale structural surveys that would be impractical using traditional experimental approaches.

<strong>Cost-Effective Structure Determination</strong>- The system eliminates the need for expensive experimental equipment and specialized facilities, reducing the cost of obtaining structural information from hundreds of thousands of dollars per protein to essentially free. This cost reduction democratizes access to structural biology and enables resource-constrained research groups to pursue ambitious structural studies.

<strong>Global Accessibility</strong>- AlphaFold predictions are freely available through online databases, providing researchers worldwide with immediate access to structural information regardless of their institutional resources or geographic location. This global accessibility has particularly benefited researchers in developing countries and smaller institutions who previously lacked access to structural biology facilities.

<strong>Coverage of Difficult Targets</strong>- The system can predict structures for proteins that are challenging or impossible to study experimentally, including membrane proteins, intrinsically disordered regions, and proteins from extremophile organisms. This expanded coverage opens new research opportunities and enables the study of previously inaccessible biological systems.

<strong>Consistency and Reproducibility</strong>- Unlike experimental methods that can be affected by crystallization conditions or sample preparation artifacts, AlphaFold provides consistent and reproducible predictions that can be easily shared and validated across different research groups. This consistency facilitates collaborative research and enables more reliable comparative studies.

<strong>Integration with Computational Workflows</strong>- AlphaFold predictions can be seamlessly integrated into computational drug discovery pipelines, molecular dynamics simulations, and other computational biology workflows, enhancing the efficiency and accuracy of these approaches. This integration capability makes structural information more actionable for downstream applications.

<strong>Evolutionary Insights</strong>- The system's reliance on evolutionary information provides insights into protein evolution and conservation patterns, helping researchers understand which structural features are essential for function and which can be modified. These evolutionary insights inform protein engineering efforts and help predict the effects of mutations.

<strong>Scalability</strong>- AlphaFold can process large numbers of proteins simultaneously, enabling genome-wide structural studies and comparative analyses across entire proteomes. This scalability has enabled the creation of comprehensive structural databases covering millions of proteins from thousands of organisms.

<strong>Quality Assessment</strong>- The system provides confidence scores that help researchers assess the reliability of different structural regions, enabling informed decision-making about which parts of a prediction are suitable for specific applications. This quality assessment feature helps prevent misinterpretation of uncertain structural predictions.

<strong>Complementarity with Experiments</strong>- AlphaFold predictions serve as excellent starting points for experimental structure determination, providing initial models that can guide crystallization efforts and help interpret experimental data. This complementarity enhances rather than replaces experimental approaches, leading to more efficient and successful structural studies.

## Common Use Cases

<strong>Drug Target Identification</strong>- Pharmaceutical companies use AlphaFold predictions to identify and characterize potential drug targets, particularly for diseases where traditional experimental approaches have been unsuccessful. The structural insights help researchers understand binding sites, allosteric mechanisms, and druggability assessments for novel therapeutic targets.

<strong>Structure-Based Drug Design</strong>- Medicinal chemists leverage AlphaFold structures to design small molecule inhibitors and other therapeutic compounds, using the predicted binding sites to guide molecular docking and lead optimization efforts. This application has accelerated drug discovery timelines and improved the success rates of early-stage drug development programs.

<strong>Protein Engineering and Design</strong>- Biotechnology companies utilize structural predictions to engineer enzymes with improved properties, design new protein functions, and optimize existing proteins for industrial applications. The structural insights guide rational design strategies and help predict the effects of specific mutations on protein stability and function.

<strong>Understanding Disease Mechanisms</strong>- Researchers studying genetic diseases use AlphaFold predictions to understand how disease-causing mutations affect protein structure and function, providing insights into pathogenic mechanisms. This understanding helps develop targeted therapeutic strategies and improve genetic counseling for patients with inherited disorders.

<strong>Agricultural Biotechnology</strong>- Agricultural researchers apply AlphaFold predictions to study plant proteins involved in stress resistance, nutritional content, and crop yield, enabling the development of improved crop varieties. These applications contribute to food security efforts and sustainable agriculture practices.

<strong>Antibiotic Resistance Research</strong>- Microbiologists use structural predictions to understand resistance mechanisms in pathogenic bacteria and identify new targets for antimicrobial development. This research is crucial for addressing the growing global threat of antibiotic-resistant infections.

<strong>Vaccine Development</strong>- Immunologists leverage AlphaFold structures to design more effective vaccines by understanding the three-dimensional organization of viral proteins and identifying optimal epitopes for immune recognition. This application has proven particularly valuable for emerging infectious diseases and pandemic preparedness.

<strong>Evolutionary Biology Studies</strong>- Evolutionary biologists use structural predictions to study protein evolution, understand functional constraints, and trace the evolutionary history of protein families across different species. These studies provide insights into the fundamental principles governing protein evolution and adaptation.

<strong>Membrane Protein Research</strong>- Researchers studying membrane proteins, which are notoriously difficult to crystallize, rely on AlphaFold predictions to understand their structure and function in cellular membranes. This research is essential for understanding cellular transport, signaling, and energy conversion processes.

<strong>Structural Genomics Initiatives</strong>- Large-scale genomics projects incorporate AlphaFold predictions to provide structural annotations for newly sequenced genomes, enhancing the functional understanding of genetic information. These initiatives contribute to comprehensive biological databases and support comparative genomics research.

## Protein Structure Prediction Methods Comparison

| Method | Accuracy | Speed | Cost | Coverage | Experimental Requirements |
|--------|----------|-------|------|----------|---------------------------|
| X-ray Crystallography | Very High | Months-Years | $100K-500K | Limited | Protein crystallization, synchrotron access |
| NMR Spectroscopy | High | Months | $50K-200K | Small proteins | Isotope labeling, specialized equipment |
| Cryo-EM | High | Weeks-Months | $20K-100K | Large complexes | Sample preparation, electron microscope |
| AlphaFold | High | Hours-Days | Free | Universal | Sequence only |
| Homology Modeling | Moderate | Hours | Low | Template-dependent | Known homolog structure |
| Ab Initio Methods | Low-Moderate | Days-Weeks | Moderate | Universal | Computational resources |

## Challenges and Considerations

<strong>Confidence Assessment Interpretation</strong>- Users must carefully interpret AlphaFold's confidence scores and understand that low-confidence regions may still contain valuable structural information, while high-confidence predictions are not guaranteed to be perfect. Proper interpretation requires understanding the relationship between confidence scores and actual structural accuracy for different types of protein regions.

<strong>Dynamic and Flexible Regions</strong>- AlphaFold predictions represent static structures and may not accurately capture highly dynamic or intrinsically disordered regions that adopt multiple conformations in solution. Researchers must consider protein flexibility and dynamics when interpreting predictions and designing experiments based on structural models.

<strong>Ligand Binding and Conformational Changes</strong>- The system predicts apo structures without bound ligands or cofactors, which may differ significantly from biologically relevant holo structures that undergo conformational changes upon binding. This limitation requires careful consideration when using predictions for drug design or understanding protein-ligand interactions.

<strong>Membrane Protein Environment</strong>- While AlphaFold can predict membrane protein structures, these predictions do not account for the specific lipid environment or membrane composition that can significantly influence protein conformation and function. Researchers must consider the native membrane environment when interpreting predictions for membrane proteins.

<strong>Protein-Protein Interactions</strong>- The system primarily predicts individual protein structures and has limited capability for modeling protein complexes or protein-protein interactions accurately. Understanding biological function often requires knowledge of how proteins interact with their partners, which may not be captured in individual structure predictions.

<strong>Evolutionary Bias</strong>- AlphaFold's reliance on evolutionary information means that predictions may be less accurate for proteins with few homologs or those from poorly studied organisms. This bias can limit the system's effectiveness for studying novel protein families or proteins from understudied species.

<strong>Validation and Experimental Confirmation</strong>- Despite high accuracy, AlphaFold predictions should be validated through experimental approaches when possible, particularly for critical applications such as drug design or understanding disease mechanisms. The predictions serve as hypotheses that require experimental testing rather than definitive structural determinations.

<strong>Computational Resource Requirements</strong>- While using pre-computed predictions is free, running AlphaFold independently requires significant computational resources and technical expertise, potentially limiting access for some research groups. The computational demands may also limit the ability to predict structures for very large proteins or protein complexes.

<strong>Version Control and Updates</strong>- As AlphaFold continues to improve, researchers must track which version of predictions they are using and understand how updates might affect their results. Version control becomes particularly important for reproducibility and when comparing results across different studies.

<strong>Integration with Experimental Data</strong>- Effectively combining AlphaFold predictions with experimental data requires sophisticated approaches and careful consideration of the strengths and limitations of both computational and experimental methods. This integration challenge requires interdisciplinary expertise and collaborative approaches between computational and experimental researchers.

## Implementation Best Practices

<strong>Confidence Score Analysis</strong>- Always examine confidence scores carefully and focus experimental validation efforts on regions with lower confidence while using high-confidence regions for computational analyses. Understand that confidence scores are region-specific and that different applications may require different confidence thresholds for reliable use.

<strong>Comparative Structure Analysis</strong>- Compare AlphaFold predictions with available experimental structures of homologous proteins to assess local accuracy and identify potential discrepancies. This comparative approach helps calibrate expectations and identify regions where the prediction may be less reliable.

<strong>Functional Annotation Integration</strong>- Combine structural predictions with functional annotations, sequence conservation data, and experimental evidence to develop comprehensive understanding of protein function. This integrated approach provides more robust insights than relying solely on structural information.

<strong>Experimental Validation Planning</strong>- Design targeted experiments to validate critical aspects of AlphaFold predictions, particularly for regions that are functionally important or have lower confidence scores. Focus validation efforts on features that are most relevant to your specific research questions or applications.

<strong>Multi-Template Modeling</strong>- When available, compare AlphaFold predictions with structures generated using other computational methods or experimental templates to identify consistent features and potential discrepancies. This multi-method approach increases confidence in reliable structural features.

<strong>Dynamic Considerations</strong>- Supplement static AlphaFold predictions with molecular dynamics simulations or other methods to understand protein flexibility and dynamics. Consider how conformational changes might affect the biological relevance of the predicted structure.

<strong>Literature Integration</strong>- Thoroughly review existing literature on the protein of interest and related family members to contextualize AlphaFold predictions within known functional and structural information. This integration helps identify potential inconsistencies and guides interpretation of predictions.

<strong>Collaborative Validation</strong>- Engage with experimental collaborators early in the research process to design validation experiments and ensure that computational predictions address experimentally testable hypotheses. This collaborative approach maximizes the value of both computational and experimental efforts.

<strong>Database Version Tracking</strong>- Maintain careful records of which version of AlphaFold predictions you are using and monitor for updates that might affect your results. Establish protocols for incorporating updated predictions into ongoing research projects.

<strong>Quality Control Workflows</strong>- Develop standardized workflows for assessing prediction quality, including automated checks for geometric plausibility, comparison with known structures, and integration with experimental constraints. These workflows help ensure consistent and reliable use of structural predictions across different projects.

## Advanced Techniques

<strong>AlphaFold-Multimer Applications</strong>- Advanced users leverage AlphaFold's multimer capabilities to predict protein complex structures and protein-protein interactions, though these predictions require careful validation and interpretation. The multimer version enables modeling of homo- and hetero-oligomeric complexes, providing insights into quaternary structure organization and interface regions.

<strong>Confidence-Guided Molecular Dynamics</strong>- Researchers combine AlphaFold predictions with molecular dynamics simulations, using confidence scores to apply appropriate restraints and validate structural stability. This approach allows exploration of protein dynamics while maintaining structural integrity in high-confidence regions and permitting flexibility in uncertain areas.

<strong>Hybrid Experimental-Computational Approaches</strong>- Advanced practitioners integrate AlphaFold predictions with experimental data from techniques like cross-linking mass spectrometry, small-angle X-ray scattering, or hydrogen-deuterium exchange to refine structural models. These hybrid approaches leverage the strengths of both computational predictions and experimental constraints to achieve higher accuracy.

<strong>Structure-Based Virtual Screening</strong>- Computational biologists use AlphaFold structures as starting points for large-scale virtual screening campaigns, employing sophisticated docking algorithms and machine learning approaches to identify potential drug candidates. These applications require careful consideration of binding site accuracy and conformational flexibility.

<strong>Evolutionary Coupling Analysis</strong>- Researchers combine AlphaFold predictions with evolutionary coupling analysis to identify functionally important residue networks and allosteric pathways within proteins. This approach provides insights into protein evolution and functional mechanisms that extend beyond static structural information.

<strong>Machine Learning Feature Engineering</strong>- Advanced users extract structural features from AlphaFold predictions to train machine learning models for predicting protein function, stability, or other properties. These applications leverage the rich structural information encoded in AlphaFold predictions as input features for downstream predictive models.

## Future Directions

<strong>Real-Time Conformational Sampling</strong>- Future developments aim to predict multiple protein conformations and dynamic states rather than single static structures, providing more complete pictures of protein behavior in biological systems. This advancement would enable better understanding of protein flexibility and conformational changes associated with function.

<strong>Improved Complex Prediction</strong>- Ongoing research focuses on enhancing the accuracy of protein complex predictions and modeling larger multi-protein assemblies with greater reliability. These improvements will enable better understanding of cellular machinery and protein interaction networks.

<strong>Integration with Cellular Context</strong>- Future versions may incorporate cellular environment factors such as pH, ionic strength, and crowding effects to provide more biologically relevant structural predictions. This contextual modeling would improve the accuracy of predictions for proteins in their native cellular environments.

<strong>Enhanced Ligand Binding Prediction</strong>- Development efforts are directed toward predicting protein structures in complex with ligands, cofactors, and other binding partners to better support drug discovery applications. This capability would provide more relevant structural models for understanding protein function and designing therapeutic interventions.

<strong>Temporal Structure Prediction</strong>- Research is progressing toward predicting how protein structures change over time, including folding pathways and conformational transitions associated with function. This temporal dimension would provide unprecedented insights into protein mechanisms and dynamics.

<strong>Personalized Structure Prediction</strong>- Future applications may enable prediction of how genetic variants affect individual protein structures, supporting personalized medicine approaches and precision therapeutics. This capability would help predict the structural consequences of patient-specific mutations and guide treatment decisions.

## References

Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S. A. A., Ballard, A. J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., Back, T., Petersen, S., Reiman, D., Clancy, E., Zielinski, M., Steinegger, M., Pacholska, M., Berghammer, T., Bodenstein, S., Silver, D., Vinyals, O., Senior, A. W., Kavukcuoglu, K., Kohli, P., & Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873), 583-589.

Varadi, M., Anyango, S., Deshpande, M., Nair, S., Natassia, C., Yordanova, G., Yuan, D., Stroe, O., Wood, G., Laydon, A., Žídek, A., Green, T., Tunyasuvunakool, K., Petersen, S., Jumper, J., Clancy, E., Green, R., Vora, A., Lutfi, M., Figurnov, M., Cowie, A., Hobbs, N., Kohli, P., Kleywegt, G., Birney, E., Hassabis, D., & Velankar, S. (2022). AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models. Nucleic Acids Research, 50(D1), D439-D444.

Senior, A. W., Evans, R., Jumper, J., Kirkpatrick, J., Sifre, L., Green, T., Qin, C., Žídek, A., Nelson, A. W. R., Bridgland, A., Penedones, H., Petersen, S., Simonyan, K., Crossan, S., Kohli, P., Jones, D. T., Silver, D., Kavukcuoglu, K., & Hassabis, D. (2020). Improved protein structure prediction using potentials from deep learning. Nature, 577(7792), 706-710.

Tunyasuvunakool, K., Adler, J., Wu, Z., Green, T., Zielinski, M., Žídek, A., Bridgland, A., Cowie, A., Meyer, C., Laydon, A., Velankar, S., Kleywegt, G. J., Bateman, A., Evans, R., Pritzel, A., Figurnov, M., Ronneberger, O., Bates, R., Kohl, S. A. A., Potapenko, A., Ballard, A. J., Romera-Paredes, B., Nikolov, S., Jain, R., Clancy, E., Reiman, D., Petersen, S., Senior, A. W., Kavukcuoglu, K., Birney, E., Kohli, P., Jumper, J., & Hassabis, D. (2021). Highly accurate protein structure prediction for the human proteome. Nature, 596(7873), 590-596.

Mirdita, M., Schütze, K., Moriwaki, Y., Heo, L., Ovchinnikov, S., & Steinegger, M. (2022). ColabFold: making protein folding accessible to all. Nature Methods, 19(6), 679-682.

Evans, R., O'Neill, M., Pritzel, A., Antropova, N., Senior, A., Green, T., Žídek, A., Bates, R., Blackwell, S., Yim, J., Ronneberger, O., Bodenstein, S., Zielinski, M., Bridgland, A., Potapenko, A., Cowie, A., Tunyasuvunakool, K., Jain, R., Clancy, E., Kohli, P., Jumper, J., & Hassabis, D. (2022). Protein complex prediction with AlphaFold-Multimer. bioRxiv preprint.

AlphaFold Protein Structure Database. Freely available database of protein structure predictions. URL: https://alphafold.ebi.ac.uk/

ColabFold Server. Accessible interface for protein structure prediction using AlphaFold and related methods. URL: https://colab.research.google.com/github/deepmind/alphafold/
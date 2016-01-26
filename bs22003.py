# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
errmsg='''An error occurred in your code. 
Please check the previous cells have all been run correctly and in order'''
msg=' then run the test again'
def test1():
    try:    
        if enzyme=='TCCGGA':
            print('variable enzyme created correctly')
        else:
            print('variable enzyme not created correctly')
    except:
        print(errmsg)

def test1a():
    if 'cut1' not in globals() and 'cut1' not in locals():
        print("Try using 'cut1 = ' to set the value of cut1")
        return
    if cut1==840:
        print('cut1 value set correctly')
        if 'cut2' not in globals() and 'cut2' not in locals():
            print("Try using 'cut2 = ' to set the value of cut2")
            return    
        if cut2==1571:
            print('Correct answers. cut1 and cut2 set correctly')
        else:
            print('cut2 value incorrect')
    else:
        print('cut1 value incorrect')
        
def test2():
    try:
        if frag1==840:
            print("Fragment 1 correct" )
        else:
            print("Fragment 1 incorrect")
        if frag2==731 :
            print("Fragment 2 correct" )
        else:
            print("Fragment 2 incorrect")
        if frag3== 556 :
            print("Fragment 3 correct" )
        else:
            print("Fragment 3 incorrect")
    except:
        print(errmsg)
        
def test4():
    ps='ctcgcactccctctggccggcccagggcgccttcagcccaacctccccagccccacgggcgccacggaacccgctcgatctcgccgccaactggtagacatggagacccctgcctggccccgggtcccgcgccccgagaccgccgtcgctcggacgctcctgctcggctgggtcttcgcccaggtggccggcgcttcaggcactacaaatactgtggcagcatataatttaacttggaaatcaactaatttcaagacaattttggagtgggaacccaaacccgtcaatcaagtctacactgttcaaataagcactaagtcaggagattggaaaagcaaatgcttttacacaacagacacagagtgtgacctcaccgacgagattgtgaaggatgtgaagcagacgtacttggcacgggtcttctcctacccggcagggaatgtggagagcaccggttctgctggggagcctctgtatgagaactccccagagttcacaccttacctggagacaaacctcggacagccaacaattcagagttttgaacaggtgggaacaaaagtgaatgtgaccgtagaagatgaacggactttagtcagaaggaacaacactttcctaagcctccgggatgtttttggcaaggacttaatttatacactttattattggaaatcttcaagttcaggaaagaaaacagccaaaacaaacactaatgagtttttgattgatgtggataaaggagaaaactactgtttcagtgttcaagcagtgattccctcccgaacagttaaccggaagagtacagacagcccggtagagtgtatgggccaggagaaagggGAATTCagagaaatattctacatcattggagctgtggtatttgtggtcatcatccttgtcatcatcctggctatatctctacacaagtgtagaaaggcaggagtggggcagagctggaaggagaactccccactgaatgtttcataaaggaagcactgttggagctactgcaaatgctatattgcactgtgaccgagaacttttaagaggatagaatacatggaaacgcaaatgagtatttcggagcatgaagaccctggagttcaaaaaactcttgatatgacctgttattaccattagcattctggttttgacatcagcattagtcactttgaaatgtaacgaatggtactacaaccaattccaagttttaatttttaacaccatggcaccttttgcacataacatgctttagattatatattccgcactcaaggagtaaccaggtcgtccaagcaaaaacaaatgggaaaatgtcttaaaaaatcctgggtggacttttgaaaagcttttttttttttttttttttgagacggagtcttgctctgttgcccaggctggagtgcagtagcacgatctcggctcactgcaccctccgtctctcgggttcaagcaattgtctgcctcagcctcccgagtagctgggattacaggtgcgcactaccacaccaagctaatttttgtattttttagtagagatggggtttcaccatcttggccaggctggtcttGAATTCctgacctcagttgatccacccaccttggcctcccaaagtgctagtattatgggcgtgaaccaccatgcccagccgaaaagcttttgaggggctgacttcaatccatgtaggaaagtaaaatggaaggaaattgggtgcatttctaggacttttctaacatatgtctataatatagtgtttaggttcttttttttttcaggaatacatttggaaattcaaaacaattggcaaactttgtattaatgtgttaagtgcaggagacattggtattctgggcaccttcctaatatgctttacaatctgcactttaactgacttaagtggcattaaacatttgagagctaactatatttttataagactactatacaaactacagagtttatgatttaaggtacttaaagcttctatggttgacattgtatatataattttttaaaaaggttttctatatggggattttctatttatgtaggtaatattgttctatttgtatatattgagataatttatttaatatactttaaataaaggtgactgggaattgtta'
    if prettyseq==ps:
        print('congratulations. Your sequence is suitably pretty')
        return
    if prettyseq[cut1+6:cut1+12]==ecori.lower() or prettyseq[cut2+6:cut2+12]==ecori.lower():
        print("Fail. Don't forget to skip the restriction site when adding the fragment" )
    else:
        print('Wrong answer - get each part with text[start:end+1] and use .lower() as required')
        
def test5():
    msg=' then run the test again'
    if 'noncutter' not in globals() or 'largest_frag' not in globals() or 'largest_cutter' not in globals() or 'smallest_frag' not in globals() or 'smallest_cutter' not in globals():
        print('Make sure you have properly defined all five variables'+msg)
        return
    if noncutter==bsai or noncutter.upper()=='GGTCTC' or noncutter.upper()=='BSAI':
        print('Correct. BsaI does not cut.')
    else:
        print('check the results for your non-cutting enzyme'+msg)
        return
        
    if largest_frag == 2127:
        print('Choose an enzyme that does cut'+msg)
        return
    if largest_frag ==2009 and largest_cutter.lower()=='smai':
        print('Correct largest fragment')
    else:
        print('check your results carefully'+msg)
        
def test6():
    if 'variance' not in globals():
        print('ensure that your code runs without an error'+msg)
        return
    if variance==0:
        print('ensure your code adds to the sumofsquares variable'+msg)
        return
    if variance==437112:
        print('you should add to the sumofsquares, not replace it. Check your code'+msg)
        return
    if variance != 873290:
        print(errmsg)
        return
    else:
        print('Correct. The variance has been calculated.')
        
def test7():
    if 'longest' not in globals():
        print('you must run the previous cell without error first. Please fix your code'+msg)
        return
    if longest==1996:
        print('Correct. The longest fragment has been successfully found')
    else:
        print(errmsg)

def test8():
    if not singlecutters:
        print('check your code to make sure you append something to the list of single cutters'+msg)
        return
    if len(singlecutters)==92:
        print('Correct. There are 92 enzymes in the list that cut exactly once')
        return
    else:
        print('check your code. Especially check that you have indented it properly and the if statement is correct'+msg)
        
def test9():
    if '' in overlaps:
        print('Check you have got the smaller value in the first position when findign your overlap in the pattern'+msg)
        return
    if len(overlaps)==42:
        print('congratulations, you have found the overlaps')
        return
    else:
        print(errmsg)
        
def test10():        
    if not 'stickies' in globals():
        print('Ensure your code runs without errors'+msg)
        return
    try:
        assert len(stickies)==14
        assert len(stickies['Blunt'])==5
    except:
        print(errmsg)
        return
    print('All tests passed - stickies are good to go!')
        
        
        
        
        
        
        
        
        
        
        
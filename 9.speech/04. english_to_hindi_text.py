# importing the module
from englisttohindi.englisttohindi import EngtoHindi

# message to be translated
#f=open("sholay.txt", 'r')

message ="""Former police chief Thakur Baldev Singh (Sanjeev Kumar) summons an old colleague and requests him to track down a pair of small-time thieves he once apprehended in the line of duty. The two petty criminals, Veeru (Dharmendra) and Jai (Amitabh Bachchan), are close pals who work together and share everything. They had encountered Thakur in  past (as seen in a flashback), when after being caught by him trying to rob a train, he let them free temporarily to help him fight off bandits. The three succeeded in doing so, but as Thakur lays unconscious after sustaining a wound, Veeru and Jai disputed over leaving him for dead and escaping or letting him live but facing jail themselves. The call was decided over a coin toss, which Jai won. Recollecting that experience, Thakur explains that Veeru and Jai would be the ideal men to help him end the tyranny of Gabbar Singh (Amjad Khan) an infamous bandit wanted by the authorities for a ₹ 50,000 reward. But money is not what Thakur is after. Veeru and Jai are found and brought to Ramgarh. They are told by Thakur that they are to bring Gabbar to him alive for ₹ 20,000 plus the ₹ 50,000 reward. After some difficulty in trusting each other, Thakur demands Veeru and Jai's word and eventually Jai promises that they will do the job and he and Veeru decide to stay in Ramgarh to repel attacks from Gabbar's large gang."""


# creating a EngtoHindi() object
res = EngtoHindi(message)

# displaying the translation
print(res.convert)

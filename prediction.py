def calc_acc(actual_labels, predicted_labels):
    for label,pred in zip(actual_labels, predicted_labels):
        print(label,pred)
        
calc_acc([1,2,3,4,5],[1,2,3,4,5])
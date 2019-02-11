else:
    model_current1 = torch.load('../weights/SE_data_current1_ann' + str(window) + '.pt')
    model_current2 = torch.load('../weights/SE_data_current2_ann' + str(window) + '.pt')
    model_torque = torch.load('../weights/SE_data_torque_ann' + str(window) + '.pt')

    model_current1.eval()
    model_current2.eval()
    model_torque.eval()

    out_current1 = []
    out_current2 = []
    out_torque = []

    true_current1 = []
    true_current2 = []
    true_torque = []

    for i in range(dataset.shape[0]):
        if i + window < dataset.shape[0]:
            inp = np.asarray([dataset[i:i+window, 1:4]])
            inp = Variable(torch.from_numpy(inp).type(torch.FloatTensor).cuda())

            current1_pred = model_current1(inp)
            current2_pred = model_current2(inp)
            torque_pred = model_torque(inp)

#                 print (current1_pred.size())
            out_current1.append(current1_pred.data.cpu().numpy()[0])
            out_current2.append(current2_pred.data.cpu().numpy()[0])
            out_torque.append(torque_pred.data.cpu().numpy()[0])

            true_current1.append(dataset[i+window//2,4])
            true_current2.append(dataset[i+window//2,5])
            true_torque.append(dataset[i+window//2,6])

    print (len(out_current1), len(true_current1))
    out = np.stack([out_current1, true_current1, out_current2, true_current2, out_torque, true_torque])

    np.save('../datasets/results_npy/SE_data_ann' + str(window) + '_out.npy', out)

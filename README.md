# Road Crack Detection
Under development

## Dataset Location and Structure
The dataset used for this project is stored in a shared Box folder. Access it using this link: [Dataset Link](https://buffalo.app.box.com/folder/294130463025).

**Folder Structure in Box**
- Datasets/
    - Crack_Dataset_Name/
        - images/
            - image_name.jpg
        - masks/
            - mask_name.png
    - train.txt
    - val.txt

### How to Use the Dataset
- Download the required `Crack_Dataset_Name/` folder from the box link.
- Place it in your project under `datasets/` directory as shown below:
`datasets/Crack_Dataset_Name/`
- Ensure the paths in your `.env` file or training scripts point to the appropriate location.
